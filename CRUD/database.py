DB_NAME: str = 'data.txt'
DB_TEMPLATE: dict[str] = {
    'serial': 'xxxxxx',
    'tanggal_input': 'yyyy-mm-dd',
    'judul': 255 * ' ',
    'penulis': 255 * ' ',
    'tahun_terbit': 'yyyy'
}

def check():
    print(DB_NAME)
    print(DB_TEMPLATE)
    