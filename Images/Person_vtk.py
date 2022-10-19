import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Телефонный справочник")
        #setting window size
        width=622
        height=504
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        lbl_title=tk.Label(root)
        ft = tkFont.Font(family='Serif',size=10)
        lbl_title["font"] = ft
        lbl_title["fg"] = "#333333"
        lbl_title["justify"] = "center"
        lbl_title["text"] = "Контакты"
        lbl_title["relief"] = "flat"
        lbl_title.place(x=100,y=10,width=70,height=25)

        lst_person=tk.Listbox(root)
        lst_person["borderwidth"] = "3px"
        ft = tkFont.Font(family='Serif',size=10)
        lst_person["font"] = ft
        lst_person["fg"] = "#333333"
        lst_person["justify"] = "center"
        lst_person.place(x=30,y=40,width=219,height=386)

        btn_add_cont=tk.Button(root)
        btn_add_cont["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Serif',size=10)
        btn_add_cont["font"] = ft
        btn_add_cont["fg"] = "#000000"
        btn_add_cont["justify"] = "center"
        btn_add_cont["text"] = "Добавить контакт"
        btn_add_cont.place(x=80,y=440,width=120,height=30)
        btn_add_cont["command"] = self.GButton_727_command

        btn_save_cont=tk.Button(root)
        btn_save_cont["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Serif',size=10)
        btn_save_cont["font"] = ft
        btn_save_cont["fg"] = "#000000"
        btn_save_cont["justify"] = "center"
        btn_save_cont["text"] = "Сохранить контакт"
        btn_save_cont.place(x=260,y=440,width=120,height=25)
        btn_save_cont["command"] = self.GButton_144_command

        btn_del_cont=tk.Button(root)
        btn_del_cont["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Serif',size=10)
        btn_del_cont["font"] = ft
        btn_del_cont["fg"] = "#000000"
        btn_del_cont["justify"] = "center"
        btn_del_cont["text"] = "Удалить контакт"
        btn_del_cont.place(x=470,y=440,width=120,height=25)
        btn_del_cont["command"] = self.GButton_255_command

        # GMessage_847=tk.Message(root)
        # ft = tkFont.Font(family='Serif',size=10)
        # GMessage_847["font"] = ft
        # GMessage_847["fg"] = "#333333"
        # GMessage_847["justify"] = "center"
        # GMessage_847["text"] = "Ошибка!"
        # GMessage_847.place(x=200,y=470,width=80,height=25)

        lbl_lastname=tk.Label(root)
        ft = tkFont.Font(family='Serif',size=10)
        lbl_lastname["font"] = ft
        lbl_lastname["fg"] = "#333333"
        lbl_lastname["justify"] = "right"
        lbl_lastname["text"] = "Фамилия"
        lbl_lastname.place(x=260,y=80,width=70,height=25)
        
        ent_lastname=tk.Entry(root)
        ent_lastname["borderwidth"] = "2px"
        ft = tkFont.Font(family='Serif',size=10)
        ent_lastname["font"] = ft
        ent_lastname["fg"] = "#333333"
        ent_lastname["justify"] = "center"
        ent_lastname["text"] = "Entry"
        ent_lastname.place(x=340,y=80,width=250,height=30)

        lbl_firstname=tk.Label(root)
        ft = tkFont.Font(family='Serif',size=10)
        lbl_firstname["font"] = ft
        lbl_firstname["fg"] = "#333333"
        lbl_firstname["justify"] = "right"
        lbl_firstname["text"] = "Имя"
        lbl_firstname.place(x=260,y=130,width=70,height=25)
        
        ent_firstname=tk.Entry(root)
        ent_firstname["borderwidth"] = "2px"
        ft = tkFont.Font(family='Serif',size=10)
        ent_firstname["font"] = ft
        ent_firstname["fg"] = "#333333"
        ent_firstname["justify"] = "center"
        ent_firstname["text"] = "Entry"
        ent_firstname.place(x=340,y=130,width=245,height=30)

        lbl_patronymic=tk.Label(root)
        ft = tkFont.Font(family='Serif',size=10)
        lbl_patronymic["font"] = ft
        lbl_patronymic["fg"] = "#333333"
        lbl_patronymic["justify"] = "right"
        lbl_patronymic["text"] = "Отчество"
        lbl_patronymic.place(x=260,y=180,width=70,height=25)

        ent_patronymic=tk.Entry(root)
        ent_patronymic["borderwidth"] = "2px"
        ft = tkFont.Font(family='Serif',size=10)
        ent_patronymic["font"] = ft
        ent_patronymic["fg"] = "#333333"
        ent_patronymic["justify"] = "center"
        ent_patronymic["text"] = "Entry"
        ent_patronymic.place(x=340,y=180,width=247,height=30)

        lbl_phone_num=tk.Label(root)
        ft = tkFont.Font(family='Serif',size=10)
        lbl_phone_num["font"] = ft
        lbl_phone_num["fg"] = "#333333"
        lbl_phone_num["justify"] = "right"
        lbl_phone_num["text"] = "Телефоны"
        lbl_phone_num.place(x=260,y=230,width=70,height=25)

        lbl_phone_num=tk.Listbox(root)
        lbl_phone_num["borderwidth"] = "2px"
        ft = tkFont.Font(family='Serif',size=10)
        lbl_phone_num["font"] = ft
        lbl_phone_num["fg"] = "#333333"
        lbl_phone_num["justify"] = "center"
        lbl_phone_num.place(x=340,y=230,width=247,height=91)

        btn_del_phone=tk.Button(root)
        btn_del_phone["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Serif',size=10)
        btn_del_phone["font"] = ft
        btn_del_phone["fg"] = "#000000"
        btn_del_phone["justify"] = "center"
        btn_del_phone["text"] = "Удалить"
        btn_del_phone.place(x=360,y=340,width=70,height=25)
        btn_del_phone["command"] = self.GButton_13_command

        btn_save_phone=tk.Button(root)
        btn_save_phone["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Serif',size=10)
        btn_save_phone["font"] = ft
        btn_save_phone["fg"] = "#000000"
        btn_save_phone["justify"] = "center"
        btn_save_phone["text"] = "Сохранить"
        btn_save_phone.place(x=490,y=340,width=70,height=25)
        btn_save_phone["command"] = self.GButton_318_command

    def GButton_255_command(self):
        print("command")


    def GButton_144_command(self):
        print("command")


    def GButton_727_command(self):
        print("command")


    def GButton_13_command(self):
        print("command")


    def GButton_318_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
