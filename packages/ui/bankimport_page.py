import tkinter as tk
from tkinter import *
import packages.remove.bank.bankimport.query as query_bankimport


def bank_remove(project_type):
    project = int(project_type.get())
    query_bankimport.main(project)

def main(main_frame):
    bankruptcy_frame = tk.Frame(main_frame)
    conumbers = StringVar()
    project_type = StringVar(bankruptcy_frame)
    
    lb = tk.Label(bankruptcy_frame, text='Импорт банкротства', font=('Bold', 14))
    lb.pack()


    radio_project_type = {"Lime" : "0",
          "Konga" : "1",
          "Mango" : "2",
          "Cess" : "3"}
    frame = LabelFrame(main_frame, width=100, height=200, text="Project")
    frame.pack()
    frame.place(x=100, y=100)
    
    for (text, radio_project_type) in radio_project_type.items():
        Radiobutton(frame, text = text, variable = project_type,
                value = radio_project_type, indicator = 0,
                background = "white", width = 20).pack(fill = X, ipady = 2, anchor=W)
        
    button_Crh=Button(main_frame, command=lambda: bank_remove(project_type), text='Generate\n', fg='blue', font=(16))
    button_Crh.pack()
    button_Crh.place(x=100, y=260, width=152)

    # tip = tk.Label(main_frame, text='TIP: Файл импорта bankimport', font=('Bold', 8))
    # tip.pack()
    # tip.place(x=100, y=330)

    bankruptcy_frame.pack(pady=20)

if __name__ == "__main__":
    print('bank_parse_page')
