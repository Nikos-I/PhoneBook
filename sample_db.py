import sqlite3


conn = sqlite3.connect('.\Seminar7\PhoneBook\db\phone_book.db')

cur = conn.cursor()

cur.execute("select id_person, lastname, firstname, patronymic, note from persons;")
list_person = cur.fetchall()
print(f'list_person {list_person}')

cur.execute("select id_phone, id_person, id_type, phone_number from phones;")
list_phones = cur.fetchall()
print(f'list_phones {list_phones}')

cur.execute("select id_type, c_type from types;")
list_types = cur.fetchall()
print(f'list_types {list_types}')


cur.execute("SELECT * FROM persons p LEFT JOIN phones ph ON p.id_person = p.id_person join types t on t.id_type=ph.id_type;")
print(f' list_full {cur.fetchall()}')

conn.close()
