import tkinter as tk
from tkinter import *
import packages.filenames.nbki.filename as nbki_filename
import packages.remove.call.nbki.query as nbki_call_query
import packages.remove.call.nbki.query_uid as nbki_call_query_uid
import packages.remove.call.nbki.query_nouid as nbki_call_query_nouid

def call_remove(textbox_clids, project_type):
    project = int(project_type.get())
    clids = str(textbox_clids.get("1.0","end-1c"))
    filename = nbki_filename.call(project)
    nbki_call_query.main(clids,filename,project)

def call_nouid_remove(textbox_clids, project_type):
    project = int(project_type.get())
    clids = str(textbox_clids.get("1.0","end-1c"))
    filename = nbki_filename.call_nouid(project)
    nbki_call_query_nouid.main(clids,filename,project)    
    
def call_uid_remove(textbox_clids, project_type):
    project = int(project_type.get())
    clids = str(textbox_clids.get("1.0","end-1c"))
    nbki_call_query_uid.main(clids,project)
    
def main(main_frame):
    callremove_frame = tk.Frame(main_frame)
    project_type = StringVar(callremove_frame)
    
    lb = tk.Label(callremove_frame, text='Удаление запроса/заявки БКИ', font=('Bold', 14))
    lb.pack()

    frameClids = LabelFrame(main_frame, width=150, height=262, text="Client ID's")
    frameClids.pack()
    frameClids.place(x=15, y=50)
    
    textbox_clids=Text(frameClids,fg='blue',font=(16))
    textbox_clids.pack()
    textbox_clids.place(width=144,height=242)

    
    radio_project_type = {"Lime" : "0",
          "Konga" : "1",
          "Mango" : "2"}
    frame = LabelFrame(main_frame, width=100, height=200, text="Project")
    frame.pack()
    frame.place(x=200, y=50)

    for (text, radio_project_type) in radio_project_type.items():
        Radiobutton(frame, text = text, variable = project_type,
                value = radio_project_type, indicator = 0,
                background = "white", width = 20).pack(fill = X, ipady = 5, anchor=W)

    buttonCall=Button(main_frame, command=lambda: call_remove(textbox_clids, project_type), text='Запрос', fg='blue', font=(16))
    buttonCall.pack()
    buttonCall.place(x=200, y=228, width=150)
    
    buttonCallUid=Button(main_frame, command=lambda: call_uid_remove(textbox_clids, project_type), text='Заявка(UID)', fg='blue', font=(16))
    buttonCallUid.pack()
    buttonCallUid.place(x=200, y=278, width=150)

    buttonCallnoUid=Button(main_frame, command=lambda: call_nouid_remove(textbox_clids, project_type), text='Заявка(OLD)', fg='blue', font=(16))
    buttonCallnoUid.pack()
    buttonCallnoUid.place(x=200, y=328, width=150)



    
    callremove_frame.pack(pady=20)

if __name__ == "__main__":
    print('callremove_page')
