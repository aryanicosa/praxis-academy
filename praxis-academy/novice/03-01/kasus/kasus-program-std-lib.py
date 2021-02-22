from datetime import date

class User():
    def __init__(self, nama, status):
        self.nama = nama
        self.status = status

class Siswa(User):
    
    def tanggal_masuk(self):
        return date.today()
    
    def data_kelas(self, data_kelas):
        self.data_kelas = data_kelas

    def data_siswa(self):
        print(self.nama)
        print(self.status)
        print(self.data_kelas)

class Admin(User):
    def cek_data(self):
        print(self.nama)
        print(self.status)

adm = Admin("arya", "guru")
sis = Siswa("nicosa", "siswa")
sis.data_kelas("python")

sis.data_siswa()
print(sis.tanggal_masuk())

adm.cek_data()