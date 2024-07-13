import os
import CRUD

if __name__ == '__main__':
    sistem_operasi = os.name
    match sistem_operasi:
        case 'nt': os.system('cls')        
        case 'posix': os.system('clear')

    print(f'{'PERPUSTAKAAN':^32}')
    print('=' * 32 + '\n')

    # cek db
    DB = CRUD.init_console()

    while True:
        match sistem_operasi:
            case 'nt': os.system('cls')        
            case 'posix': os.system('clear')        

        
        # header
        print(f'{'PERPUSTAKAAN':^32}')
        print('=' * 32 + '\n')
        
        # pilihan
        list_pilihan = CRUD.list_pilihan
        for nomor, pilihan in enumerate(list_pilihan):
            print(f'{nomor}. {pilihan}')
        input_pilihan = CRUD.input_pilihan()


        # output berdasarkan pilihan
        match input_pilihan:
            case 0:
                break
            case 1:
                CRUD.read_console()
            case 2:
                CRUD.write_console()    
            case 3:       
                print('Update Data') 
            case 4:
                print('Delete Data')        

        # break
        is_done = input('\nApakah sudah selesai (y/n)? ')
        if is_done.lower() == 'y':
            break
        elif is_done.lower() == 'n':
            None
        else:
            print('Input tidak valid, keluar dari program.')
            break

    print('program selesai, makasi bwaanggg!\n')