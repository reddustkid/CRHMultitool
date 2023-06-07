import csv
import packages.filenames.nbki.filename as filename
from pyutil import filereplace


def main(project,trailer,opcode,actreason):
    with open("input/"+"newcrhremovenbki.csv", encoding='utf8', newline = '') as csvfile:
        reader = csv.DictReader(csvfile,delimiter="*")
        recnumber = 1
        csv_filename = "output/"+ filename.project_datetime(project)
        with open (csv_filename, 'w',encoding='cp1251', newline = '') as csvfile:
            writer = csv.writer(csvfile,quotechar="\'")
            header = filename.call_uid(project)
            writer.writerow([header])
        
        for row in reader:

            #header = filename.call_uid(project)
            groupheader = '0_GROUPHEADER\t' +  str(recnumber) + '\t' + '\t' + str(opcode) + '\t' + '{ '+'"'+'annul_reason'+'"'+' : '+'"'+ str(actreason) +'"'+' }\t' + row['ActualDate']
            recnumber += 1
            name = 'C1_NAME\t' + row['LastName'] + '\t' + row['FirstName'] + '\t' + row['FatherName']
            prevname = 'C2_PREVNAME\t' + '0\t' + '\t' + '\t' + '\t'
            birth = 'C3_BIRTH\t' + row['BirthDate'] + '\t' + '999\t' + row['BirthPlace']
            passport = 'C4_ID\t' + '643\t\t' + '21\t\t' + row['Series'] +'\t' + row['Number'] + '\t' + row['IssuedOn'] + '\t' + row['IssuedBy'] +'\t' + row['Code'] +'\t'
            
            previd = 'C5_PREVID\t' + '0\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + '\t'
            regnum = 'C6_REGNUM\t' + '1\t' + row['InnOrFnsInn'] +'\t'
            if regnum == 'C6_REGNUM	1		':
                regnum = 'C6_REGNUM\t\t\t'
            snils = 'C7_SNILS\t' + row['SNILS']
            delete = 'DELETE'
            uid = 'C17_UID\t' + row['Uid']
            application = 'C55_APPLICATION\t' + '1\t' + row['RequestedAmount'] + '0' + '\t' + 'RUB\t' + row['Uid'] + '\t' + row['ApplicationDate'] +  '\t' + '2\t' + '2\t' + row['ApprovalExpireDate']
            obligparttake = 'C56_OBLIGPARTTAKE\t' + '1\t3\t' + row['Uid'] + '\t' + row['FundDate'] + '\t' + row['PastDue90'] + '\t' + row['LoanIndicator']

            with open (csv_filename, 'a',encoding='cp1251', newline = '') as csvfile:
               #writer = csv.writer(csvfile,quotechar="\'", quoting=csv.QUOTE_NONE, escapechar='\\')
                writer = csv.writer(csvfile,quotechar="\'")
               #writer.writerow([header])
                writer.writerow([groupheader])
                writer.writerow([name])
                writer.writerow([prevname])
                writer.writerow([birth])
                writer.writerow([passport])
                writer.writerow([previd])
                writer.writerow([regnum])
                writer.writerow([snils])
                writer.writerow([delete])
                writer.writerow([uid])
                writer.writerow([application])
                writer.writerow([obligparttake])
        with open (csv_filename, 'a',encoding='cp1251', newline = '') as csvfile:
            writer = csv.writer(csvfile,quotechar="\'")
            trailerr = 'TRAILER\t' + str(trailer) + '\t' + str(recnumber-1)
            # trailer = 'TRAILER\t' + row['TrailerCount'] + '\t' + str(recnumber-1)
            writer.writerow([trailerr])
        filereplace(csv_filename,"0.00\t","0,00\t") #заменяет точку в дробях на запятую
        filereplace(csv_filename,"'","")  #убирает кавычки
        print('INFO: Done. File created at: ' + csv_filename)
        
            
if __name__ == "__main__":
    print('done')