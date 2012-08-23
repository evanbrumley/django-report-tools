class MyReport(Report):
    renderer = GoogleChartsRenderer

    stacked_column_chart = charts.ColumnChart(
        title="Pony Populations", 
        width="500",
        renderer_options={
            'isStacked': True,
            'legend': {
                'position': 'none',
            },
            'backgroundColor': '#f5f5f5',
            'series': [
                {'color': '#ff0000'},
                {'color': '#0000ff'},
            ],
        }

    )

    def get_data_for_stacked_column_chart(self):
        ...
