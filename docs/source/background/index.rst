Background
==========

When creating data driven web applications, the following is a relatively common site structure:

    .. image:: data_driven_site.png

In this sort of layout, the data management pages provide all your basic CRUD, the results
of which are passed into several reporting views. These views typically contain a series of charts
and tables, giving an analysis of the data entered. The dashboard view then allows users to pick
various charts and tables from the reporting views and keep them on a customised home page.

The goal of the Report Tools package is to make the creation of the reporting views and dashboard
as easy and clean as possible. Without such a package, a simple reporting view might look like this:

.. literalinclude:: simple_reporting_view.py
    :language: python

.. literalinclude:: simple_reporting_view_template.html
    :language: django

This code has some problems:

* Even after abstracting out a lot of the hard lifting, there's going to be a lot of code in your
  view, some of it quite repetitive.
* There's no easy way to lift out individual charts for your dashboard - you'll have to repeat
  code somewhere else to get that to work.
* Charts can't share calculations between each other in a clean way unless you de-abstract and make
  your view even longer.
* The formats generated/required by ``gather_chart1_data`` and ``chart1_options`` are probably
  going to be heavily tied to the charting package you use.
* ``generate_chart_html`` is going to be a massive can of time-eating worms.

So, here's how you'd write a similar view with Report Tools:

.. literalinclude:: better_reporting_view.py
    :language: python

.. literalinclude:: better_reporting_view_template.html
    :language: django

So you now have the following advantages:

* Your view code is a lot shorter and more manageable
* Options for your charts can be entered in a nice, declarative syntax
* Calculation results can be shared by storing them as instance variables
* Chart options and chart data are now entered in a standard format.
* What used to be a monolithic ``generate_chart_html`` function is now implemented
  as a renderer class. Report Tools currently provides an inbuilt renderer for the
  Google Visualization Toolkit, and it's easy to write your own.
* Because the entire report is stored in its own highly structured class,
  ripping an individual chart out for a dashboard is a lot easier. Report Tools
  even provides a class-based view expressly for this purpose. See the API generation
  documentation for examples.

This gives you a basic overview of why Report Tools exists - to learn about how it works and how
to use it properly, move on to the :doc:`Getting Started </getting_started/index>` section.
