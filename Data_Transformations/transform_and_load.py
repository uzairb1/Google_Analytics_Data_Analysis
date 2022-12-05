from os import walk
from execute_query import execute_query
from data_load import upload


"""
This is the main file of this folder
Imports the other 2 Python files of this Folder, and the executes the transformations 
by reading the queries folder
"""

f = []
for (dirpath, dirnames, filenames) in walk('Data_Transformations/Queries'):
    f.extend(filenames)
    break
for name in f:
    print(name)
    file = name.split('.')[0] #get the file name without file extension
    execute_query(file)
    upload(file)
