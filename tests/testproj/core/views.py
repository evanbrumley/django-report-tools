from django.shortcuts import render
from report_tools.views import ReportView
from report_tools import api
from reports import GoogleChartsReport, JQPlotReport



def home(request):
    template = "core/index.html"

    google_charts_report = GoogleChartsReport(prefix='gchart')
    jqplot_report = JQPlotReport(prefix='jqplot')

    context = {
        'google_charts_report': google_charts_report,
        'jqplot_report': jqplot_report,
    }

    return render(request, template, context)


class MyReportView(ReportView):
    api_key = 'my_report'

    def get_report(self, request):
        return GoogleChartsReport()

    def get(self, request):
        template = "core/index.html"
        report = self.get_report(request)
        context = {'report': report}

        return render(request, template, context)

api.register(MyReportView)
