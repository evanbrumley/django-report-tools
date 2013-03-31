from report_tools.reports import Report
from report_tools.chart_data import ChartData
from report_tools.renderers.googlecharts import GoogleChartsRenderer
from report_tools import charts



class MyReport(Report):
    renderer = GoogleChartsRenderer

    pie_chart = charts.PieChart(title="Pony Populations", width="500")
    template_chart = charts.TemplateChart(title="Pony Types", template="core/template_chart.html")
    column_chart = charts.ColumnChart(title="Pony Populations", width="500")
    multiseries_column_chart = charts.ColumnChart(title="Pony Populations by Country", width="500")
    bar_chart = charts.BarChart(title="Pony Populations", width="500")
    multiseries_bar_chart = charts.BarChart(title="Pony Populations by Country", width="500")
    line_chart = charts.LineChart(title="Blue Pony Population - 2009-2012", width="500")
    multiseries_line_chart = charts.LineChart(title="Pony Populations - 2009-2012", width="500")
    naughty_pie_chart = charts.PieChart(title="Pony </script>Populations", width="500")

    def get_data_for_line_chart(self):
        data = ChartData()

        data.add_column("Test Period")
        data.add_column("Blue Pony Population")

        data.add_row(["2009-10", 20])
        data.add_row(["2010-11", 18])
        data.add_row(["2011-12", 100])

        return data

    def get_data_for_multiseries_line_chart(self):
        data = ChartData()

        data.add_column("Test Period")
        data.add_column("Blue Pony Population")
        data.add_column("Pink Pony Population")
        data.add_column("Magical Pony Population")

        data.add_row(["2009-10", 20, 10, 50])
        data.add_row(["2010-11", 18, 8, 60])
        data.add_row(["2011-12", 100, 120, 2])

        return data

    def get_data_for_bar_chart(self):
        data = ChartData()

        data.add_column("Pony Type")
        data.add_column("Population")

        data.add_row(["Blue", 20])
        data.add_row(["Pink", 20])
        data.add_row(["Magical", 1])

        return data

    def get_data_for_multiseries_bar_chart(self):
        data = ChartData()

        data.add_column("Pony Type")
        data.add_column("Australian Population")
        data.add_column("Switzerland Population")
        data.add_column("USA Population")

        data.add_row(["Blue", 5, 10, 5])
        data.add_row(["Pink", 10, 2, 8])
        data.add_row(["Magical", 1, 0, 0])

        return data

    def get_data_for_column_chart(self):
        data = ChartData()

        data.add_column("Pony Type")
        data.add_column("Population")

        data.add_row(["Blue", 20])
        data.add_row(["Pink", 20])
        data.add_row(["Magical", 1])

        return data

    def get_data_for_multiseries_column_chart(self):
        data = ChartData()

        data.add_column("Pony Type")
        data.add_column("Australian Population")
        data.add_column("Switzerland Population")
        data.add_column("USA Population")

        data.add_row(["Blue", 5, 10, 5])
        data.add_row(["Pink", 10, 2, 8])
        data.add_row(["Magical", 1, 0, 0])

        return data

    def get_data_for_pie_chart(self):
        data = ChartData()

        data.add_column("Pony Type")
        data.add_column("Population")

        data.add_row(["Blue", 20])
        data.add_row(["Pink", 20])
        data.add_row(["Magical", 1])

        return data

    def get_data_for_naughty_pie_chart(self):
        data = ChartData()

        data.add_column("Pony</script> &&&Type")
        data.add_column("Population")

        data.add_row(["Blue", 20])
        data.add_row(["Pink</script>&&&", 20])
        data.add_row(["Magical", 1])

        return data

    def get_data_for_template_chart(self):
        pony_types = [
            ('Blue', 'Equus Caeruleus'),
            ('Pink', 'Equus Roseus'),
            ('Magical', 'Equus Magica')
        ]

        template_context = {
            'pony_types': pony_types
        }

        return template_context
