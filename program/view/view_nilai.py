from model.daftar_nilai import *
from view.input_nilai import *

class view(daftar,masuk):
    def cetak_daftar_nilai(self):
        if x.items():
            print("\nDaftar Nilai")
            print("="*78)
            print("|No. |      NAMA       |       NIM       |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
            print("="*78)
            i = 0
            for z in x.items():
                i += 1
                print("| {no:2d} | {0:15s}| {1:15d}  | {2:5d}   | {3:5d} |{4:6d} | {5:7.2f} |"
                    .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
            print("=" * 78)

        else:
            print("\nDaftar Nilai")
            print("="*78)
            print("|No. |      NAMA       |       NIM       |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
            print("="*78)
            print("|                                TIDAK ADA DATA                              |")
            print("="*78)

    def cetak_hasil_pencarian(self):
        if self.nama in x.keys():
            print("\nHasil Pencarian")
            print("="*78)
            print("|No. |      NAMA       |       NIM       |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
            print("="*78)
            i = 0
            for z in x.items():
                i += 1
                print("| {no:2d} | {0:15s}| {1:15d}  | {2:5d}   | {3:5d} |{4:6d} | {5:7.2f} |"
                    .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
            print("=" * 78)

        else:
            print("\nHasil Pencarian")
            print("="*78)
            print("|No. |      NAMA       |       NIM       |  TUGAS  |  UTS  |  UAS  |  AKHIR  |")
            print("="*78)
            print("|                                TIDAK ADA DATA                              |")
            print("="*78)
