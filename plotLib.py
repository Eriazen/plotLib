#!/usr/bin/python3

import pandas as pd

class data:
    """ python class to load data from table files """

    def __init__(self,dirs):
        self.dirs = dirs
    
    def loadData(self, file, delim):
        """ loads data into pandas DataFrame """

        self.df = pd.read_table(self.dirs+file,delimiter=delim)

    def selectData(self, col, arg):
        """ selects data based on values in a specified column,
         if arg is None, only select column"""

        if arg == None:
            return self.df[col]

        return self.df.loc[self.df[col] == arg]