class MyReport(Report):
    renderer = GoogleChartsRenderer

    line_chart = charts.LineChart(title="Blue Pony Population - 2009-2012", width="500")
    multiseries_line_chart = charts.LineChart(title="Pony Populations - 2009-2012", width="500")

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