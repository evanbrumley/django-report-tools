Using ChartData to fill your charts
===================================

.. class:: report_tools.chart_data.ChartData

    The ChartData class provides a consistent way to get data into charts.
    Each ChartData object represents a 2 dimensional array of cells, which
    can be annotated on a column, row or cell level.

    .. method:: report_tools.chart_data.ChartData.add_column(self, name, metadata=None)

        Adds a new column to the data table.

        :param name: The name of the column
        :param metadata: A dictionary of metadata describing the column

    .. method:: report_tools.chart_data.ChartData.add_columns(self, columns)

        Adds multiple columns to the data table

        :param columns: A list of column names. If you need to enter metadata with the columns,
                        you can also pass in a list of name-metadata tuples.

    .. method:: report_tools.chart_data.add_row(self, data, metadata=None)

        Adds a new row to the datatable

        :param data: A list of data points that will form the row. The length of the list should
                     match the number of columns added.
        :param metadata: A dictionary of metadata describing the row

    .. method:: report_tools.chart_data.add_rows(self, rows)

        Adds multiple rows to the data table

        :param rows: A list of rows. If you need to enter metadata with the rows,
                     you can also pass in a list of row-metadata tuples.

    .. method:: get_columns(self)

        Returns a list of columns added so far

    ..method:: get_rows(self)

        Returns a list of rows added so far
