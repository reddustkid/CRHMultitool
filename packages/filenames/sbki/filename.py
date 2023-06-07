from datetime import datetime, timedelta
#import packages.filenames.nbkifilename as nbkifilename

def generate_name_sbki(posnum, project):
    date = datetime.now() + timedelta(hours=3)
    if project ==3:
        project = 0
    sbki_project = ["","",""]
    convTable = '0123456789ABCDEFGHIJKLMNOPQRSTUV' #Converting SBKI lats digits into x32
    return sbki_project[project] + "D" + convTable[int(date.year)-2000]+ convTable[date.month] + convTable[date.day] + convTable[posnum]
    
def verasergeevna(project,posnum):
    date = datetime.now() + timedelta(hours=3)
    if project == 3:
        project = 0
    sbki_project = ["","",""]
    return str(sbki_project[project]) + '_FCH_' + str(date.year) + f"{date.month:02d}" + f"{date.day:02d}" + '_' + str(posnum)

if __name__ == "__main__":
    print(generate_name_sbki())
