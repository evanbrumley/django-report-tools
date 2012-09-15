.. wsp-reports documentation master file, created by
   sphinx-quickstart on Thu Jan 12 14:58:42 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Django Report Tools
===================

Report tools aims to take the pain out of putting charts, graphs and tables into
your Django projects. Feature include:

* Define reports and charts the same way you would Django forms/models and fields
* Use 'renderers' to avoid the hassle of dealing with various
  charting technologies
* Use bundled renderers for Google Chart Tools and jqPlot
* Enter chart data in a standardised format
* Build a simple API, allowing for the creation of chart exports or a 'save to dashboard'
  feature.

An example report:

.. literalinclude:: example.py
   :language: python

For an expanation of this code, read on to the :doc:`getting started </getting_started/index>` section.

Contents
--------

.. toctree::
   :maxdepth: 2

   getting_started/index
   charts/index
   renderers/index
   chart_data/index
   api/index

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

