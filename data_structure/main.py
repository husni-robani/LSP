from student_record import Record

mahasiswa_informatika = Record()

# add students
mahasiswa_informatika.addStudent(nama="Husni Robani", npm="0620101068", tempat_lahir="Garut", tanggal_lahir="5 mei 2001", prodi="Informatika")
mahasiswa_informatika.addStudent(nama="test", npm="test", tempat_lahir="test", tanggal_lahir="test", prodi="Informatika")

# print all students on record
mahasiswa_informatika.printRecord()

# delete last student
mahasiswa_informatika.deleteStudent()

mahasiswa_informatika.printRecord()