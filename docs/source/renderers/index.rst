Chart Renderers
===============

Chart renderers control the way reports display on your site. There are currently
two bundled renderers - Google Chart Tools and jqPlot. More are on the way,
and it's easy to write one for your own favourite charting package.

Included Renderers
------------------

.. toctree::
   :maxdepth: 1

   googlecharts/index
   jqplot/index

Basic Usage
-----------

Renderers are typically defined on your report objects. For example:

.. literalinclude:: basic_renderer_usage_example.py
    :language: python
    :emphasize-lines: 2

You can also select renderers on a chart-by-chart basis. For example:

.. literalinclude:: chart_renderer_usage_example.py
    :language: python
    :emphasize-lines: 9

Talking to Your Renderer
------------------------

Above and beyond the basic options described in the :doc:`chart documentation </charts/index>`,
individual renderers usually provide a lot of unique customization 
options. You can set these by passing in a ``renderer_options`` dictionary to
the chart. For example, for a red background using the Google Charts renderer:

.. literalinclude:: renderer_options_example.py
    :language: python

For information on the the various options available, refer to the documentation
for your chosen renderer above.

Writing Your Own
----------------

A very simple stub of a chart renderer looks something like the following:

.. literalinclude:: chart_renderer_example.py
    :language: python


When a chart is rendered, it goes to the selected chart renderer class and tries to call an
appropriate class method. This method will typically be named ``render_xxx`` where ``xxx``
is a lower case representation of the chart's class name. All rendering methods take the
same parameters:

chart_id
    A unique identifier for the chart. Safe for use as an html element id.

options
    If a chart accepts additional parameters, such as width, height or template,
    they will be loaded into this dictionary.

data
    The data returned by the chart's ``get_data_for_xxx`` method. This typically
    comes in as a ChartData object, so you'll need to wrangle it into something
    your charting package can read.

renderer_options
    The renderer options specified when the chart was defined on the report.
