from report_tools.renderers import ChartRenderer


class MyChartRenderer(ChartRenderer):
    @classmethod
    def render_piechart(cls, chart_id, options, data, renderer_options):
        return "<div id='%s' class='placeholder'>Pie Chart</div>" % chart_id

    @classmethod
    def render_columnchart(cls, chart_id, options, data, renderer_options):
        return "<div id='%s' class='placeholder'>Column Chart</div>" % chart_id

    @classmethod
    def render_barchart(cls, chart_id, options, data, renderer_options):
        return "<div id='%s' class='placeholder'>Bar Chart</div>" % chart_id

    @classmethod
    def render_linechart(cls, chart_id, options, data, renderer_options):
        return "<div id='%s' class='placeholder'>Line Chart</div>" % chart_id