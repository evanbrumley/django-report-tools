class MyReport(Report):
    renderer = GoogleChartsRenderer

    column_chart = charts.ColumnChart(title="Pony Populations", width="500")

    def get_data_for_column_chart(self):
        ...
