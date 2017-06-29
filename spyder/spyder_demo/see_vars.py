# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 09:06:55 2017

@author: paul
"""

#Go to View> Panes > Variables inspector to see all variables created below

myage = 22
mylist = [1,2,3]
mydict = {"name": "Paul", "age": 22}
myname = "Paul"

#Import a library, and give it an alias
import pandas as pd

#use the read_csv() function from that library to load a CSV file
#Note this needs to be in the same directory as this project
#Or we can describe a path, or URL
buslanefines = pd.read_csv("buslanefines.csv")

#Print the first few rows in the console to the right
buslanefines.head()

#Print information about the different fields
buslanefines.info()

#You can export using DataFrame.to_csv()
#File will appear in same directory
pd.DataFrame.to_csv(buslanefines,"busfinesexport.csv")
