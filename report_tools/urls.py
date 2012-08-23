from views import ReportAPIDispatchView

from django.conf.urls.defaults import *
from django.conf import settings



urlpatterns = patterns('',
    url(r'^(?P<report_api_key>\w+)/(?P<chart_name>\w+)/$', ReportAPIDispatchView.as_view(), name="reports-api-chart"),
)
