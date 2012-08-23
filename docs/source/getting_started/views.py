# myapp/views.py

from django.shortcuts import render
from myapp.reports import MyReport


def my_report(request):
    # Initialise the report
    template = "myapp/my_report.html"
    report = MyReport()
    context = {'report': report}

    return render(request, template, context)
