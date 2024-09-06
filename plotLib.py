import pandas as pd

class data:
    """ python class to load data from table files """

    def __init__(self,dirs):
        self.dirs = dirs
    
    def loadData(self, file, delim):
        """ loads data into pandas DataFrame """

        self.tables = {}
        i = 0
        for dir in self.dirs:
            self.tables[i] = pd.read_table(dir+file,delimiter=delim)
            i += 1

    def selectData(self, col, arg, sort):
        """ selects data based on values in a specified column,
         if arg is None, only select column"""

        for i in range(0,self.tables.__len__()):
            if arg == None:
                self.tables[i] = self.tables[i][col].sort_values()
            else:
                self.tables[i] = self.tables[i].loc[self.tables[i][col] == arg].sort_values(by=[sort])

    def assignValues(self, varList):
        """ assigns values into lists in a dictionary """

        values = {}
        for i in range(0,self.tables.__len__()):
            vars = []
            for var in varList:
                vars.append(self.tables[i][var])
            values[i] = vars
        return values