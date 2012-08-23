from django.db import models
from django.utils.copycompat import deepcopy
from django.utils.datastructures import SortedDict
from django.utils.encoding import StrAndUnicode
from django.utils.safestring import mark_safe

from charts import Chart

__all__ = ('BaseReport', 'Report')


def pretty_name(name):
    """Converts 'first_name' to 'First name'"""
    if not name:
        return u''
    return name.replace('_', ' ').capitalize()
    

def get_declared_charts(bases, attrs, with_base_charts=True):
    """
    Create a list of report chart instances from the passed in 'attrs', plus any
    similar charts on the base classes (in 'bases'). This is used by the Report
    metaclass.
    
    If 'with_base_charts' is True, all charts from the bases are used.
    Otherwise, only charts in the 'declared_charts' attribute on the bases are
    used.
    """
    charts = [(chart_name, attrs.pop(chart_name)) for chart_name, obj in attrs.items() if isinstance(obj, Chart)]
    
    charts.sort(key=lambda x: x[1].creation_counter)
    
    # If this class is subclassing another Report, add that Report's charts.
    # Note that we loop over the bases in *reverse*. This is necessary in order
    # to preserver the correct order of charts.
    if with_base_charts:
        for base in bases[::-1]:
            if hasattr(base, 'base_charts'):
                charts = base.base_charts.items() + charts
    else:
        for base in bases[::-1]:
            if hasattr(base, 'declared_charts'):
                charts = base.declared_charts.items() + charts
    
    return SortedDict(charts)


class DeclarativeChartsMetaclass(type):
    """
    Metaclass that converts Chart attributes to a dictionary called
    'base_charts', taking into account parent class 'base_charts' as well.
    """
    def __new__(cls, name, bases, attrs):
        attrs['base_charts'] = get_declared_charts(bases, attrs)
        new_class = super(DeclarativeChartsMetaclass,
                          cls).__new__(cls, name, bases, attrs)
        
        return new_class


class BaseReport(StrAndUnicode):
    def __init__(self, data=None, prefix=None):
        self.data = data or {}
        self.prefix = prefix
        
        # The base_charts class attribute is the *class-wide* definition of
        # charts. Because a particular *instance* of the class might want to
        # alter self.charts, we create self.charts here by copying base_charts.
        # Instances should always modify self.charts; they should not modify
        # self.base_charts
        self.charts = deepcopy(self.base_charts)
    
    def __unicode__(self):
        return "WHOLE REPORT PRINTING NOT YET IMPLEMENTED" # TODO
    
    def __iter__(self):
        for name, chart in self.charts.items():
            data = self._get_chart_data(name)
            yield BoundChart(self, chart, name, data)
            
    def __getitem__(self, name):
        "Returns a BoundChart with the given name"
        try:
            chart = self.charts[name]
        except KeyError:
            raise KeyError('Key %r not found in Report' % name)
            
        data = self._get_chart_data(name)
        return BoundChart(self, chart, name, data, self.prefix)
    
    def set_prefix(self, prefix):
        self.prefix = prefix
    
    def _get_chart_data(self, name):
        callback_name = 'get_data_for_%s' % name
        if name in self.data:
            data = self.data[name]
        elif hasattr(self, callback_name):
            data = getattr(self, callback_name)()
            self.data[name] = data
        else:
            data = None
            
        return data
    
    def setup(self, request):
        pass
    
    def api_setup(self, request):
        return self.setup(request)

        
class Report(BaseReport):
    "A collection of charts, plus their associated data."
    # This is a separate class from BaseReport in order to abstract the way
    # self.charts is specified. This class (Report) is the one that does the
    # fancy metaclass stuff purely for the semantic sugar -- it allows one to
    # define a report using declarative syntax.
    # BaseReport itself has no way of designating self.charts
    __metaclass__ = DeclarativeChartsMetaclass
    
    
class BoundChart(StrAndUnicode):
    "A chart plus data"
    def __init__(self, report, chart, name, data=None, prefix=None):
        self.report = report
        self.chart = chart
        self.name = name
        self.data = data
        self.prefix = prefix
        self.attrs = self.chart.attrs
        self.options = self.chart.options
        self.renderer_options = self.chart.renderer_options
        
        if self.chart.title is None:
            self.title = pretty_name(name)
        else:
            self.title = self.chart.title
        
    def __unicode__(self):
        """Renders this chart"""
        return self.render()
    
    @property
    def chart_id(self):
        if self.prefix:
            chart_id = 'chartid_%s_%s' % (self.prefix, self.name)
        else:
            chart_id = 'chartid_%s' % self.name
            
        return chart_id
    
    def render(self):
        base_renderer = getattr(self.report, 'renderer', None)
        
        return mark_safe(self.chart.render(self.chart_id, self.data, base_renderer=base_renderer))