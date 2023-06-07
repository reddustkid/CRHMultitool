import tkinter as tk
from tkinter import *
import packages.filenames.nbki.filename as nbki_filename
import packages.filenames.sbki.filename as sbki_filename
import packages.remove.crh.nbki_old.query as nbki_crh_query
import packages.remove.crh.sbki_old.query as sbki_crh_query


def crh_remove(textbox_conumbers, posnum, project_type, bki_type):
    project = int(project_type.get())
    conumbers = str(textbox_conumbers.get("1.0","end-1c"))
    bki_type = int(bki_type.get())
    print(conumbers)
    if bki_type == 0:
        filename = nbki_filename.crh(project)
        nbki_crh_query.main(conumbers,filename,project)
    else:
        posnum = int(posnum.get())
        filename = sbki_filename.generate_name_sbki(posnum, project)
        sbki_crh_query.main(conumbers,filename,project)

def main(main_frame):
    crhremove_frame = tk.Frame(main_frame)
    conumbers=StringVar()
    posnum=StringVar()
    project_type = StringVar(crhremove_frame)
    bki_type = StringVar(crhremove_frame)
    
    lb = tk.Label(crhremove_frame, text='Удаление КИ  ', font=('Bold', 14))
    lb.pack()

    frameConumbers = LabelFrame(main_frame, width=150, height=262, text="Contract numbers")
    frameConumbers.pack()
    frameConumbers.place(x=15, y=50)
    
    textbox_conumbers=Text(frameConumbers,fg='blue',font=(16))
    textbox_conumbers.pack()
    textbox_conumbers.place(width=144,height=242)
    

    framePosition = LabelFrame(main_frame, width=150, height=70, text="Position number (SBKI)")
    framePosition.pack()
    framePosition.place(x=200, y=50)
    
    textbox_position=Entry(framePosition,textvariable=posnum,fg='blue',font=(16), justify=CENTER)
    textbox_position.pack()
    textbox_position.place(width=144,height=50)

    radio_project_type = {"Lime" : "0",
          "Konga" : "1",
          "Mango" : "2",
          "Cess" : "3"}
    frame = LabelFrame(main_frame, width=100, height=200, text="Project")
    frame.pack()
    frame.place(x=200, y=137)
    
    for (text, radio_project_type) in radio_project_type.items():
        Radiobutton(frame, text = text, variable = project_type,
                value = radio_project_type, indicator = 0,
                background = "white", width = 20).pack(fill = X, ipady = 5, anchor=W)

    radio_bki_type = {"NBKI" : "0",
          "ScoringBureau" : "1"}
    frameBki = LabelFrame(main_frame, width=100, height=200, text="BKI")
    frameBki.pack()
    frameBki.place(x=200, y=300)
    for (text, radio_bki_type) in radio_bki_type.items():
        Radiobutton(frameBki, text = text, variable = bki_type,
                value = radio_bki_type, indicator = 0,
                background = "white", width = 20).pack(fill = X, ipady = 5, anchor=W)

    
    buttonCrh=Button(main_frame, command=lambda: crh_remove(textbox_conumbers, posnum, project_type, bki_type), text='\nGenerate\n', fg='blue', font=(16))
    buttonCrh.pack()
    buttonCrh.place(x=15, y=320, width=150)

    crhremove_frame.pack(pady=20)

if __name__ == "__main__":
    print('crhremove_page')
