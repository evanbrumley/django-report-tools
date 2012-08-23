from report_tools.reports import Report
from report_tools.chart_data import ChartData
from report_tools.renderers.googlecharts import GoogleChartsRenderer
from report_tools import charts



class GenericReport(Report):
    template_chart = charts.TemplateChart(template="templates/examples/template_chart.html")

    def get_data_for_template_chart(self):
        template_context = {
            'pony_types': ["Blue", "Pink", "Magical"]
        }

        return template_context


class GoogleChartsReport(Report):
    renderer = GoogleChartsRenderer

    pie_chart = charts.PieChart(width="500")
    column_chart = charts.ColumnChart(width="500")
    line_chart = charts.LineChart(width="500")
    bar_chart = charts.BarChart(width="500")

    def get_single_series_data(self):
        data = ChartData()

        data.add_column("Pony Type")
        data.add_column("Population")

        data.add_row(["Blue", 20])
        data.add_row(["Pink", 20])
        data.add_row(["Magical", 1])

        return data

    def get_multi_series_data(self):
        data = ChartData()

        data.add_column("Pony Type")
        data.add_column("Australian Population")
        data.add_column("Switzerland Population")
        data.add_column("USA Population")

        data.add_row(["Blue", (5, {'formatted_value': "Five"}), 10, 5])
        data.add_row(["Pink", 10, 2, 8])
        data.add_row(["Magical", 1, 0, 0])

        return data

    def get_data_for_pie_chart(self):
        return self.get_single_series_data()

    def get_data_for_column_chart(self):
        return self.get_multi_series_data()

    def get_data_for_bar_chart(self):
        return self.get_multi_series_data()

    def get_data_for_line_chart(self):
        return self.get_multi_series_data()