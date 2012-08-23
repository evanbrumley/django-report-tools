from report_tools.views import ReportView
from report_tools.api import register


class MyReportView(ReportView):
    ...

register(MyReportView, 'myreportview_api_key')
