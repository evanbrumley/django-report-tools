from django.test import TestCase
from django.test.client import RequestFactory
from report_tools.tests.reports import GoogleChartsReport
from report_tools import api
from report_tools.tests.views import GoogleChartsReportView



class GoogleChartsTest(TestCase):
    def test_pie_chart(self):
        """
        Test google charts rendering of a pie chart
        """
        report = GoogleChartsReport()
        chart_html = u'%s' % report['pie_chart']

        self.assertRegexpMatches(chart_html, r'google\.visualization\.PieChart')

    def test_column_chart(self):
        """
        Test google chart rendering of a column chart
        """
        report = GoogleChartsReport()
        chart_html = u'%s' % report['column_chart']

        self.assertRegexpMatches(chart_html, r'google\.visualization\.ColumnChart')

    def test_line_chart(self):
        """
        Test google chart rendering of a column chart
        """
        report = GoogleChartsReport()
        chart_html = u'%s' % report['line_chart']

        self.assertRegexpMatches(chart_html, r'google\.visualization\.LineChart')

    def test_bar_chart(self):
        """
        Test google chart rendering of a bar chart
        """
        report = GoogleChartsReport()
        chart_html = u'%s' % report['bar_chart']

        self.assertRegexpMatches(chart_html, r'google\.visualization\.BarChart')


class APITest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/')

        api.register(GoogleChartsReportView)

    def test_internal_api_get(self):
        """
        Test the internal get_chart function
        """
        chart = api.get_chart(self.request, 'google_charts_report', 'pie_chart')
        chart_html = u'%s' % chart
        self.assertRegexpMatches(chart_html, r'google\.visualization\.PieChart')

    def test_report_not_found(self):
        """
        Make sure asking for a non-existant report throws an appropriate error
        """
        with self.assertRaises(api.ReportNotFoundError):
            chart = api.get_chart(self.request, 'doogle_charts_report', 'pie_chart')

    def test_chart_not_found(self):
        """
        Make sure asking for a non-existant chart throws an appropriate error
        """
        with self.assertRaises(api.ChartNotFoundError):
            chart = api.get_chart(self.request, 'google_charts_report', 'delicious_pie_chart')
