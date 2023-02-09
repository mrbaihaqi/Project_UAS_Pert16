x={}

class daftar():
    def tambah_data(self):
        try:
            print("\nTambah data")
            self.nama = input("Nama           : ")
            self.nim = int(input("NIM            : "))
            self.uts = int(input("Nilai UTS      : "))
            self.uas = int(input("Nilai UAS      : "))
            self.tugas = int(input("Nilai Tugas    : "))
            self.akhir = self.tugas*30/100 + self.uts*35/100 + self.uas*35/100
            x[self.nama] = self.nim, self.tugas, self.uts, self.uas, self.akhir
        except ValueError:
            print("\nMohon hanya masukan angka untuk NIM dan Nilai")
            print("=============================================")
            print("           GAGAL MENAMBAH DATA")
        
    def ubah_data(self):
        print("\nUbah Data")
        self.nama = input("Nama           : ")
        if self.nama in x.keys():
            try:
                print("\nData Ditemukan")
                print("==================")
                print("Ubah Menjadi\n")
                self.nama = input("Nama           : ")
                self.nim = int(input("NIM            : "))
                self.uts = int(input("Nilai UTS      : "))
                self.uas = int(input("Nilai UAS      : "))
                self.tugas = int(input("Nilai Tugas    : "))
                self.akhir = self.tugas*30/100 + self.uts*35/100 + self.uas*35/100
                x[self.nama] = self.nim, self.tugas, self.uts, self.uas, self.akhir
                del x[self.nama]
                print()
                print("|====================================|")
                print("|        BERHASIL MENGUBAH DATA      |")
                print("|====================================|")
            except ValueError:
                print("\nMohon hanya masukan angka untuk NIM dan Nilai")
                print("=============================================")
                print("           GAGAL MENGUBAH DATA")
                
        else:
            print("Nama {0} tidak ditemukan".format(self.nama))
    
    def hapus_data(self):
        print("\nHapus Data")
        self.nama = input("Masukan Nama    : ")
        if self.nama in x.keys():
            del x[self.nama]
            print()
            print("|====================================|")
            print("|       BERHASIL MENGHAPUS DATA      |")
            print("|====================================|")
        else:
            print("Nama {0} Tidak Ditemukan".format(self.nama))
    
    def cari_data(self):
        print("\nCari Data")
        self.nama = input("Nama\t\t\t: ")
        self.cetak_hasil_pencarian()
