from report_tools.renderers import ChartRenderer, ChartRendererError
from report_tools.renderers.googlecharts.gviz_api import gviz_api
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode

try:
  import json
except ImportError:
  import simplejson as json


DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 300


class JSONEncoderForHTML(json.JSONEncoder):
    """
    An encoder that produces JSON safe to embed in HTML.

    To embed JSON content in, say, a script tag on a web page, the
    characters &, < and > should be escaped. They cannot be escaped
    with the usual entities (e.g. &amp;) because they are not expanded
    within <script> tags.

    Originally from the simplejson project:
    https://github.com/simplejson/simplejson
    """

    def encode(self, o):
        # Override JSONEncoder.encode because it has hacks for
        # performance that make things more complicated.
        chunks = self.iterencode(o)
        if self.ensure_ascii:
            return ''.join(chunks)
        else:
            return u''.join(chunks)

    def iterencode(self, o):
        chunks = super(JSONEncoderForHTML, self).iterencode(o)
        for chunk in chunks:
            chunk = chunk.replace('&', '\\u0026')
            chunk = chunk.replace('<', '\\u003c')
            chunk = chunk.replace('>', '\\u003e')
            yield chunk


class GoogleChartsRenderer(ChartRenderer):
    """
    Renders basic charts using the Google Visualization API
    Requires the following to be added to your pages:

    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    """
    @classmethod
    def render_piechart(cls, chart_id, options, data, renderer_options):
        template = 'report_tools/renderers/googlecharts/piechart.html'
        return cls._render(chart_id, options, data, renderer_options, template)
        
    @classmethod
    def render_columnchart(cls, chart_id, options, data, renderer_options):
        template = 'report_tools/renderers/googlecharts/columnchart.html'
        return cls._render(chart_id, options, data, renderer_options, template)
    
    @classmethod
    def render_barchart(cls, chart_id, options, data, renderer_options):
        template = 'report_tools/renderers/googlecharts/barchart.html'
        return cls._render(chart_id, options, data, renderer_options, template)
    
    @classmethod
    def render_linechart(cls, chart_id, options, data, renderer_options):
        template = 'report_tools/renderers/googlecharts/linechart.html'
        return cls._render(chart_id, options, data, renderer_options, template)
    
    @classmethod
    def _render(cls, chart_id, options, data, renderer_options, template):
        gchart_options = cls._process_base_options(options)
        gchart_options.update(renderer_options)
        data_json = mark_safe(GoogleChartsDataConverter.convert_to_datatable_json(data))
        
        context = {
            'chart_id': chart_id,
            'data_json': data_json,
            'options': mark_safe(json.dumps(gchart_options, cls=JSONEncoderForHTML)),
        }
        
        html = render_to_string(template, context)
        return mark_safe(html)
    
    @classmethod
    def _process_base_options(cls, options):
        gchart_options = {
            'width': options.get('width', None),
            'height': options.get('height', None),
        }
        
        return gchart_options
    
    
class GoogleChartsDataConverter(object):
    @classmethod
    def convert_to_datatable_json(cls, data):
        # TODO: At some point we may need to expand this method to
        # account for non label-number chartdata types (i.e. geodata)
        return cls.convert_standard_chartdata_to_datatable_json(data)
    
    @classmethod
    def convert_standard_chartdata_to_datatable_json(cls, data):
        """
        Converts a ChartData object to a datatable json blob assuming
        that the first column is a label and all subsequent columns are numbers
        """
        cols = data.get_columns()
        
        label_col = cols[0]
        data_cols = cols[1:]
        
        if 'datatype' not in label_col.metadata:
            label_col.metadata['datatype'] = 'string'
        
        for col in data_cols:
            if 'datatype' not in col.metadata:
                col.metadata['datatype'] = 'number'
        
        return cls.convert_generic_to_datatable_json(data)

    @classmethod
    def convert_generic_to_datatable_json(cls, data):
        cols = data.get_columns()
        
        for col in cols:
            if 'datatype' not in col.metadata:
                col.metadata['datatype'] = 'string'

        description = {}
        index = 1
        columns_order = []
        for col in cols:
            columns_order.append(str(index))
            description[str(index)] = (col.metadata['datatype'], col.name)
            index += 1

        datatable_data = []
            
        for row in data.get_rows():
            datatable_data_row = {}
            index = 1
            for datum_cell in row:
                data_description = datum_cell.metadata.get('formatted_value', datum_cell.data)
                datatable_data_row[str(index)] = (datum_cell.data, force_unicode(data_description))
                index += 1
            
            datatable_data.append(datatable_data_row)
        
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(datatable_data)
        
        return data_table.ToJSon(columns_order=columns_order)
