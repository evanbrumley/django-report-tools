from report_tools.renderers import JQPlotRenderer
from report_tools.charts.jqplot import JQPlotChart


class MyReport(Report):
    renderer = JQPlotRenderer

    multiseries_xy_line_chart = JQPlotChart(
        title="Pony Sparkliness vs. Age",
        height="300",
        width="400",
        renderer_options={
            'title': "Pony Sparkliness vs. Age",
            'legend': {'show': True, 'location': 'nw'},
            'seriesColors': ['blue', 'pink', 'octarine'],
            'series': [{'label': 'Blue'}, {'label': 'Pink'}, {'label': 'Magical'}]
        }
    )

    def get_data_for_multiseries_xy_line_chart(self):
        # Note use of a normal python array - ChartData objects
        # don't support 3 dimensional arrays yet!
        data = [
            [[1, 10], [5, 12], [10, 14]],  # blue
            [[1, 14], [5, 15], [10, 20]],  # pink
            [[1, 30], [5, 40], [10, 60]],  # magical
        ]
        
        return data
