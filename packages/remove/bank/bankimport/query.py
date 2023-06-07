# import pytest
import pyodbc
import pandas as pd
import packages.remove.bank.bankimport.filegen_sbki as filegen_sbki
import packages.remove.bank.bankimport.filegen_nbki as filegen_nbki
import warnings
import datetime as dt



#Заголовок создается отдельно чтобы можно было построчно записывать датафрейм
def header(conn,number,file):
    sql = '''
    
    '''
    a = 'a'
    numberlisted = [str(number)]
    sql = sql.format('?',','.join('?'*len(a)))
    query = pd.read_sql_query(sql, conn, params=numberlisted)
    df = pd.DataFrame(query)
    df.to_csv(file, index = False, mode = 'w', sep='*', header= True)
    print('INFO: Csv header created')

#Записываем полученный запрос в датафрейм и сохраняем построчно 
def writer(dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,query,file):
	df = pd.DataFrame(query)
	if pd.isnull(df.loc[0, 'islt']):
		pass
	else:
		dfLt.extend(df['contractnumber'].tolist())
	if df.empty:
		dfEmpty.append(str(dfImport_splitted))
	else:
		df.to_csv(file, index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(dfImport_splitted))
		dfTrailer.extend(df['clientid'].tolist())

# Получаем запрос с лайном базы и отправляем его на запись writer
def lime(conn,dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,file):
	sql = '''
    
    '''
	a = 'a'
	numberlisted = [str(dfImport_splitted)]
	sql = sql.format('?',','.join('?'*len(a))) #Костыль, пока хз как исправить
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	writer(dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,query,file)

def konga(conn,dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,file):
	sql = '''

    '''
	a = 'a'
	numberlisted = [str(dfImport_splitted)]
	sql = sql.format('?',','.join('?'*len(a))) 
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	writer(dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,query,file)
			
def mango(conn,dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,file):
	sql = '''
    
    '''
    a = 'a'
	numberlisted = [str(dfImport_splitted)]
	sql = sql.format('?',','.join('?'*len(a))) 
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	df = pd.DataFrame(query)
	writer(dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,query,file)
		
def limecess(conn,dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,file):
	sql = '''
    '''
	a = 'a'
	numberlisted = [str(dfImport_splitted)]
	sql = sql.format('?',','.join('?'*len(a))) 
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	df = pd.DataFrame(query)
	writer(dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,query,file)
          
def main(project):
	dfImport = pd.read_excel('bankimport' + '.xlsx', dtype='object')
	dfImport['bankdate'] = dfImport['bankdate'].dt.strftime('%d.%m.%Y')
	file = 'input/bankimport.csv'
	dfLt		= []
	dfExists    = []
	dfEmpty     = []
	dfTrailer   = []
	dfImport_list = dfImport.values.tolist()

	print('INFO: List passed to sql query: ' + str(dfImport_list))
	if project == 0: #Lime
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(dfImport_list):
            #Номера договоров посылаются поочередно через цикл
			# и чтобы на каждый из них не создавался заголовок посылается первым пустое значение у которого тег header=True, сами договора уже генерятся без него
			dfImport_splitted = dfImport_list[i][0]
			pass
			if i == 0:
				print('INFO: Header init')
				header(conn,0,file) 
			lime(conn,dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,file)
           
	elif project == 1: #Konga
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(dfImport):
			dfImport_splitted = dfImport_list[i][0]
			if i == 0:
				print('INFO: Header init')
				header(conn,0,file)
			konga(conn,dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,file)
			
	elif project == 2: #Mango
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(dfImport):
			dfImport_splitted = dfImport_list[i][0]
			if i == 0:
				print('INFO: Header init')
				header(conn,0,file)
			mango(conn,dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,file)
			
	elif project == 3: #Limecess
		conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=;'
                              'Database=;'
                              'Trusted_Connection=yes;')
		for i, number in enumerate(dfImport):
			dfImport_splitted = dfImport_list[i][0]
			if i == 0:
				print('INFO: Header init')
				header(conn,0,file)
			limecess(conn,dfImport_splitted,dfExists,dfEmpty,dfLt,dfTrailer,file)

	dfbankparsinfo = pd.read_csv(file, sep='*', dtype='object')
	dfbankparsinfo = pd.merge(dfbankparsinfo, dfImport, left_on='contractnumber', right_on='contractnumber', how='left')
	dfbankparsinfo.to_csv(file, index = False, mode = 'w', sep='*', header= True) 
	print('INFO: DataFrame returned successfully on contract numbers: ' + str(dfExists))
	print('INFO: DataFrame returned empty on contract numbers: ' + str(dfEmpty))
	print('INFO: Количество договоров ДЗ: ' + str(len(dfLt)) + str(dfLt))
	trailer = len(set(dfTrailer))
	filegen_nbki.main(project,trailer)
	filegen_sbki.main(project,trailer)

if __name__ == "__main__":
    main()