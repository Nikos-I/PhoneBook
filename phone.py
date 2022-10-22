from logging import root
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk


def GRadio_261_command():
    print("command")


def btn_add_command():
    # global w_phone
    # w_phone.destroy()
    print("command")

def btn_cancel_command():
    print("command")
    end_phone = True


def add_phone(a_conn, a_cur):

    
    w_phone = tk.Tk()
    #setting title
    w_phone.title("Телефон")
    #setting window size
    width=200
    height=181
    screenwidth = w_phone.winfo_screenwidth()
    screenheight = w_phone.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    w_phone.geometry(alignstr)
    w_phone.resizable(width=False, height=False)

    lbl_phone=tk.Label(w_phone)
    ft = tkFont.Font(family='Times',size=8)
    lbl_phone["font"] = ft
    lbl_phone["fg"] = "#333333"
    lbl_phone["justify"] = "left"
    lbl_phone["text"] = "Номер телефона"
    lbl_phone.place(x=10,y=10,width=130,height=30)

    ent_phone=tk.Entry(w_phone)
    ent_phone["borderwidth"] = "1px"
    # ft = tkFont.Font(family='Times',size=10)
    ent_phone["font"] = ft
    ent_phone["fg"] = "#333333"
    ent_phone["justify"] = "left"
    ent_phone["text"] = "Entry"
    ent_phone.place(x=10,y=40,width=180,height=30)


    languages = ["Python", "C#", "Java", "JavaScript"]
    # по умолчанию будет выбран первый элемент из languages
    languages_var = tk.StringVar(value=languages[0])   
    
    cmb_type = ttk.Combobox(w_phone, textvariable=languages_var, justify = "left",  values=languages)
    # ft = tkFont.Font(family='Times',size=10)
    cmb_type["font"] = ft
    # cmb_type["fg"] = "#333333"

    cmb_type.place(x=10,y=80,width=132,height=30)
    # cmb_type["command"] = GRadio_261_command
    # print(cmb_type.get())

    # GRadio_261=tk.Radiobutton(w_phone)
    # ft = tkFont.Font(family='Times',size=12)
    # GRadio_261["font"] = ft
    # GRadio_261["fg"] = "#333333"
    # GRadio_261["justify"] = "left"
    # GRadio_261["text"] = "RadioButton"
    # GRadio_261.place(x=10,y=80,width=132,height=30)
    # GRadio_261["command"] = GRadio_261_command

    btn_add=tk.Button(w_phone)
    btn_add["bg"] = "#f0f0f0"
    # ft = tkFont.Font(family='Times',size=10)
    btn_add["font"] = ft
    btn_add["fg"] = "#000000"
    btn_add["justify"] = "left"
    btn_add["text"] = "Добавить"
    btn_add.place(x=10,y=140,width=75,height=25)
    # btn_add["command"] = w_phone.destroy
    btn_add["command"] = btn_add_command

    btn_cancel=tk.Button(w_phone)
    btn_cancel["bg"] = "#f0f0f0"
    # ft = tkFont.Font(family='Times',size=10)
    btn_cancel["font"] = ft
    btn_cancel["fg"] = "#000000"
    btn_cancel["justify"] = "left"
    btn_cancel["text"] = "Отменить"
    btn_cancel.place(x=115,y=140,width=75,height=25)
    btn_cancel["command"] = btn_cancel_command

    w_phone.mainloop()

