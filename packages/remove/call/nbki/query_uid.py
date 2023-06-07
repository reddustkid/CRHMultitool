# import pytest
import pyodbc 
import pandas as pd
import tkinter as tk
import packages.remove.call.nbki.uid_filegenerator as uid_filegenerator
import numpy as np


def main(clids,project):
    if project == 0:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
    else:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
    root = tk.Tk() # create main window
    root.withdraw() # hide main window 

    clids_splitted = list(filter(None, clids.split("\n")))
    print("INFO: Call removal init on client id's: " + str(clids_splitted))

    if project == 0: #lime
        sql = '''

            '''
    elif project == 1: #konga
        sql = '''

            '''
    elif project == 2: #mango
        sql = '''

            '''
    sql = sql.format('?',','.join('?'*len(clids_splitted)))
    query = pd.read_sql_query(sql, conn, params=clids_splitted*2)
    print('INFO: SQL query executed. Loading into DataFrame')
    df = pd.DataFrame(query)
    if df.empty:
        print('MISS: DataFrame is empty!')
    else:
        print('INFO: DataFrame is loaded!')
    df.to_csv ('input/calluidremove.csv', index = False, sep='*')
    print('INFO: Input file created at input/calluidremove.csv')
    print('INFO: Creating NBKI file')
    uid_filegenerator.main(project)

if __name__ == "__main__":
    main()
