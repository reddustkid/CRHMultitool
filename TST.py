import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from packages.ui.crhannul_page import main as newcrhremove_page
from packages.ui.bankruptcy_page import main as newbankruptcy_page
from packages.ui.callremove_page import main as callremove_page
from packages.ui.bankparser_page import main as bankparser_page
from packages.ui.bankimport_page import main as bankimport_page


root = tk.Tk()
root.geometry('510x450')
root.resizable(width=False, height=False)
root.title('TST')
root.iconbitmap("frog.ico")

def hide_indicators():
    newcrhremove_indicate.config(bg='#c3c3c3')
    callremove_indicate.config(bg='#c3c3c3')
    newbankruptcy_indicate.config(bg='#c3c3c3')
    bankimport_indicate.config(bg='#c3c3c3')

#Удаление предыдущей страницы после выбора новой
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
        
#Маленький индикатор выбраной страницы, так же переход на страницу и удаление предыдущей
def indicate(lb, page,main_frame):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page(main_frame)

options_frame = tk.Frame(root, bg='#c3c3c3')

#Кнопка страницы удаления КИ
# crhremove_btn = tk.Button(options_frame, text='CrhRemove\n', font=('Bold', 12),
#                      fg='#158aff', bd=0, bg='#c3c3c3',
#                      command=lambda: indicate(crhremove_indicate, crhremove_page, main_frame))
# crhremove_btn.place(x=5,y=100)
# crhremove_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
# crhremove_indicate.place(x=2, y=100, width=5, height=46)

#Кнопка страницы удаления КИ в новом формате
newcrhremove_btn = tk.Button(options_frame, text='Annulment\n', font=('Bold', 12),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(newcrhremove_indicate, newcrhremove_page, main_frame))
newcrhremove_btn.place(x=5,y=100)
newcrhremove_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
newcrhremove_indicate.place(x=2, y=100, width=5, height=46)

#Кнопка передачи банкротства в новом формате
newbankruptcy_btn = tk.Button(options_frame, text='Bankruptcy\n', font=('Bold', 12),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(newbankruptcy_indicate, newbankruptcy_page, main_frame))
newbankruptcy_btn.place(x=5,y=150)
newbankruptcy_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
newbankruptcy_indicate.place(x=2, y=150, width=5, height=46)

#Кнопка страницы импорта файла банкротов
bankimport_btn = tk.Button(options_frame, text='BankImport ', font=('Bold', 12),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(bankimport_indicate, bankimport_page, main_frame))
bankimport_btn.place(x=5,y=200)
bankimport_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
bankimport_indicate.place(x=2, y=200, width=5, height=40)

#Кнопка страницы удаления заявки
callremove_btn = tk.Button(options_frame, text='CallRemove ', font=('Bold', 12),
                     fg='#158aff', bd=0, bg='#c3c3c3',
                     command=lambda: indicate(callremove_indicate, callremove_page, main_frame))
callremove_btn.place(x=5,y=250)
callremove_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
callremove_indicate.place(x=2, y=250, width=5, height=40)

# #Кнопка страницы парсера банкротов
# bankparser_btn = tk.Button(options_frame, text='             ', font=('Bold', 12),
#                      fg='#158aff', bd=0, bg='#c3c3c3',
#                      command=lambda: indicate(bankparser_indicate, bankparser_page, main_frame))
# bankparser_btn.place(x=5,y=400)
# bankparser_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
# bankparser_indicate.place(x=2, y=400, width=5, height=40)



#Меню выбора 
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=120, height=450)

main_frame=tk.Frame(root, highlightbackground='black',
                    highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=450, width=500)


root.mainloop()
