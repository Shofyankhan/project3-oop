"""
OOP Program
"""
from Geometri.persegipanjang import PersegiPanjang
from Geometri.segitiga import Segitiga

p1 = PersegiPanjang(10, 3)
p1.info()
p1.hitung_luas()
print(p1.info())
print(f'hasil perhitungannya adalah {p1.hitung_luas()} :D')

print("\n")

s1 = Segitiga(20, 5)
s1.info()
s1.hitung_luas()
print(s1.info())
print(f'hasil perhitungannya adalah {s1.hitung_luas()} :D')

daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())