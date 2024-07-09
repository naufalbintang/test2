
def fungsi_input_pilihan(banyak_pilihan: int) -> int:
    while True:
        input_pilihan: str = input('Masukkan pilihan: ')
        if input_pilihan.isdigit():
            input_pilihan: int = int(input_pilihan)
            if 0 <= input_pilihan < banyak_pilihan:
                break
            else:
                print(f'Tolong masukkan pilihan antara 0 - {banyak_pilihan}')
        else:
            print(f'Tolong masukkan pilihan antara 0 - {banyak_pilihan}')
    return input_pilihan
    