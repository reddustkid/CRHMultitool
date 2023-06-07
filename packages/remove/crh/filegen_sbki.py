import csv
import packages.filenames.sbki.filename as filename
from datetime import datetime
from pyutil import filereplace
import codecs
import os
import uuid



def main(project,trailer,opcode,actvolume,actreason):

    with open("input/crhannulmentsbki.csv", encoding='utf8', newline = '') as csvfile:
        recnumber = 1
        posnum = uuid.uuid4().hex
        source_inn_id = ["","","",""]
        source_ogrn_id = ["","","",""]
        reader = csv.DictReader(csvfile,delimiter="*")
        csv_filename = "output/"+ filename.verasergeevna(project,posnum)
        with open (csv_filename, 'a',encoding='utf8', newline = '') as csvfile:
            xml     = '<?xml version="1.0" encoding="utf-8"?>'
            fch     = '<fch version="4.0" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            head        = '\t' + '<head>'
            source_inn      = '\t\t' + '<source_inn>' + str(source_inn_id[project]) + '</source_inn>'
            source_ogrn     = '\t\t' + '<source_ogrn>' + str(source_ogrn_id[project]) + '</source_ogrn>'
            date            = '\t\t' + '<date>' + datetime.today().strftime('%d.%m.%Y') +'</date>'
            file_reg_date   = '\t\t' + '<file_reg_date>' + datetime.today().strftime('%d.%m.%Y') +'</file_reg_date>'
            file_reg_num    = '\t\t' + '<file_reg_num>' + str(posnum) + '</file_reg_num>'
            headc       = '\t' + '</head>'
            
            writer = csv.writer(csvfile,quotechar="\'")    
            writer.writerow([xml])
            writer.writerow([fch])
            writer.writerow([head])
            writer.writerow([source_inn])
            writer.writerow([source_ogrn])
            writer.writerow([date])
            writer.writerow([file_reg_date])
            writer.writerow([file_reg_num])
            writer.writerow([headc])
            
        for row in reader:
            infoc   = '\t' + '</info>'
            info    = '\t' + '<info recnumber="'+ str(recnumber) + '" action="' + str(opcode) + '" action_volume="' + str(actvolume) + '"' + ' action_reason="' + str(actreason) + '">'
            infoan    = '\t' + '<info recnumber="'+ str(recnumber) + '" action="C"'+ ' action_volume="3" comment="{&quot;contract_no&quot;:&quot;' + row['ContractNumber'] + '&quot;,&quot;contract_date&quot;:&quot;' + row['DateCreated'] + '&quot;,&quot;contract_type&quot;:&quot;19&quot;}"' + '>'
            title_part  = '\t\t' + '<title_part>'
            private         = '\t\t\t' + '<private>'
            name                = '\t\t\t\t' + '<name>'
            lastname                = '\t\t\t\t\t' + '<last>' + row['LastName'] + '</last>'
            firstname               = '\t\t\t\t\t' + '<first>' + row['FirstName'] + '</first>'
            middlename              = '\t\t\t\t\t' + '<middle>' + row['FatherName'] + '</middle>'
            namec               = '\t\t\t\t' + '</name>'
            doc                 = '\t\t\t\t' + '<doc>'
            country                 = '\t\t\t\t\t' + '<country>643</country>'
            type                    = '\t\t\t\t\t' + '<type>21</type>'   
            pserial                 = '\t\t\t\t\t' + '<serial>' + row['PSeries'] + '</serial>'
            pnumber                 = '\t\t\t\t\t' + '<number>' + row['PNumber'] + '</number>'
            pdate                   = '\t\t\t\t\t' + '<date>' + row['DocDate'] + '</date>'
            ppwho                   = '\t\t\t\t\t' + '<who>' + row['DocPlace'] + '</who>'
            department_code         = '\t\t\t\t\t' + '<department_code>' + row['DocPlaceCode'] + '</department_code>'
            docc                = '\t\t\t\t' + '</doc>'
            birth               = '\t\t\t\t' + '<birth>'
            birthdate               = '\t\t\t\t\t' + '<date>' + row['Birthday'] + '</date>'
            birthcountry            = '\t\t\t\t\t' + '<country>999</country>'
            birthplace              = '\t\t\t\t\t' + '<place>' + row['BirthPlace'] + '</place>'
            birthc              = '\t\t\t\t' + '</birth>'
            history             = '\t\t\t\t' + '<history>'
            historyname             = '\t\t\t\t\t' + '<name>'
            hist_name_sign                 = '\t\t\t\t\t\t' + '<hist_name_sign>0</hist_name_sign>'
            historynamec            = '\t\t\t\t\t' + '</name>'
            historydoc              = '\t\t\t\t\t' + '<doc>'
            hist_doc_sign                  = '\t\t\t\t\t\t' + '<hist_doc_sign>0</hist_doc_sign>'
            historydocc              = '\t\t\t\t\t' + '</doc>'
            historyc            = '\t\t\t\t' + '</history>'
            inn                 = '\t\t\t\t' + '<inn>'
            inncode                 = '\t\t\t\t\t' + '<code>1</code>'
            innno                   = '\t\t\t\t\t' + '<no>' + row['Inn'] + '</no>'
            innc                = '\t\t\t\t' + '</inn>'
            snils               = '\t\t\t\t' + '<snils>'
            snilsno                 = '\t\t\t\t\t' + '<no>' + row['Snils'] + '</no>'
            snilsc              = '\t\t\t\t' + '</snils>'
            privatec        = '\t\t\t' + '</private>'
            title_partc = '\t\t' + '</title_part>'
            uid         = '\t\t' + '<uid>'
            uidid           = '\t\t\t' + '<id>' + row['Uid'] + '</id>'
            uidc        = '\t\t' + '</uid>'
            with open (csv_filename, 'a',encoding='utf8', newline = '') as csvfile:
                writer = csv.writer(csvfile,quotechar="\'")
                if uidid == '			<id></id>':
                    print('MISS: ' + row['ClientId']+ ' has no uid')
                    writer.writerow([infoan])
                else:
                    writer.writerow([info])
                writer.writerow([title_part])
                writer.writerow([private])
                writer.writerow([name])
                writer.writerow([lastname])
                writer.writerow([firstname])
                if middlename == '				<middlename></middlename>':
                    print('MISS: ' + row['ClientId']+ ' has no middlename')
                else:
                    writer.writerow([middlename])
                writer.writerow([namec])
                writer.writerow([doc])
                writer.writerow([country])
                writer.writerow([type])
                writer.writerow([pserial])
                writer.writerow([pnumber])
                writer.writerow([pdate])
                writer.writerow([ppwho])
                writer.writerow([department_code])
                writer.writerow([docc])
                writer.writerow([birth])
                writer.writerow([birthdate])
                writer.writerow([birthcountry])
                writer.writerow([birthplace])
                writer.writerow([birthc])
                writer.writerow([history])
                writer.writerow([historyname])
                writer.writerow([hist_name_sign])
                writer.writerow([historynamec])
                writer.writerow([historydoc])
                writer.writerow([hist_doc_sign])
                writer.writerow([historydocc])
                writer.writerow([historyc])
                if innno == '					<no></no>':
                    print('MISS: ' + row['ClientId']+ ' has no inn')
                else:
                    writer.writerow([inn])
                    writer.writerow([inncode])
                    writer.writerow([innno])
                    writer.writerow([innc])
                if snilsno == '					<no></no>':
                    print('MISS: ' + row['ClientId']+' has no snils')
                else:
                    writer.writerow([snils])
                    writer.writerow([snilsno])
                    writer.writerow([snilsc])
                writer.writerow([privatec])
                writer.writerow([title_partc])
                if uidid == '			<id></id>':
                    pass
                else:
                    writer.writerow([uid])
                    writer.writerow([uidid])
                    writer.writerow([uidc])
                writer.writerow([infoc])
            recnumber +=1        
        with open (csv_filename, 'a',encoding='utf8', newline = '') as csvfile:
            reader = csv.DictReader(csvfile,delimiter="*")
            footer    = '\t' + '<footer>'
            subjects_count  = '\t\t' + '<subjects_count>' + str(trailer) + '</subjects_count>'
            records_count  = '\t\t' + '<records_count>' + str(recnumber-1) + '</records_count>'
            footerc   = '\t' + '</footer>'
            fchc      = '</fch>'
            writer = csv.writer(csvfile,quotechar="\'")
            writer.writerow([footer])
            writer.writerow([subjects_count])
            writer.writerow([records_count])
            writer.writerow([footerc])
            writer.writerow([fchc])
    with codecs.open (csv_filename, 'r', 'utf_8_sig') as f, codecs.open (csv_filename+'.xml', 'w','utf_8_sig') as fo:
        for line in f:
            fo.write(line.replace("'",''))
        f.close()
    os.remove(csv_filename)
    print('INFO: Done | File generated at '+ csv_filename)
            
if __name__ == "__main__":
    print('INIT: writeoff_filegenerator')
