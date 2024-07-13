from . import Database, Operasi, Utils, View

def input_pilihan():
    while True:
        input_pilihan = input('\nMasukkan pilihan: ')
        if input_pilihan.isdigit():
            input_pilihan = int(input_pilihan)
            if 0 <= input_pilihan <= len(Utils.list_pilihan) - 1:
                break
            else:
                print(f'Masukkan angka 0 - {len(Utils.list_pilihan)}')
        else:
            print(f'Masukkan angka 0 - {len(Utils.list_pilihan)}')
    return input_pilihan

def input_judul():
    while True:
        try:
            judul = input('Judul\t\t: ')
            if len(judul) <= 255:
                break
            else:
                print('Judul maksimal 255 karakter.')
        except:
            print('Tolong masukkan judul yang valid.')
    return judul

def input_penulis():
    while True:
        penulis = input('Nama penulis\t: ')
        if len(penulis) <= 255:
            break
        else:
            print('Nama penulis maksimal 255 karakter.')
    return penulis

def input_tahun():
    while True:
        try:
            tahun = int(input('Tahun terbit\t: '))
            if len(str(tahun)) <= 4:
                break
            else:
                print(f'Tolong masukkan tahun yang valid.')
        except:
            print(f'Tolong masukkan angka.')
    return tahun