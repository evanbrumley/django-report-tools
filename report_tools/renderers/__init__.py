class ChartRenderer(object):
    @classmethod
    def render_piechart(cls, chart_id, options, data, renderer_options):
        raise NotImplementedError

    @classmethod
    def render_columnchart(cls, chart_id, options, data, renderer_options):
        raise NotImplementedError

    @classmethod
    def render_barchart(cls, chart_id, options, data, renderer_options):
        raise NotImplementedError

    @classmethod
    def render_linechart(cls, chart_id, options, data, renderer_options):
        raise NotImplementedError


class ChartRendererError(Exception):
    pass
