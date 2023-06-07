# import pytest
import pyodbc
import pandas as pd
import tkinter as tk
import packages.remove.crh.filegen_nbki as filegen_nbki
import warnings


def header(conn,number):
    sql = '''
    code goes here
    '''
    a = 'a'
    numberlisted = [str(number)]
    sql = sql.format('?',','.join('?'*len(a)))
    query = pd.read_sql_query(sql, conn, params=numberlisted)
    df = pd.DataFrame(query)
    df.to_csv('input/newcrhremovenbki.csv', index = False, mode = 'w', sep='*', header= True)
    print('INFO: Csv header created')

def prolongs(conn,number,prolongExists,prolongEmpty):
	sql = '''
    code goes here
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
    code goes here
    '''
	a = 'a'
	numberlisted = [str(number)]
	sql = sql.format('?',','.join('?'*len(a)))
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	df = pd.DataFrame(query)
	if df.empty:
		dfEmpty.append(str(number))
	else:
		df.to_csv('input/newcrhremovenbki.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['ClientId'].tolist())

def konga(conn,number,dfExists,dfEmpty,dfTrailer):
	sql = '''
    code goes here
    '''
	a = 'a'
	numberlisted = [str(number)]
	sql = sql.format('?',','.join('?'*len(a))) 
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	df = pd.DataFrame(query)
	if df.empty:
		dfEmpty.append(str(number))
	else:
		df.to_csv('input/newcrhremovenbki.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['ClientId'].tolist())
			
def mango(conn,number,dfExists,dfEmpty,dfTrailer):
	sql = '''
    code goes here
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
		df.to_csv('input/newcrhremovenbki.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['ClientId'].tolist())
		#print ('INFO: Client info for contract number ' + str(number) + ' on Konga created')
		
def limecess(conn,number,dfExists,dfEmpty,dfTrailer):
	sql = '''
    code goes here
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
		df.to_csv('input/newcrhremovenbki.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['ClientId'].tolist())
		#print ('INFO: Client info for contract number ' + str(number) + ' on Lime created')
          
def main(conumbers,project,opcode,actreason):
	
	conumbers_splitted = list(filter(None, conumbers.split("\n")))
	print('INFO: List passed to sql query: ' + str(conumbers_splitted))
	# prolongExists = []
	# prolongEmpty = []
	dfExists    = []
	dfEmpty     = []
	dfTrailer   = []
	if project == 0:
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
			#print('INFO: Lime writeoff init for contract number: ' + str(number))
			lime(conn,number,dfExists,dfEmpty,dfTrailer)
            #Продления генерируются в папку input/prolongs + номер договора т.к. продлений может быть несколько и они не помещаются в одну строку.
			# prolongs(conn,number,prolongExists,prolongEmpty)
            
	elif project == 1:
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(conumbers_splitted):
			if i == 0:
				print('INFO: Header init')
				header(conn,0)
			#print('INFO: Konga writeoff init for contract number: ' + str(number))
			konga(conn,number,dfExists,dfEmpty,dfTrailer)
			# prolongs(conn,number,prolongExists,prolongEmpty)
	elif project == 2:
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(conumbers_splitted):
			if i == 0:
				print('INFO: Header init')
				header(conn,0)
			#print('INFO: Konga writeoff init for contract number: ' + str(number))
			mango(conn,number,dfExists,dfEmpty,dfTrailer)
			# prolongs(conn,number,prolongExists,prolongEmpty)
	elif project == 3:
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(conumbers_splitted):
			if i == 0:
				print('INFO: Header init')
				header(conn,0)
			#print('INFO: Konga writeoff init for contract number: ' + str(number))
			limecess(conn,number,dfExists,dfEmpty,dfTrailer)
			# prolongs(conn,number,prolongExists,prolongEmpty)
	print('INFO: DataFrame returned successfully on contract numbers: ' + str(dfExists))
	# print('INFO: Contract numbers with prolongs: ' + str(prolongExists))
	print('INFO: DataFrame returned empty on contract numbers: ' + str(dfEmpty))
    # print('INFO: Contract numbers without prolongs: ' + str(prolongEmpty))

	trailer = len(set(dfTrailer))
	print(trailer)
	filegen_nbki.main(project,trailer,opcode,actreason)
if __name__ == "__main__":
    main()