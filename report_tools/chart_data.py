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
    
    def add_column(self, name, metadata=None):
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
        if len(data) < len(self.columns):
            raise ChartDataError("Not enough data points (%s) for the given number of columns (%s)" % (len(data), len(self.columns)))

        if len(data) > len(self.columns):
            raise ChartDataError("Too many data points (%s) for the given number of columns (%s)" % (len(data), len(self.columns)))
        
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
