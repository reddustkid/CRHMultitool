import csv
import packages.filenames.nbki.filename as filename
from datetime import datetime, timedelta
from pyutil import filereplace


def main(project):
    date = datetime.now() + timedelta(hours=0)
    with open("input/"+"calluidremove.csv", encoding='utf8', newline = '') as csvfile:
        reader = csv.DictReader(csvfile,delimiter="*")
        counter = 1
        csv_filename = "output/"+ filename.project_datetime(project)
        with open (csv_filename, 'w',encoding='cp1251', newline = '') as csvfile:
            writer = csv.writer(csvfile,quotechar="\'")
            header = filename.call_uid(project)
            writer.writerow([header])
        
        for row in reader:

            groupheader = '0_GROUPHEADER\t' +  str(counter) + '\t' + '1.1\t' + 'D\t' + '{ '+'"'+'annul_reason'+'"'+' : '+'"'+'3'+'"'+' }\t' + date.strftime("%d.%m.%Y")
            counter += 1
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
            application = 'C55_APPLICATION\t' + '1\t' + row['RequestedAmount'] + '0' + '\t' + 'RUB\t' + row['Uid'] + '\t' + row['RequestedPeriod'] +  '\t' + '2\t' + '2\t' + '31.12.9999'
            with open (csv_filename, 'a',encoding='cp1251', newline = '') as csvfile:
                writer = csv.writer(csvfile,quotechar="\'")
                writer.writerow([groupheader])
                writer.writerow([name])
                writer.writerow([prevname])
                writer.writerow([birth])
                writer.writerow([passport])
                writer.writerow([previd])
                writer.writerow([regnum])
                writer.writerow([snils])
                writer.writerow([delete])
                writer.writerow([application])
        with open (csv_filename, 'a',encoding='cp1251', newline = '') as csvfile:
            writer = csv.writer(csvfile,quotechar="\'")
            trailer = 'TRAILER\t' + row['TrailerCount'] + '\t' + str(counter-1)
            writer.writerow([trailer])
        print('INFO: Done. File created at: ' + csv_filename)
        
            
if __name__ == "__main__":
    print('done')