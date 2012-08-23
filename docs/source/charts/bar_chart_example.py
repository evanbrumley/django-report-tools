class MyReport(Report):
    renderer = GoogleChartsRenderer

    bar_chart = charts.BarChart(title="Pony Populations", width="500")
    multiseries_bar_chart = charts.BarChart(title="Pony Populations by Country", width="500")

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