import sqlite3

# добавить 1
# =====================
import json_module
import csv_module
import txt_module

# ====================

global conn 
global cur 


# добавить 2
# =====================
# Экспорт по таблично
def task1_export(e_conn, e_cur):
    
    e_cur.execute("select id_person, lastname, firstname, patronymic, note from persons;")
    list_person = e_cur.fetchall()
    # print(f'list_person {list_person}')

    e_cur.execute("select id_phone, id_person, id_type, phone_number from phones;")
    list_phones = e_cur.fetchall()
    # print(f'list_phones {list_phones}')

    e_cur.execute("select id_type, c_type from types;")
    list_types = e_cur.fetchall()
    # print(f'list_types {list_types}')

    json_module.exp_json(list_person, 'export_person')
    json_module.exp_json(list_phones, 'export_phones')
    json_module.exp_json(list_types, 'export_types')

    csv_module.exp_csv(list_person, 'export_person')
    csv_module.exp_csv(list_phones, 'export_phones')
    csv_module.exp_csv(list_types, 'export_types')

    txt_module.exp_txt(list_person, 'export_person')
    txt_module.exp_txt(list_phones, 'export_phones')
    txt_module.exp_txt(list_types, 'export_types')


# task1_export()


# добавить 3
# =====================
# Загрузка данных в программу (по таблично)
def task2_import(i_conn, i_cur):
    def task2_csv():
        imp_test_person = csv_module.imp_csv('export_person')
        imp_test_phones = csv_module.imp_csv('export_phones')
        imp_test_types = csv_module.imp_csv('export_types')
        # print(f'Импорт csv: person {imp_test_person}')
        # print(f'Импорт csv: phones {imp_test_phones}')
        # print(f'Импорт csv: types {imp_test_types}')

        for i in range(len(imp_test_person)):
            exec_str = f'REPLACE INTO persons (id_person, lastname, firstname, patronymic, note) VALUES ' \
                       f'({imp_test_person[i][0]}, "{imp_test_person[i][1]}", "{imp_test_person[i][2]}", ' \
                       f'"{imp_test_person[i][3]}", "{imp_test_person[i][4]}")'
            cur.execute(exec_str)
            i_conn.commit()

        for j in range(len(imp_test_phones)):
            exec_str = f'REPLACE INTO phones (id_phone, id_person, id_type, phone_number) VALUES ' \
                       f'({imp_test_phones[j][0]}, "{imp_test_phones[j][1]}", "{imp_test_phones[j][2]}", ' \
                       f'"{imp_test_phones[j][3]}")'
            i_cur.execute(exec_str)
            i_conn.commit()

        for k in range(len(imp_test_types)):
            exec_str = f'REPLACE INTO types (id_type, c_type) VALUES ' \
                       f'({imp_test_types[k][0]}, "{imp_test_types[k][1]}")'
            i_cur.execute(exec_str)
            i_conn.commit()

    def task2_json():
        imp_test_person = json_module.imp_json('export_person')
        imp_test_phones = json_module.imp_json('export_phones')
        imp_test_types = json_module.imp_json('export_types')
        print(f'Импорт json: person {imp_test_person}')
        print(f'Импорт json: phones {imp_test_phones}')
        print(f'Импорт json: types {imp_test_types}')

        for i in range(len(imp_test_person)):
            exec_str = f'REPLACE INTO persons (id_person, lastname, firstname, patronymic, note) VALUES ' \
                       f'({imp_test_person[i][0]}, "{imp_test_person[i][1]}", "{imp_test_person[i][2]}", ' \
                       f'"{imp_test_person[i][3]}", "{imp_test_person[i][4]}")'
            i_cur.execute(exec_str)
            i_conn.commit()

        for j in range(len(imp_test_phones)):
            exec_str = f'REPLACE INTO phones (id_phone, id_person, id_type, phone_number) VALUES ' \
                       f'({imp_test_phones[j][0]}, "{imp_test_phones[j][1]}", "{imp_test_phones[j][2]}", ' \
                       f'"{imp_test_phones[j][3]}")'
            i_cur.execute(exec_str)
            i_conn.commit()

        for k in range(len(imp_test_types)):
            exec_str = f'REPLACE INTO types (id_type, c_type) VALUES ' \
                       f'({imp_test_types[k][0]}, "{imp_test_types[k][1]}")'
            i_cur.execute(exec_str)
            i_conn.commit()

    def task2_txt():
        imp_test_person = txt_module.imp_txt('export_person')
        imp_test_phones = txt_module.imp_txt('export_phones')
        imp_test_types = txt_module.imp_txt('export_types')
        # print(f'Импорт txt: person {imp_test_person}')
        # print(f'Импорт txt: phones {imp_test_phones}')
        # print(f'Импорт txt: types {imp_test_types}')

        for i in range(len(imp_test_person)):
            exec_str = f'REPLACE INTO persons (id_person, lastname, firstname, patronymic, note) VALUES ' \
                       f'({imp_test_person[i][0]}, "{imp_test_person[i][1]}", "{imp_test_person[i][2]}", ' \
                       f'"{imp_test_person[i][3]}", "{imp_test_person[i][4]}")'
            i_cur.execute(exec_str)
            i_conn.commit()

        for j in range(len(imp_test_phones)):
            exec_str = f'REPLACE INTO phones (id_phone, id_person, id_type, phone_number) VALUES ' \
                       f'({imp_test_phones[j][0]}, "{imp_test_phones[j][1]}", "{imp_test_phones[j][2]}", ' \
                       f'"{imp_test_phones[j][3]}")'
            i_cur.execute(exec_str)
            i_conn.commit()

        for k in range(len(imp_test_types)):
            exec_str = f'REPLACE INTO types (id_type, c_type) VALUES ' \
                       f'({imp_test_types[k][0]}, "{imp_test_types[k][1]}")'
            i_cur.execute(exec_str)
            i_conn.commit()

    # task2_csv()
    # task2_json()
    # task2_txt()


# task2_import()

# cur.close()
# conn.close()

# cur.execute(
#     "SELECT * FROM persons p LEFT JOIN phones ph ON p.id_person = p.id_person join types t on t.id_type=ph.id_type;")
# list_full = cur.fetchall()
# print(f'list_full {list_full}')
