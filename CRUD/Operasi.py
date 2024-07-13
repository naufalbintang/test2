from . import Database, Input_user, Utils, View
import datetime

def create_first_data():
    TEMPLATE = Database.TEMPLATE.copy()
    judul = Input_user.input_judul()
    penulis = Input_user.input_penulis()
    tahun = Input_user.input_tahun()
    pk = Utils.random_string(6)
    date_add = datetime.datetime.now()

    TEMPLATE['judul'] = judul + TEMPLATE['judul'][len(judul):]
    TEMPLATE['penulis'] = penulis + TEMPLATE['penulis'][len(penulis):]
    TEMPLATE['tahun'] = tahun
    TEMPLATE['pk'] = pk
    TEMPLATE['date_add'] = date_add

    data_str = f'{TEMPLATE['pk']},{TEMPLATE['date_add']},{TEMPLATE['judul']},{TEMPLATE['penulis']},{TEMPLATE['tahun']}\n'
    
    try:
        with open(Database.DB, 'w', encoding='utf-8') as file: 
            file.write(data_str)
    except:
        print('Gagal membuat data.')
    
def read_data():
    try:
        with open(Database.DB, 'r') as file:
            content = file.readlines()
            return content
    except:
        print('Tidak ada data untuk dibaca, silakan buat.')
        create_first_data()

def write_data():
    TEMPLATE = Database.TEMPLATE.copy()
    judul = Input_user.input_judul()
    penulis = Input_user.input_penulis()
    tahun = Input_user.input_tahun()
    pk = Utils.random_string(6)
    date_add = datetime.datetime.now()

    TEMPLATE['judul'] = judul + TEMPLATE['judul'][len(judul):]
    TEMPLATE['penulis'] = penulis + TEMPLATE['penulis'][len(penulis):]
    TEMPLATE['tahun'] = tahun
    TEMPLATE['pk'] = pk
    TEMPLATE['date_add'] = date_add
    data_str = f'{TEMPLATE['pk']},{TEMPLATE['date_add']},{TEMPLATE['judul']},{TEMPLATE['penulis']},{TEMPLATE['tahun']}\n'

    try:
        with open(Database.DB, 'a', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('Gagal menambah data.')

    


def Update_data():
    None

def Delete_data():
    None

