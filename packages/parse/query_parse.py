import pyodbc
import packages.parse.web_parse as web_parse
import warnings
import pandas as pd

warnings.filterwarnings("ignore") #Предупреждение вылетает на запрос из-за старой версии библиотеки. А новая с последним патчем сломалась и не работает (Не подключается к БД)😵



def header(conn,number):
    sql = '''

    '''
    a = 'a'
    numberlisted = [str(number)]
    sql = sql.format('?',','.join('?'*len(a)))
    query = pd.read_sql_query(sql, conn, params=numberlisted)
    df = pd.DataFrame(query)
    df.to_csv('input/bankparsinfo.csv', index = False, mode = 'w', sep='*', header= True)
    print('INFO: Csv header created')

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
		df.to_csv('input/bankparsinfo.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['clientid'].tolist())

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
		df.to_csv('input/bankparsinfo.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['clientid'].tolist())
			
def mango(conn,number,dfExists,dfEmpty,dfTrailer):
	sql = '''

    '''
	a = 'a'
	numberlisted = [str(number)]
	sql = sql.format('?',','.join('?'*len(a))) #Костыль, пока хз как исправить
	query = pd.read_sql_query(sql, conn, params=numberlisted)
	df = pd.DataFrame(query)
	if df.empty:
		#print('MISS: Konga DataFrame on contract number ' + str(number) +' is empty!')
		dfEmpty.append(str(number))
	else:
		df.to_csv('input/bankparsinfo.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['clientid'].tolist())
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
		df.to_csv('input/bankparsinfo.csv', index = False, mode = 'a', sep='*', header= False)
		dfExists.append(str(number))
		dfTrailer.extend(df['clientid'].tolist())
		#print ('INFO: Client info for contract number ' + str(number) + ' on Lime created')
          
def main(conumbers,project):
	
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
	bank_buster = pd.read_csv('input/bankparsinfo.csv', sep='*', low_memory = True)
	bank_buster.reset_index(drop=True, inplace=True)

	print(bank_buster)
	for index, row in bank_buster.iterrows():
		bank_buster_list = bank_buster.loc[index, :].values.flatten().tolist()
		print(bank_buster_list)
	
	web_parse.browser_init(bank_buster)
if __name__ == "__main__":
    main()