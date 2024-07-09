import os
import input_data
from CRUD import database

if __name__ == '__main__':
    
    list_pilihan: list[str] = ['Keluar', 'Read Data', 'Create Data', 'Update Data', 'Delete Data']
    
    while True:
        sistem_operasi: str = os.name
        match sistem_operasi:
            case 'nt': os.system('cls')
            case 'posix': os.system('clear')
            
        print(f'{'PERPUSTAKAAN':^32}')
        print(f'{'=' * 32}\n')
        
        for nomor, pilihan in enumerate(list_pilihan):
            print(f'{nomor}. {pilihan}')
        
        input_pilihan: int = input_data.fungsi_input_pilihan(len(list_pilihan))
        
        match input_pilihan:
            case 0:
                print('Keluar')
                break
            case 1:
                print(list_pilihan[1])    
            case 2:
                print(list_pilihan[2])    
            case 3:
                print(list_pilihan[3])    
            case 4:
                print(list_pilihan[4])    
        # break
        is_done: str = input('\nApakah sudah selesai (y/n)? ')
        if is_done.lower() == 'y':
            break
        elif is_done.lower() == 'n':
            pass
        else:
            print('invalid input, exiting program')
            break            