class Student :
    def __init__(self, nama: str, npm: str, tempat_lahir: str, tanggal_lahir: int, prodi: str) -> None:
        self.nama = nama
        self.npm = npm
        self.tempat_lahir = tempat_lahir
        self.tanggal_lahir = tanggal_lahir
        self.prodi = prodi

class Record :
    def __init__(self) -> None:
        self.records: Student = []

    def addStudent(self, nama, npm, tempat_lahir, tanggal_lahir, prodi):
        newStudent = Student(nama, npm, tempat_lahir, tanggal_lahir, prodi)
        self.records.append(newStudent)

    def deleteStudent(self):
        self.records.pop()

    def printRecord(self):
        print(self.records)

