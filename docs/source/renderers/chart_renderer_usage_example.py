class MyReport(Report):
    renderer = GoogleChartsRenderer

    column_chart = charts.ColumnChart(title="Pony Populations", width="500")

    column_chart_other_renderer = charts.ColumnChart(
        title="Pony Populations", 
        width="500", 
        renderer=SomeOtherRenderer
    )

    def get_data_for_column_chart(self):
        ...

    def get_data_for_column_chart_other_renderer(self):
        ...