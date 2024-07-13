from . import Database, Input_user, Operasi, Utils

def read_console():
    data = Operasi.read_data()
    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = 'Tahun Terbit'
    date_add = 'Tanggal Input'

    print('=' * 85)
    print(f'{index:3} | {judul:30} | {penulis:30} | {tahun:5}')
    print('-' * 85)

    for index, data in enumerate(data, 1):
        data_break = data.split(',')
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]
        print(f'{index:<3} | {judul:.30} | {penulis:.30} | {tahun:5}', end='')
    
    print('-' * 85)

def write_console():
    Operasi.write_data()

