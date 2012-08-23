# myapp/views.py

from django.shortcuts import render
from myapp.reports import MyReport
from report_tools.views import ReportView


class MyReportView(ReportView):
    def get_report(self, request):
        return MyReport()
        
    def get(self, request):
        template = 'myapp/my_report.html'
        context = {
            'report': self.get_report(request),
        }
        
        return render(request, template, context)
