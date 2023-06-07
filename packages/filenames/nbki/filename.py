from datetime import datetime, timedelta



def call(project):
    date = datetime.now() + timedelta(hours=0)
    return "" + short_project[project] + '_' + date.strftime("%Y.%m.%d.")

def call_nouid(project):
    date = datetime.now() + timedelta(hours=0)
    return "" + short_project[project] + '_' + date.strftime("%Y.%m.%d.")

def call_uid(project):
    date = datetime.now() + timedelta(hours=0)
    projectINN = ["","",""]
    projectOGRN = ["","",""]
    projectPass = ["","",""]
    return 'HEADER\t' + projectINN[project] +'\t' + projectOGRN[project] + '\t' + project_datetime(project) + '\t' + date.strftime("%d.%m.%Y") +'\t\t' +  long_project[project] + '\t' + projectPass[project] + '\t' + '4.0\t'

def project_datetime(project):
    date = datetime.now() + timedelta(hours=0)
    return long_project[project] + '_' + date.strftime("%Y%m%d_%H%M%S")

def crh(project):
    date = datetime.now() + timedelta(hours=0)
    return "ReportRemoveKI_" + long_project[project] + '_' + date.strftime("%Y%m%d_%H%M%S")


long_project = ["","","",""]
short_project = ["","","",""]
      


if __name__ == "__main__":
    print(project_datetime())
