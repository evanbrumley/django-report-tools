from django.utils.encoding import smart_unicode
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe



class Chart(object):
    # Tracks each time a Chart instance is created. Used to retain order.
    creation_counter = 0
    name = None
    
    def __init__(self, title=None, renderer=None, renderer_options={}, attrs={}):
        if title is not None:
            title = smart_unicode(title)
            
        self.title = title
        
        self.renderer = renderer
        self.renderer_options = renderer_options
        self.attrs = attrs
        self.options = {}
        
        self.creation_counter = Chart.creation_counter
        Chart.creation_counter += 1
        
    def __unicode__(self):
        return self.name
        
    def render(self, chart_id, data, base_renderer=None):
        if not self.name:
            raise NotImplementedError
        
        if self.renderer:
            renderer = self.renderer
        else:
            renderer = base_renderer
        
        if renderer:
            render_method_name = 'render_' + self.name
            render_method = getattr(renderer, render_method_name, None)
            
            if render_method:
                return render_method(chart_id, self.options, data, self.renderer_options)
            else:
                raise NotImplementedError
        else:
            raise RendererRequiredError

    @classmethod
    def get_empty_data_object(cls, sort=None):
        raise NotImplementedError
    

class RendererRequiredError(Exception):
    pass


class DimensionedChart(Chart):
    def __init__(self, *args, **kwargs):
        width = kwargs.pop('width', None)
        height = kwargs.pop('height', None)

        super(DimensionedChart, self).__init__(*args, **kwargs)

        self.options['width'] = width
        self.options['height'] = height


class PieChart(DimensionedChart):
    name = 'piechart'


class BarChart(DimensionedChart):
    name = 'barchart'


class ColumnChart(DimensionedChart):
    name = 'columnchart'


class LineChart(DimensionedChart):
    name = 'linechart'


class TemplateChart(Chart):
    name = 'templatechart'
    
    def __init__(self, template, *args, **kwargs):
        self.template = template
        super(TemplateChart, self).__init__(*args, **kwargs)

    def render(self, chart_id, data={}, base_renderer=None):
        if 'chart_id' not in data:
            data['chart_id'] = chart_id
        
        html = render_to_string(self.template, data)
        return mark_safe(html)


class DummyChart(Chart):
    def render(self, chart_id, data, *args, **kwargs):
        return u'%s' % data
