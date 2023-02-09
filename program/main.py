from view.view_nilai import *

class main(view):
    def __init__(self):
            print("Program Input Nilai")
            print("="*19)
            self.input_data()
            while True:
                c = input("\n(T)ambah, (L)ihat, (U)bah, (H)apus, (C)ari, (K)eluar: ")
                if c.lower() == 't':
                    self.tambah_data()
                elif c.lower() == 'l':
                    self.cetak_daftar_nilai()
                elif c.lower() == 'u':
                    self.ubah_data()
                elif c.lower() == 'h':
                    self.hapus_data()
                elif c.lower() == 'c':
                    self.cari_data()
                elif c. lower() == 'k':
                    print("\n|====================================|")
                    print("|             TERIMAKASIH            |")
                    print("|====================================|")
                    break
                else:
                    print("Pilih menu yang tersedia")

try:
    run = main()
except KeyboardInterrupt:
    print("\n|====================================|")
    print("|             TERIMAKASIH            |")
    print("|====================================|")
