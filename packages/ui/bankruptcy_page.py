import tkinter as tk
from tkinter import *
import packages.remove.bank.query as query


def bank_remove(textbox_conumbers, project_type, bki_type):
    project = int(project_type.get())
    conumbers = str(textbox_conumbers.get("1.0","end-1c"))
    bki_type = int(bki_type.get())
    query.main(conumbers,project,bki_type)

def main(main_frame):
    bankruptcy_frame = tk.Frame(main_frame)
    conumbers = StringVar()
    project_type = StringVar(bankruptcy_frame)
    bki_type = StringVar(bankruptcy_frame)
    
    lb = tk.Label(bankruptcy_frame, text='Банкротство', font=('Bold', 14))
    lb.pack()

    frame_conumbers = LabelFrame(main_frame, width=150, height=210, text="Contract numbers")
    frame_conumbers.pack()
    frame_conumbers.place(x=15, y=50)
    
    textbox_conumbers=Text(frame_conumbers,fg='blue',font=(16))
    textbox_conumbers.pack()
    textbox_conumbers.place(width=144,height=190)

    radio_project_type = {"Lime" : "0",
          "Konga" : "1",
          "Mango" : "2",
          "Cess" : "3"}
    frame = LabelFrame(main_frame, width=100, height=200, text="Project")
    frame.pack()
    frame.place(x=200, y=50)
    
    for (text, radio_project_type) in radio_project_type.items():
        Radiobutton(frame, text = text, variable = project_type,
                value = radio_project_type, indicator = 0,
                background = "white", width = 20).pack(fill = X, ipady = 2, anchor=W)
        
    radio_bki_type = {"1" : "0",
          "2" : "1"}
    frame_Bki = LabelFrame(main_frame, width=150, height=200, text="BKI")
    frame_Bki.pack()
    frame_Bki.place(x=15, y=355)
    for (text, radio_bki_type) in radio_bki_type.items():
        Radiobutton(frame_Bki, text = text, variable = bki_type,
                value = radio_bki_type, indicator = 0,
                background = "white", width = 20).pack(fill = X, ipady = 2, anchor=W)
        
    button_Crh=Button(main_frame, command=lambda: bank_remove(textbox_conumbers, project_type,bki_type), text='\nGenerate\n', fg='blue', font=(16))
    button_Crh.pack()
    button_Crh.place(x=200, y=360, width=152)

    bankruptcy_frame.pack(pady=20)

if __name__ == "__main__":
    print('bankruptcy_page')
