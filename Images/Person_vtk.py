import tkinter as tk
import tkinter.font as tkFont
import sqlite3
import functools
import operator


class App:
    def __init__(self, root):
        global conn
        global cur
        global list_person

        name_var = tk.StringVar()

        def submit(event):
            name = name_var.get()
            print("The name is : " + name)
            name_var.set(name)

        conn = sqlite3.connect('../db/phone_book.db')
        cur = conn.cursor()
        cur.execute("select title from v_person_short;")
        list_person = functools.reduce(operator.add, (cur.fetchall()))

        # setting title
        root.title("Телефонный справочник")
        # setting window size
        width = 622
        height = 504
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        ft = tkFont.Font(family='Serif', size=10)
        lbl_title = tk.Label(root, font=ft, fg="#333333", justify="center",
                             text="Контакты", relief="flat")
        lbl_title.place(x=100, y=10, width=70, height=25)

        person_var = tk.Variable(value=list_person)
        lst_person = tk.Listbox(root, borderwidth="3px", font=ft, fg="#333333", justify="left",
                                listvariable=person_var, selectmode=tk.SINGLE)
        lst_person.bind("<<ListboxSelect>>", self.lst_person_selected)
        lst_person.place(x=30, y=40, width=219, height=386)

        btn_add_cont = tk.Button(root, bg="#f0f0f0", font=ft, fg="#000000", justify="center",
                                 text="Добавить контакт")
        btn_add_cont.place(x=80, y=440, width=120, height=30)
        btn_add_cont["command"] = self.btn_add_cont_command

        btn_save_cont = tk.Button(root, bg="#f0f0f0", font=ft, fg="#000000", justify="center",
                                  text="Сохранить контакт")
        btn_save_cont.place(x=260, y=440, width=120, height=25)
        btn_save_cont["command"] = self.btn_save_con_command

        btn_del_cont = tk.Button(root, bg="#f0f0f0", font=ft, fg="#000000", justify="center",
                                 text="Удалить контакт")
        btn_del_cont.place(x=470, y=440, width=120, height=25)
        btn_del_cont["command"] = self.btn_del_cont_command

        lbl_lastname = tk.Label(root, font=ft, fg="#333333", justify="right",
                                text="Фамилия")
        lbl_lastname.place(x=260, y=80, width=70, height=25)

        ent_lastname = tk.Entry(root, borderwidth="2px", font=ft, fg="#333333", justify="center", textvariable=name_var)
        ent_lastname.place(x=340, y=80, width=250, height=30)
        ent_lastname.bind("<Return>", submit)

        lbl_firstname = tk.Label(root, font=ft, fg="#333333", justify="right",
                                 text="Имя")
        lbl_firstname.place(x=260, y=130, width=70, height=25)

        ent_firstname = tk.Entry(root, borderwidth="2px", font=ft, fg="#333333", justify="center")
        ent_firstname.place(x=340, y=130, width=245, height=30)

        lbl_patronymic = tk.Label(root, font=ft, fg="#333333", justify="right",
                                  text="Отчество")
        lbl_patronymic.place(x=260, y=180, width=70, height=25)

        ent_patronymic = tk.Entry(root, borderwidth="2px", font=ft, fg="#333333", justify="center")
        ent_patronymic.place(x=340, y=180, width=247, height=30)

        lbl_phone_num = tk.Label(root, font=ft, fg="#333333", justify="right",
                                 text="Телефоны")
        lbl_phone_num.place(x=260, y=230, width=70, height=25)

        lbl_phone_num = tk.Listbox(root, borderwidth="2px", font=ft, fg="#333333", justify="center")
        lbl_phone_num.place(x=340, y=230, width=247, height=91)

        btn_del_phone = tk.Button(root, bg="#f0f0f0", font=ft, fg="#000000", justify="center",
                                  text="Удалить")
        btn_del_phone.place(x=360, y=340, width=70, height=25)
        btn_del_phone["command"] = self.btn_del_phone_command

        btn_save_phone = tk.Button(root, bg="#f0f0f0", font=ft, fg="#000000", justify="center",
                                   text="Сохранить")
        btn_save_phone.place(x=490, y=340, width=70, height=25)
        btn_save_phone["command"] = self.btn_save_phone_command

    def lst_person_selected(self, event):
        select = list(self.list_person.curselection())
        print(select)

    def btn_del_cont_command(self):
        print("command1")

    def btn_save_con_command(self):
        print("command2")

    def btn_add_cont_command(self):
        print("command3")

    def btn_del_phone_command(self):
        print("command4")

    def btn_save_phone_command(self):
        print("command5")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

root.mainloop()
