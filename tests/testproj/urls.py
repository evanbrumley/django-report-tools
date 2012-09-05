from django.conf import settings
from django.conf.urls import patterns, include, url
from testproj.core.views import MyReportView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproj.views.home', name='home'),
    # url(r'^testproj/', include('testproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'testproj.core.views.home', name='index'),
    url(r'^class_based/$', MyReportView.as_view(), name='class_based'),
    url(r'^api/', include('report_tools.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views', url(r'^static/(?P<path>.*)$', 'serve'),)
