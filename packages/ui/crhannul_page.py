import tkinter as tk
from tkinter import *
import packages.filenames.nbki.filename as nbki_filename
import packages.filenames.sbki.filename as sbki_filename
# import packages.remove.crh.nbki.query_new as nbki_crh_query_new
# import packages.remove.crh.sbki.query_ann as sbki_crh_query_ann
import packages.remove.crh.query_nbki as ann_nbki
import packages.remove.crh.query_sbki as ann_sbki



def crh_remove(textbox_conumbers, project_type,textbox_opcode,textbox_actvolume,textbox_actreason,bki_type):
    conumbers       = StringVar()
    opcode          = StringVar()
    actvolume       = StringVar()
    actreason       = StringVar()
    project         = int(project_type.get())
    bki_type        = int(bki_type.get())
    conumbers       = str(textbox_conumbers.get("1.0","end-1c"))
    opcode          = str(textbox_opcode.get("1.0","end-1c"))
    actvolume       = str(textbox_actvolume.get("1.0","end-1c"))
    actreason       = str(textbox_actreason.get("1.0","end-1c"))

    if bki_type == 0:
        ann_nbki.main(conumbers,project,opcode,actreason)
    else:
        ann_sbki.main(conumbers,project,opcode,actvolume,actreason)


def main(main_frame):
    crhannul_frame = tk.Frame(main_frame)
    project_type = StringVar(crhannul_frame)
    bki_type = StringVar(crhannul_frame)
    
    lb = tk.Label(crhannul_frame, text='Аннулирование КИ', font=('Bold', 14))
    lb.pack()

    frame_conumbers = LabelFrame(main_frame, width=150, height=210, text="Contract numbers")
    frame_conumbers.pack()
    frame_conumbers.place(x=15, y=50)
    textbox_conumbers=Text(frame_conumbers,fg='blue',font=(16))
    textbox_conumbers.pack()
    textbox_conumbers.place(width=144,height=190)


    frame_opcode = LabelFrame(main_frame, width=150, height=50, text="Operation code")
    frame_opcode.pack()
    frame_opcode.place(x=200, y=200)
    textbox_opcode=Text(frame_opcode,fg='blue',font=(16))
    textbox_opcode.tag_configure("center", justify='center')
    textbox_opcode.insert("1.0", "D")
    textbox_opcode.tag_add("center", "1.0", "end")
    textbox_opcode.pack()
    textbox_opcode.place(width=144,height=30)

    frame_actvolume = LabelFrame(main_frame, width=150, height=50, text="Action volume")
    frame_actvolume.pack()
    frame_actvolume.place(x=200, y=250)
    textbox_actvolume=Text(frame_actvolume,fg='blue',font=(16))
    textbox_actvolume.tag_configure("center", justify='center')
    textbox_actvolume.insert("1.0", "3")
    textbox_actvolume.tag_add("center", "1.0", "end")
    textbox_actvolume.pack()
    textbox_actvolume.place(width=144,height=30)

    frame_actreason = LabelFrame(main_frame, width=150, height=50, text="Action reason")
    frame_actreason.pack()
    frame_actreason.place(x=200, y=300)
    textbox_actreason=Text(frame_actreason,fg='blue',font=(16))
    textbox_actreason.tag_configure("center", justify='center')
    textbox_actreason.insert("1.0", "3")
    textbox_actreason.tag_add("center", "1.0", "end")
    textbox_actreason.pack()
    textbox_actreason.place(width=144,height=30)

    radio_project_type = {"Lime" : "0",
          "Konga" : "1",
          "Mango" : "2",
          "Cess" : "3"}
    frame_project = LabelFrame(main_frame, width=100, height=200, text="Project")
    frame_project.pack()
    frame_project.place(x=200, y=50)
    
    for (text, radio_project_type) in radio_project_type.items():
        Radiobutton(frame_project, text = text, variable = project_type,
                value = radio_project_type, indicator = 0,
                background = "white", width = 20).pack(fill = X, ipady = 2, anchor=W)
        
    radio_bki_type = {"NBKI" : "0",
          "ScoringBureau" : "1"}
    frame_bki = LabelFrame(main_frame, width=150, height=200, text="BKI")
    frame_bki.pack()
    frame_bki.place(x=15, y=355)
    for (text, radio_bki_type) in radio_bki_type.items():
        Radiobutton(frame_bki, text = text, variable = bki_type,
                value = radio_bki_type, indicator = 0,
                background = "white", width = 20).pack(fill = X, ipady = 2, anchor=W)
        
    buttonCrh=Button(main_frame, command=lambda: crh_remove(textbox_conumbers, project_type,textbox_opcode,textbox_actvolume,textbox_actreason,bki_type), text='\nGenerate\n', fg='blue', font=(16))
    buttonCrh.pack()
    buttonCrh.place(x=200, y=360, width=152)

    crhannul_frame.pack(pady=20)

if __name__ == "__main__":
    print('crhremove_page')
