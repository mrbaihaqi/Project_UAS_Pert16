from model.daftar_nilai import *

class masuk():
    def input_data(self):
        try:
            print("\nInput Data")
            self.nama = input("Nama           : ")
            self.nim = int(input("NIM            : "))
            self.uts = int(input("Nilai UTS      : "))
            self.uas = int(input("Nilai UAS      : "))
            self.tugas = int(input("Nilai Tugas    : "))
            self.akhir = self.tugas*30/100 + self.uts*35/100 + self.uas*35/100
            x[self.nama] = self.nim, self.tugas, self.uts, self.uas, self.akhir
        except ValueError:
            print("Mohon hanya masukan angka untuk NIM dan Nilai")
            self.input_data()
