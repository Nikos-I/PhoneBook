import sqlite3
import json_module
import csv_module

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
print(f'list_full {cur.fetchall()}')

cur.close()
conn.close()

print(f'Тестовые данные: {list_types}')
# экспорты
json_module.exp_json(list_types, 'export')
csv_module.exp_csv(list_types, 'export')

# импорты
imp_test_csv = csv_module.imp_csv('export')
imp_test_json = json_module.imp_json('export')
print(f'Импорт csv: {imp_test_csv}')
print(f'Импорт json: {imp_test_json}')
