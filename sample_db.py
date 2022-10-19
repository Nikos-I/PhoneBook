import sqlite3
import json_module
import csv_module
import txt_module

conn = sqlite3.connect('db\phone_book.db')

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

cur.execute(
    "SELECT * FROM persons p LEFT JOIN phones ph ON p.id_person = p.id_person join types t on t.id_type=ph.id_type;")
list_full = cur.fetchall()
print(f'list_full {list_full}')

cur.close()
conn.close()

print(f'Тестовые данные: {list_full}')

# экспорты
json_module.exp_json(list_full, 'export')
csv_module.exp_csv(list_full, 'export')
txt_module.exp_txt(list_full, 'export')

# импорты
imp_test_csv = csv_module.imp_csv('export')
imp_test_json = json_module.imp_json('export')
imp_test_txt = txt_module.imp_txt('export')

print(f'Импорт csv: {imp_test_csv}')
print(f'Импорт json: {imp_test_json}')
print(f'Импорт txt: {imp_test_txt}')
