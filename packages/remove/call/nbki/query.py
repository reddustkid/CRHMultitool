# import pytest
import pyodbc 
import pandas as pd
import tkinter as tk


def main(clids,filename,project):
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

    clids_splitted = clids.split("\n")
    print("INFO: Call removal init on client id's: " + str(clids_splitted))
    if project == 0:
        sql = '''

            '''
    elif project == 1:
        sql = '''

            '''
    elif project == 2:
        sql = '''

            '''
    sql = sql.format('?',','.join('?'*len(clids_splitted)))
    #param=tuple((connection_line, conumbers_splitted))
    query = pd.read_sql_query(sql, conn, params=clids_splitted)
    print('INFO: SQL query executed. Loading into DataFrame')
    df = pd.DataFrame(query)
    if df.empty:
        print('MISS: DataFrame is empty!')
    else:
        print('INFO: DataFrame is loaded!')
    df.to_excel ('output/' + filename + '.xlsx', index = False)

    print('INFO: Done. File created at output/' + filename + '.xlsx')
if __name__ == "__main__":
    main()
