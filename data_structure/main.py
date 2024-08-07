from student_record import Record
isOn = True

mahasiswa_informatika = Record()

while(isOn):
    print("1. Tambah\n2. Hapus\n3. Tampilkan\n4. Keluar")

    menu = int(input("Pilih menu: "))
    
    if menu == 1:
        nama = input('Nama: ')
        npm = input('NPM: ')
        tempat_lahir = input('Tempat Lahir: ')
        tanggal_lahir = input('Tanggal Lahir: ')
        prodi = input('Prodi: ')
        mahasiswa_informatika.addStudent(nama=nama, npm=npm, tempat_lahir=tempat_lahir, tanggal_lahir=tanggal_lahir, prodi=prodi)
    elif menu == 2:
        mahasiswa_informatika.deleteStudent()
    elif menu == 3:
        mahasiswa_informatika.printRecord()
    elif menu == 4:
        break
    else:
        print("Menu tidak ada")