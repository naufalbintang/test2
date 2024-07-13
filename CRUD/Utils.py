import random
import string

list_pilihan = ['Keluar', 'Read Data', 'Write Data', 'Update Data', 'Delete Data']

def random_string(panjang):
    random_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return random_string