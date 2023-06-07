# import pytest
import pyodbc
import pandas as pd
import tkinter as tk
import packages.remove.crh.filegen_sbki as filegen_sbki
import warnings




def header(conn,number):
    sql = '''
    '''
    a = 'a'
    numberlisted = [str(number)]
    sql = sql.format('?',','.join('?'*len(a)))
    query = pd.read_sql_query(sql, conn, params=numberlisted)
    df = pd.DataFrame(query)
    df.to_csv('input/crhannulmentsbki.csv', index = False, mode = 'w', sep='*', header= True)
    print('INFO: Csv header created')

def prolongs(conn,number,prolongExists,prolongEmpty):
	sql = '''
    '''
	a = 'a'
	numberlisted = [str(number)]
	sql = sql.format('?',','.join('?'*len(a)))
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	df = pd.DataFrame(query)
	if df.empty:
		prolongEmpty.append(str(number))
		#print('MISS: Prolongs DataFrame on contract number ' + str(number) +' is empty!')
	else:
		prolongExists.append(str(number))
		df.to_csv('input/prolongs/'+ str(number) + '.csv', index = False, mode = 'w', sep='*', header= True)
		#print('INFO: Prolongs for contract number(' + str(number) + ') created')

def lime(conn,number,dfExists,dfEmpty,dfTrailer):
	sql = '''
    '''
	a = 'a'
	numberlisted = [str(number)]
	sql = sql.format('?',','.join('?'*len(a)))
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	df = pd.DataFrame(query)
	if df.empty:
		dfEmpty.append(str(number))
	else:
		df.to_csv('input/crhannulmentsbki.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['ClientId'].tolist())

def konga(conn,number,dfExists,dfEmpty,dfTrailer):
	sql = '''
    '''
	a = 'a'
	numberlisted = [str(number)]
	sql = sql.format('?',','.join('?'*len(a))) #Костыль, пока хз как исправить
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	df = pd.DataFrame(query)
	if df.empty:
		dfEmpty.append(str(number))
	else:
		df.to_csv('input/crhannulmentsbki.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['ClientId'].tolist())
			
def mango(conn,number,dfExists,dfEmpty,dfTrailer):
	sql = '''
    '''
	a = 'a'
	numberlisted = [str(number)]
	sql = sql.format('?',','.join('?'*len(a)))
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	df = pd.DataFrame(query)
	if df.empty:
		#print('MISS: Konga DataFrame on contract number ' + str(number) +' is empty!')
		dfEmpty.append(str(number))
	else:
		df.to_csv('input/crhannulmentsbki.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['ClientId'].tolist())
		#print ('INFO: Client info for contract number ' + str(number) + ' on Konga created')
		
def limecess(conn,number,dfExists,dfEmpty,dfTrailer):
	sql = '''
    '''
	a = 'a'
	numberlisted = [str(number)]
	sql = sql.format('?',','.join('?'*len(a)))
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	df = pd.DataFrame(query)
	if df.empty:
		#print('MISS: Lime DataFrame on contract number ' + str(number) +' is empty!')
		dfEmpty.append(str(number))
	else:
		df.to_csv('input/crhannulmentsbki.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['ClientId'].tolist())
		#print ('INFO: Client info for contract number ' + str(number) + ' on Lime created')
          
def main(conumbers,project,opcode,actvolume,actreason):
	
	conumbers_splitted = list(filter(None, conumbers.split("\n")))
	print('INFO: List passed to sql query: ' + str(conumbers_splitted))
	dfExists    = []
	dfEmpty     = []
	dfTrailer   = []
	if project == 0: #Lime
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(conumbers_splitted):
            #Номера договоров посылаются поочередно через цикл
			# и чтобы на каждый из них не создавался заголовок посылается первым пустое значение у которого тег header=True, сами договора уже генерятся без него
			if i == 0:
				print('INFO: Header init')
				header(conn,0) 
			lime(conn,number,dfExists,dfEmpty,dfTrailer)

            
	elif project == 1: #Konga
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(conumbers_splitted):
			if i == 0:
				print('INFO: Header init')
				header(conn,0)
			konga(conn,number,dfExists,dfEmpty,dfTrailer)
			
	elif project == 2: #Mango
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(conumbers_splitted):
			if i == 0:
				print('INFO: Header init')
				header(conn,0)
			mango(conn,number,dfExists,dfEmpty,dfTrailer)
			
	elif project == 3: #Limecess
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(conumbers_splitted):
			if i == 0:
				print('INFO: Header init')
				header(conn,0)
			limecess(conn,number,dfExists,dfEmpty,dfTrailer)
			
	print('INFO: DataFrame returned successfully on contract numbers: ' + str(dfExists))
	print('INFO: DataFrame returned empty on contract numbers: ' + str(dfEmpty))
	trailer = len(set(dfTrailer))

	filegen_sbki.main(project,trailer,opcode,actvolume,actreason)

if __name__ == "__main__":
    main()