from tkinter import *
from tkinter import ttk
import sqlite3
import functools 
import operator 


conn = sqlite3.connect('db\phone_book.db')
cur = conn.cursor()
cur.execute("select title from v_person_short;")

list_person = functools.reduce(operator.add,(cur.fetchall()))
print(f'list_person {list_person}')

root = Tk()
root.title("METANIT.COM")
root.geometry("400x500")

# list_person = ["1. Иванов П.С.", "2. Петров И.С.", "3. Сидоров П.И."]
person_var = Variable(value=list_person)

lbox_person = Listbox(listvariable=person_var, height=20, width=30)

lbox_person.pack(anchor=NW, padx=5, pady=5)
# lbox_person.pack(anchor=NW, fill=X, padx=5, pady=5)

root.mainloop()


# SELECT (lastname + " " + substr(firstname, 1,1) + "." + substr(firstname, 1,1) + ".") as title
#       FROM persons p
conn.close