export class Student {
  constructor(nama, npm, tempat_lahir, tanggal_lahir, prodi) {
    this.name = nama;
    this.npm = npm;
    this.tempat_lahir = tempat_lahir;
    this.tanggal_lahir = tanggal_lahir;
    this.prodi = prodi;
  }
}

export class Record {
  constructor() {
    this.records = [];
  }

  add(nama, npm, tempat_lahir, tanggal_lahir, prodi) {
    let newStudent = new Student(nama, npm, tempat_lahir, tanggal_lahir, prodi);
    this.records.push(newStudent);
    return;
  }

  delete() {
    this.records.pop();
  }

  print() {
    console.log(this.records);
  }
}
