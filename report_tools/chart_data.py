from copy import copy



class ChartDataError(Exception):
    pass


class ChartDataColumn(object):
    def __init__(self, name, metadata=None):
        self.name = copy(name)

        if metadata is not None:
            self.metadata = copy(metadata)
        else:
            self.metadata = {}
        
    def get_metadata(self):
        return self.metadata
    
    def get_metadata_item(self, key):
        return self.metadata.get(key, None)


class ChartDataRow(object):
    def __init__(self, data, metadata=None):
        self.cells = []

        for datum in data:
            if type(datum) != ChartDataCell:
                if type(datum) in (list, tuple):
                    datum = ChartDataCell(datum[0], datum[1])
                else:
                    datum = ChartDataCell(datum)
            
            self.cells.append(datum)
        
        if metadata is not None:
            self.metadata = copy(metadata)
        else:
            self.metadata = {}
    
    def __iter__(self):
        for cell in self.cells:
            yield cell
            
    def __getitem__(self, index):
        return self.cells[index]

    def delete_cell(self, cell_index):
        try:
            self.cells.pop(cell_index)
        except IndexError:
            pass

        return

    def to_list(self):
        return [cell.data for cell in self.cells]


class ChartDataCell(object):
    def __init__(self, data, metadata=None):
        self.data = copy(data)

        if metadata is not None:
            self.metadata = copy(metadata)
        else:
            self.metadata = {}


class ChartData(object):
    
    def __init__(self):
        self.columns = []
        self.rows = []
    
    def get_columns(self):
        return self.columns
    
    def get_rows(self):
        return self.rows
    
    def add_column(self, name="", metadata=None):
        if self.rows:
            raise ChartDataError("Cannot add columns after data has been entered")
        
        column = ChartDataColumn(name, metadata)
        self.columns.append(column)
    
    def add_columns(self, columns):
        for column in columns:
            if type(column) in (list, tuple):
                name = column[0]
                metadata = column[1]
            else:
                name = column
                metadata = {}
                
            self.add_column(name, metadata)
    
    def add_row(self, data, metadata=None):
        # Raise an error if the row is too short
        if len(data) < len(self.columns):
            raise ChartDataError("Not enough data points (%s) for the given number of columns (%s)" % (len(data), len(self.columns)))

        # If the row is too short..
        if len(data) > len(self.columns):
            # Raise an error if they've defined columns
            if self.columns:
                raise ChartDataError("Too many data points (%s) for the given number of columns (%s)" % (len(data), len(self.columns)))

            # If they haven't defined any columns, assume that they don't need them, but add in some blank
            # ones to keep things tidy.
            else:
                num_extra_columns_required = len(data) - len(self.columns)
                
                for i in range(num_extra_columns_required):
                    self.add_column()
        
        row = ChartDataRow(data, metadata)
        self.rows.append(row)

    def add_rows(self, rows):
        for row in rows:
            if type(row) in (list, tuple):
                data = row[0]
                metadata = row[1]
            else:
                data = row
                metadata = {}
            
            self.add_row(data, metadata)

    def delete_column(self, column_index):
        try:
            self.columns.pop(column_index)
        except IndexError:
            pass

        for row in self.rows:
            try:
                row.delete_cell(column_index)
            except IndexError:
                pass

    def to_list(self):
        return [row.to_list() for row in self.get_rows()]

    def to_list_transposed(self):
        """
        Returns the list version of the chart data flipped on the main diagonal
        """
        original = self.to_list()
        return zip(*original)
