from . import Operasi
from . import View

DB = 'data.txt'
TEMPLATE = {
    'pk': 'XXXXXX',
    'date_add': 'yyyy-mm-dd',
    'judul': 255 * ' ',
    'penulis': 255 * ' ',
    'tahun': 'yyyy'
}

def init_console():
    try:
        with open(DB, 'r') as file:
            print('Database Ditemukan.')
    except:
        print('Database tidak ditemukan. Silakan buat database baru.')
        Operasi.create_first_data()