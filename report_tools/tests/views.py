from report_tools.views import ReportView
from report_tools import api
from report_tools.tests.reports import GoogleChartsReport



class GoogleChartsReportView(ReportView):
    api_key = 'google_charts_report'

    def get_report(self, request):
        return GoogleChartsReport()
