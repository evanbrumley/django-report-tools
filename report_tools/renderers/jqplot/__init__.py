from copy import copy, deepcopy

from django.utils import simplejson as json
from django.template.loader import render_to_string

from report_tools.chart_data import ChartData


DEFAULT_HEIGHT = 300
DEFAULT_WIDTH = 400


class JSRaw(int):
    """
    Hack to allow including raw Javascript code in simplejson.dumps
    output. Objects of this sort are dumped as raw strings.

    Props to Michael Elsdorfer on github for this little piece of crazy
    https://github.com/simplejson/simplejson/issues/20
    """
    def __new__(self, string):
        instance = int.__new__(self, 0)
        instance.string= string
        return instance
    def __repr__(self):
        return self.string
    def __unicode__(self):
        return self.string
    def __str__(self):
        return self.string


class JQPlotRenderer(object):
    @classmethod
    def process_renderer_options(cls, renderer_options):
        """
        Go through the renderer options and change any entries marked
        'renderer' or 'formatter' to JSRaw instances
        """
        renderer_options_copy = deepcopy(renderer_options)

        for key, val in renderer_options.iteritems():
            if key in ('renderer', 'formatter'):
                renderer_options_copy[key] = JSRaw(val)
            elif isinstance(val, dict):
                renderer_options_copy[key] = cls.process_renderer_options(val)

        return renderer_options_copy

    @classmethod
    def render_piechart(cls, chart_id, options, data, renderer_options):
        base_renderer_options = {
            'seriesDefaults': {
                'renderer': '$.jqplot.PieRenderer',
                'rendererOptions': {
                    'showDataLabels': True,
                },
            },
            'legend': {
                'show': True,
            }
        }

        data_array = [data.to_list()]

        return cls.base_render(chart_id, options, data_array, base_renderer_options, renderer_options)

    @classmethod
    def render_columnchart(cls, chart_id, options, data, renderer_options):
        ticks, data = cls.convert_chart_data(data)

        series_labels = [col.name for col in data.get_columns()]

        series_options = []
        for label in series_labels:
            series_options.append({'label': label})

        base_renderer_options = {
            'seriesDefaults': {
                'renderer': '$.jqplot.BarRenderer',
                'pointLabels': {
                    'show': True,
                }
            },
            'legend': {
                'show': True,
            },
            'axes': {
                'xaxis': {
                    'renderer': '$.jqplot.CategoryAxisRenderer',
                    'ticks': ticks,
                }
            },
            'series': series_options,
        }

        data_array = data.to_list_transposed()

        return cls.base_render(chart_id, options, data_array, base_renderer_options, renderer_options)

    @classmethod
    def render_barchart(cls, chart_id, options, data, renderer_options):
        ticks, data = cls.convert_chart_data(data)

        series_labels = [col.name for col in data.get_columns()]

        series_options = []
        for label in series_labels:
            series_options.append({'label': label})

        base_renderer_options = {
            'seriesDefaults': {
                'renderer': '$.jqplot.BarRenderer',
                'rendererOptions': {
                    'barDirection': 'horizontal',
                },
                'pointLabels': {
                    'show': True,
                },
            },
            'legend': {
                'show': True,
            },
            'axes': {
                'yaxis': {
                    'renderer': '$.jqplot.CategoryAxisRenderer',
                    'ticks': ticks,
                }
            },
            'series': series_options,
        }

        data_array = data.to_list_transposed()

        return cls.base_render(chart_id, options, data_array, base_renderer_options, renderer_options)

    @classmethod
    def render_linechart(cls, chart_id, options, data, renderer_options):
        ticks, data = cls.convert_chart_data(data)

        series_labels = [col.name for col in data.get_columns()]

        series_options = []
        for label in series_labels:
            series_options.append({'label': label})

        base_renderer_options = {
            'seriesDefaults': {
                'pointLabels': {
                    'show': True,
                },
            },
            'legend': {
                'show': True,
            },
            'axes': {
                'xaxis': {
                    'renderer': '$.jqplot.CategoryAxisRenderer',
                    'ticks': ticks,
                }
            },
            'series': series_options,
        }

        data_array = data.to_list_transposed()

        return cls.base_render(chart_id, options, data_array, base_renderer_options, renderer_options)

    @classmethod
    def base_render(cls, chart_id, options, data_array, base_renderer_options, renderer_options):
        template = "report_tools/renderers/jqplot/chart.html"
        options = copy(base_renderer_options)
        options.update(renderer_options)

        options = cls.process_renderer_options(options)

        context = {
            'chart_id': chart_id,
            'options': json.dumps(options),
            'data': json.dumps(data_array),
            'height': options.get('height', DEFAULT_HEIGHT),
            'width': options.get('width', DEFAULT_WIDTH),
        }

        return render_to_string(template, context)

    @classmethod
    def convert_chart_data(cls, data):
        ticks = []

        for row in data.get_rows():
            ticks.append(row[0].data)

        new_data = deepcopy(data)
        new_data.delete_column(0)

        return ticks, new_data
