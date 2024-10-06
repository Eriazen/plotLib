from __future__ import annotations
import pandas as pd

class data:
    """ python class to load data from table files """

    def __init__(self, dirs: str) -> data:
        self.dirs = dirs
        self.tables = []
    
    def loadData(self, file: str, delim: str) -> None:
        """ loads data into pandas DataFrame """

        for dir in self.dirs:
            self.tables.append(pd.read_table(dir+file,delimiter=delim))

    def selectData(self, col: str, sort: str, argList: list) -> None:
        """ selects data based on values in a specified column,
         \nif arg isn't specified, only select column """

        for id, tbl in enumerate(self.tables):
            if argList == None:
                self.tables[id] = tbl[col].sort_values()
            else:
                self.tables[id] = tbl.loc[tbl[col] == argList[id]].sort_values(by=sort)

    def assignValues(self, varList: list) -> list:
        """ assigns values into lists in a list """

        values = []

        for tbl in self.tables:
            vars = []
            for var in varList:
                vars.append(tbl[var])
            values.append(vars)

        return values