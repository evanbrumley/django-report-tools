django-report-tools
===================

Django Report Tools aims to take the pain out of putting charts, graphs 
and tables into your Django projects. It provides a nice class-based
framework to restore a little bit of elegance to your application's 
complex data views.


Features
--------

* Define your reports using the same syntax as Django forms and models
* Use built-in 'renderers' to avoid the hassle of dealing with various 
  charting technologies (currently only the Google Visualization Toolkit is supported)
* Enter chart data in a standardised format
* Build a simple API, allowing for the creation of chart exports or a 'save to dashboard' feature.


A fully-functional example report
-----------------

The following example implements a report with a simple pie chart, rendered
using the Google Visualization Toolkit.

::

    from report_tools.reports import Report
    from report_tools.chart_data import ChartData
    from report_tools.renderers.googlecharts import GoogleChartsRenderer
    from report_tools import charts


    class MyReport(Report):
        renderer = GoogleChartsRenderer

        pie_chart = charts.PieChart(
            title="A nice, simple pie chart",
            width=400,
            height=300
        )

        def get_data_for_pie_chart(self):
            data = ChartData()

            data.add_column("Pony Type")
            data.add_column("Population")

            data.add_row(["Blue", 20])
            data.add_row(["Pink", 20])
            data.add_row(["Magical", 1])

            return data

Read on in the documentation for a full explanation and lots more examples.


Links
-----

Project Home: http://github.com/evanbrumley/django-report-tools

Documentation: http://django-report-tools.readthedocs.org


Installation
------------

To install django-report-tools simply use: ::

    $ pip install django-report-tools

Or alternatively: ::

    $ easy_install requests
