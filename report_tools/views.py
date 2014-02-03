import functools

try:
    import json
except ImportError:
    import simplejson as json

from django.http import HttpResponse, Http404
from django.views.generic import View
from django.utils.decorators import classonlymethod
from django.utils.safestring import mark_safe




from report_tools.api import (ChartNotFoundError, report_api_registry,
    OVERRIDE_PARAMS__CHART_HEIGHT, OVERRIDE_PARAMS__CHART_WIDTH,
    OVERRIDE_PARAMS__CHART_TITLE)


class ChartPermissionError(Exception):
    pass


class ReportView(View):
    def security_check(self, request):
        return True
    
    def get_report(self, request, prefix=None):
        raise NotImplementedError
    
    def _get_report(self, request, prefix=None):
        report = self.get_report(request)
        
        if prefix:
            report.set_prefix(prefix)
    
        chart_height = request.GET.get(OVERRIDE_PARAMS__CHART_HEIGHT, None)
        chart_width = request.GET.get(OVERRIDE_PARAMS__CHART_WIDTH, None)
        chart_title = request.GET.get(OVERRIDE_PARAMS__CHART_TITLE, None)
        
        for chart_name, chart in report.charts.iteritems():
            if chart_height is not None:
                chart.options['height'] = chart_height
            if chart_width is not None:
                chart.options['width'] = chart_width
            if chart_title is not None:
                chart.options['title'] = chart_title
                
        return report
    
    def get_chart(self, request, chart_name, prefix=None):
        if not self.security_check(request):
            raise ChartPermissionError("Chart access forbidden")
        
        report = self._get_report(request, prefix)

        try:
            chart = report[chart_name]
        except KeyError:
            raise ChartNotFoundError("Chart %s not found in this report" % chart_name)
        
        return chart
    
    def api_get(self, request, chart_name, prefix=None):
        chart = self.get_chart(request, chart_name, prefix)

        if chart:
            html = mark_safe(u'%s' % chart)
            attrs = chart.attrs
        else:
            html = mark_safe(self.security_failure_message)
            attrs = {}
        
        return_data = {
            'html': html,
            'attrs': attrs,
        }
        
        return HttpResponse(json.dumps(return_data), mimetype='application/javascript')

    @classonlymethod
    def as_api_view(cls, **initkwargs):
        """
        Main entry point for an api request-response process.
        """
        # sanitize keyword arguments
        for key in initkwargs:
            if key in cls.http_method_names:
                raise TypeError(u"You tried to pass in the %s method name as a "
                                u"keyword argument to %s(). Don't do that."
                                % (key, cls.__name__))
            if not hasattr(cls, key):
                raise TypeError(u"%s() received an invalid keyword %r" % (
                    cls.__name__, key))

        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            return self.api_dispatch(request, *args, **kwargs)

        # take name and docstring from class
        functools.update_wrapper(view, cls, updated=())

        # and possible attributes set by decorators
        # like csrf_exempt from dispatch
        functools.update_wrapper(view, cls.dispatch, assigned=())
        return view
    
    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            if '_format' in request.GET:
                method_name = request.method.lower() + '_' + request.GET['_format'] + '_format'
            else:
                method_name = request.method.lower()
            handler = getattr(self, method_name, self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        self.request = request
        self.args = args
        self.kwargs = kwargs
        return handler(request, *args, **kwargs)
       
    def api_dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right api method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            method_name = 'api_' + request.method.lower()
            handler = getattr(self, method_name, self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        self.request = request
        self.args = args
        self.kwargs = kwargs
        return handler(request, *args, **kwargs)
    

class ReportAPIDispatchView(View):
    def dispatch(self, request, report_api_key, chart_name):
        report_view_class = report_api_registry.get_report_view_class(report_api_key)

        if not report_view_class:
            raise Http404
        
        report_view = report_view_class()
        return report_view.api_dispatch(request, chart_name)
