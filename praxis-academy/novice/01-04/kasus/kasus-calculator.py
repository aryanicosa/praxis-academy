# membuat calculator bangun 2D untuk digunakan oleh object

from math import pi

class Calculator():
    def __init__(self, pengguna):
        self.pengguna = pengguna

    def luas_persegi(self, s):
        self.s = s
        val = self.s * self.s
        print("luas persegi = ", val)
        self.s = 0

    def keliling_persegi(self, s):
        self.s = s
        val = self.s * 4
        print("keliling persegi = ", val)
        self.s = 0

    def luas_lingkaran(self, r):
        self.r = r
        val = pi * self.r * self.r
        print("luas lingkaran = ", val)
        self.s = 0

    def keliling_lingkaran(self, r):
        self.r = r
        val = pi * 2 * self.r
        print("keliling lingkaran = ", val)
        self.r = 0
    
    def luas_segitiga_sama_sisi(self, s):
        self.s = s
        val = self.s * self.s * 0.5
        print("luas segitiga = ", val)
        self.s = 0
    
    def keliling_segitiga_sama_sisi(self, s):
        self.s = s
        val = 3 * self.s
        print("keliling segitiga = ", val)
        self.s = 0

calc_nama = Calculator("Hitung")
nama = input("Sape name lau?")
print("Selamat datang di program kalkulator sederhana " + nama + "\nsilakan :")

while True:
    print("1. luas persegi\n2. keliling persegi\n3. luas lingkaran\n4. keliling lingkaran")
    print("5. luas segitiga sama sisi\n6. keliling segitiga sama sisi")

    value = input()
    if value == "1":
        a = int(input("masukan nilai sisi : "))
        calc_nama.luas_persegi(a)
    elif value == "2":
        b = int(input("masukan nilai sisi : "))
        calc_nama.keliling_persegi(b)
    elif value == "3":
        c = int(input("masukan nilai jari-jari : "))
        calc_nama.luas_lingkaran(c)
    elif value == "4":
        d = int(input("masukan nilai jari-jari : "))
        calc_nama.keliling_lingkaran(d)
    elif value == "5":
        e = int(input("masukan nilai sisi : "))
        calc_nama.luas_segitiga_sama_sisi(e)
    elif value == "6":
        f = int(input("masukan nilai sisi : "))
        calc_nama.keliling_segitiga_sama_sisi(f)
    else:
        print("Salah angka brok!")

    loop = input("Hitung Lagi? (y/n)")
    if loop == "y":
        continue
    elif loop == "n":
        break
    else:
        print("jangan maen2 -__-")
        break
