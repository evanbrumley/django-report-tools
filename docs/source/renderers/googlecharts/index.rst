Google Charts
=============

.. class:: report_tools.renderers.googlecharts.GoogleChartsRenderer

The google charts renderer uses 
`Google Chart Tools <https://developers.google.com/chart/interactive/docs/index>`_ 
to render the built-in chart types.

Chart Support
-------------

The google chart renderer supports all the built-in chart types described
in the :doc:`chart documentation </charts/index>`. This includes:

*   Pie Charts
*   Column Charts
*   Multi-series Column Charts
*   Bar Charts
*   Multi-series Bar Charts
*   Line Charts
*   Multi-series Line Charts

Extra Charts
------------

There are currently no additional chart types included with the google charts
renderer, although support for table charts and geo charts is planned.

Prerequisites
-------------

To use the google charts renderer, you must import the google javascript api by
including the following html in your page:

.. code-block:: html

    <script type="text/javascript" src="https://www.google.com/jsapi"></script>

Renderer Options
----------------

The ``renderer_options`` dictionary for charts using the google charts renderer
is simply JSON encoded and passed directly into the chart initialization javascript.
You therefore have full control over any parameter defined in the Google Chart Tools
documentation:

*   `Google Chart Tools Pie Chart Documentation <https://google-developers.appspot.com/chart/interactive/docs/gallery/piechart>`_
*   `Google Chart Tools Column Chart Documentation <https://google-developers.appspot.com/chart/interactive/docs/gallery/columnchart>`_
*   `Google Chart Tools Bar Chart Documentation <https://google-developers.appspot.com/chart/interactive/docs/gallery/barchart>`_
*   `Google Chart Tools Line Chart Documentation <https://google-developers.appspot.com/chart/interactive/docs/gallery/linechart>`_

For example, if you want to create a stacked column chart
with no legend, a light grey background and red and blue columns, your chart definition
might look something like the following:

.. literalinclude:: googlecharts_renderer_example.py
    :language: python


Tips and Tricks
---------------

If you need to override the default html/javascript that the google renderer creates,
you can override the default templates at:

*   ``report_tools/renderers/googlecharts/barchart.html``
*   ``report_tools/renderers/googlecharts/columnchart.html``
*   ``report_tools/renderers/googlecharts/linechart.html``
*   ``report_tools/renderers/googlecharts/piechart.html``
