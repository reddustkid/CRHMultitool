# import pytest
import pyodbc 
import pandas as pd
import tkinter as tk
import tkinter.simpledialog


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

    print(clids)
    clids_splitted = clids.split("\n")
    print(clids_splitted)

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
    query = pd.read_sql_query(sql, conn, params=clids_splitted)
    df = pd.DataFrame(query)
    df.to_excel ('output/' + filename+'.xlsx', index = False)
    print('INFO: Done. File created at: output/' + filename + '.xlsx')


if __name__ == "__main__":
    main()
