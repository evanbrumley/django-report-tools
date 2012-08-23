Creating an API
===============

Sometimes it's not enough just to have your charts accessible within the context
of a larger report. Sometimes you need to pull them out, pass them around and so on.
The following steps should provide a good way to start off a more complex data reporting
system.


Step 1 - Use the class-based view
---------------------------------

The API relies on structured, class-based views to provide the hooks necessary to generate
the reports and charts. The following is an example:

.. literalinclude:: view.py
   :language: python

This is a really simple class-based view. It behaves in the same way as Django's base `View`
class, with the addition of a `get_report` method. This method provides the necessary hook
for the API to extract the report without touching your other view code.


Step 2 - Register the class-based view
--------------------------------------

To register the view with the api, simply pass it into the ``register`` function in the ``api``
module, along with the key you wish to use to access the report later:

.. literalinclude:: register.py
  :language: python


Step 3 (optional) - Add the API endpoints to your urls.py
---------------------------------------------------------

If you plan to make your chart HTML available externally, you can let the API handle your
URLS for you by adding the following line to your `urls.py`.

.. literalinclude:: urls.py
  :language: python


Access a chart internally
-------------------------

To access a chart from a registered report, simply use the ``report_tools.api.get_chart`` function.

    .. method:: report_tools.api.get_chart(request, api_key, chart_name, parameters=None, prefix=None)

        :param request: The current request
        :param api_key: The API key used to register the report view
        :param chart_name: The attribute name given to the required chart
        :param parameters: If provided, this dictionary will override the GET parameters
                           in the provided request.
        :param prefix: If provided, this string will be prepended to the chart's id. Useful
                       if you're displaying the same chart from the same report with different
                       parameters.
        :returns: The requested chart object


Access a chart externally
-------------------------

If you've added the API to your urls.py (step 3), you should be able to access a simple JSON endpoint at
``api/report_api_key/chart_name/``. The endpoint will provide the chart HTML along with a dictionary of
anything supplied in the chart's `attrs` parameter.
