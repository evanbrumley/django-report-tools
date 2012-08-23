from copy import copy

from django.http import QueryDict



OVERRIDE_PARAMS__CHART_HEIGHT = '_height'
OVERRIDE_PARAMS__CHART_WIDTH = '_width'
OVERRIDE_PARAMS__CHART_TITLE = '_title'


class ReportAPIRegistry(object):
    def __init__(self):
        self.reports = {}

    @property
    def api_keys(self):
        return self.reports.keys()

    def register(self, report_view_class, api_key):
        if api_key not in self.reports:
            self.reports[api_key] = report_view_class
    
    def get_report_view_class(self, api_key):
        return self.reports.get(api_key, None)
    

report_api_registry = ReportAPIRegistry()


def register(report_view_class, api_key=None):
    if api_key:
        report_api_registry.register(report_view_class, api_key)
    else:
        report_api_registry.register(report_view_class, report_view_class.api_key)
    
    
def get_chart(request, api_key, chart_name, parameters=None, prefix=None):
    request = copy(request)
    if parameters is not None:
        new_get = QueryDict('', mutable=True)
        new_get.update(parameters)
        request.GET = new_get
    
    report_view_class = report_api_registry.get_report_view_class(api_key)

    if not report_view_class:
        raise ReportNotFoundError("Report not found for api key '%s'. Available reports are '%s'." %
            (api_key, ', '.join(report_api_registry.api_keys)))
    
    report_view = report_view_class()
    
    return report_view.get_chart(request, chart_name, prefix)


class ReportNotFoundError(Exception):
    pass


class ChartNotFoundError(Exception):
    pass
