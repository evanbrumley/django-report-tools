from django.shortcuts import render
from report_tools.views import ReportView
from report_tools import api
from reports import MyReport



class MyReportView(ReportView):
    api_key = 'my_report'

    def get_report(self, request):
        return MyReport()

    def get(self, request):
        template = "core/index.html"
        report = self.get_report(request)
        context = {'report': report}

        return render(request, template, context)

api.register(MyReportView)
