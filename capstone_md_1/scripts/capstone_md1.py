import sys #


data_karyawan = {
    "id_karyawan": None,
    "nik": None,
    "nama_karyawan": None,
    "alamat_karyawan": None,
    "divisi": None,
    "contact": None
} #mendeklarasikan dictionary data_karyawan


entry_list =[] #mendeklarasikan variable dengan list kosong



def create():
    global data_karyawan 
    print("{:<10} |>".format("Input data"), end=" ") #

    while True:
        try:
            num_entries = int(input('Berapa kali ingin memasukkan data karyawan? :'))
            break
        except Exception:
            print('Pilihan salah. Harap masukkan angka yang valid.')

    print(f'\nInput data untuk {num_entries} karyawan\n')

    for no in range(num_entries):
        # print("\n") 
        entry_data = {} 
        for key in data_karyawan: 
            entry_data[key] = input(f'Masukkan {key.replace("_", " ").title()} ke {no+1}: ') 
        entry_list.append(entry_data)
        print('\n')
    print("\nData berhasil di input")

    menu()


def read():
    print("|", end="") 
    for key in data_karyawan.keys():
        print("{:^20} |".format(key), end=" ") 
    print()


    for entry_data in entry_list:
        print("|", end="")
        for value in entry_data.values():
            print("{:^20} |".format(str(value)), end=" ")
        print()
    print(f"\nTotal data karyawan : {len(entry_list)}")
    menu()

    
def update():
    print("{:<10} |>".format("Fungsi ubah data"), end=" ")
    try:
        index_to_update = int(input('Masukkan data row ke berapa yang mau diubah: '))

        if 1 <= index_to_update <= len(entry_list):
            entry_data = entry_list[index_to_update - 1]
            print(f'\nUbah data untuk row ke-{index_to_update}:\n')

            update_option = input('Apakah Anda ingin mengubah semua nilai (Y/N)? ').strip().lower()
            if update_option in ('y','Y','N','n'):
                if update_option == 'y' or update_option =='Y':
                    for key in entry_data:
                        new_value = input(f'Masukkan nilai baru untuk {key.replace("_", " ").title()}: ')
                        entry_data[key] = new_value
                else:
                    columns_to_update = input('Masukkan kolom yang ingin diubah (pisahkan dengan koma): ').split(',')
                    for column in columns_to_update:
                        column = column.strip()
                        if column in entry_data:
                            new_value = input(f'Masukkan nilai baru untuk {column.replace("_", " ").title()}: ')
                            entry_data[column] = new_value
                        else:
                            print(f'Kolom {column} tidak ada.')
                            menu()
                print('data_karyawan berhasil diubah.\n')
                menu()
            else:
                print('Pilihan tidak valid. Gunakan "Y" untuk mengubah semua nilai atau "N" untuk mengubah nilai tertentu.')
                menu()
        else:
            print('Nomor data_karyawan tidak valid.')
            menu()
    except ValueError:
        print('Masukkan nomor yang valid.')
        menu()

    


def delete():
    print('fungsi hapus data_karyawan')

    while True:
        try:
            index_to_delete = int(input('Masukkan nomor data_karyawan yang ingin dihapus: '))
            if 1 <= index_to_delete <= len(entry_list):
                deleted_entry = entry_list.pop(index_to_delete - 1)
                print(f'\nData pada nomor {index_to_delete} berhasil dihapus:\n')
                print(deleted_entry)
                break
            else:
                print('Nomor data_karyawan tidak valid.')
        except ValueError:
            print('Masukkan nomor yang valid.')

    menu()



def exit():
    sys.exit()

def menu():
    print('\nMenu Utama Data Karyawan\n')
    print('1. Input data')
    print('2. Lihat data')
    print('3. Ubah data')
    print('4. Hapus data')
    print('5. Keluar\n')


    while True:
        try:
            pilihan = int(input('Masukkan Pilihan: '))
            break
        except Exception:
            print('Pilihan salah. Harap masukkan angka yang valid.')

    if pilihan == 1:
        create()
    elif pilihan == 2:
        read()
    elif pilihan == 3:
        update()
    elif pilihan == 4:
        delete()
    elif pilihan == 5:
        exit()
    



if __name__ == "__main__":
    menu()