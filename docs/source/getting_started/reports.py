# myapp/reports.py

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
