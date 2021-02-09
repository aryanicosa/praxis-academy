#latihan membuat sebuah class dan objectnya

class Rumah():
    #instance attribute
    def __init__(self, bahan, harga, lokasi):
        #self adalah instance dari sebuah class
        self.bahan = bahan
        self.harga = harga
        self.lokasi = lokasi

#membuat sebuah object, assign argumen untuk paramter Rumah
rumah1 = Rumah("kayu", 2000, "bantul")
rumah2 = Rumah("beton", 4000, "jogja")

print(rumah1) # output <__main__.Rumah object at 0x7f56621e0df0>
# output diatas menunujukkan bahwa ada sebuah object pada alamat tersebut dalam memory komputer

# mengakses atribut
print(rumah1.bahan)

# mencetak semua atribut dari sebuah object menggunakan obj.__dict__
print(rumah2.__dict__)  # bentuknya akan muncul menjadi sebuah dictionaries

# encapsulasi pada python
class Halo():
    def __init__(self, angka):
        self.a = 123
        self._b = 456 # private tapi masih bisa diakses melalui sebuah perintah, kecuali konvensi
        self.__c = 789 # private, sulit diakses, namun masih memungkinkan

halo = Halo("angka")
print(halo.a)
print(halo._b)
# print(halo.__c) # ini akan error karena strict private

# memanfaatkan setter dan getter untuk mengubah nilai dan mengambil nilai private variabel
class Software():
    #instance attribut
    def __init__(self):
        self.__version = 1.0
    
    #instance methode
    def get_version(self):
        print(self.__version)
    
    def set_version(self, version):
        self.__version = version

#instansiate object Software
obj = Software()
obj.get_version()
obj.set_version(1.1)
obj.get_version()

# single imheritance

# parent class
print("Single inheritance\n")
class Hewan():
    def bicara(self):
        print("hewan berbicara")

#child class Hewan
class Kucing(Hewan):
    def meow(self):
        print("meow.....")

k = Kucing()
k.meow()
k.bicara()

# hirarchical inheritance
# menurunkan lebih dari satu anak kelas
print("\n\nhirarchical inheritance\n")
class Burung(Hewan):
    def suit(self):
        print("swit swit....")

b = Burung()
b.bicara()
b.suit()

# multilevel inheritance
# kelas ini adalah anak kelas dari Kucing
print("\n\nmultilevel inheritance\n")
class AnakKucing(Kucing):
    def minum(self):
        print("minum susu")

a_k = AnakKucing()
a_k.bicara()
a_k.meow()
a_k.minum()

# multiple inheritance
print("\n\multiple inheritance\n")
#parent 1
class Perhitungan1():
    def penjumlahan(self, a, b):
        return a+b

#parent 2
class Perhitungan2():
    def pengurangan(self, a, b):
        return a-b

#child
class Child(Perhitungan1, Perhitungan2):
    def pembagian(self, a, b):
        return a/b

c = Child()

print(c.penjumlahan(10,20))
print(c.pengurangan(30,10))
print(c.pembagian(30,3))

# Abstraction, meyembunyikan detail yang tidak terlalu penting
# modul ABC (abstraction Based Class)
from abc import ABC, abstractmethod
class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        return self.__sisi * self.__sisi

    @abstractmethod
    def keliling(self):
        return self.__sisi * 4
    
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.__sisi = sisi
    def luas(self):
        return self.__sisi * self.__sisi
    def keliling(self):
        return self.__sisi * 4

persegi = Persegi(6)
print(persegi.luas())
print(persegi.keliling())        

# polymorphism dengan function dan object
print("\n\nPolymorphism dengan function object\n")
class Tomato():
    def type(self):
        print("Vegetable")
    def color(self):
        print("Red")

class Apple():
    def type(self):
        print("Fruit")
    def color(self):
        print("Red")

def func(obj):
    obj.type()
    obj.color()

obj_tomato = Tomato()
obj_apple = Apple()
func(obj_tomato)
func(obj_apple)


print("\n\nPolymorphism dengan class\n")
# dengan polymorpohism class, kita dapat membuat fungsi dengan nama yang sama pada kelas yang berbeda

class Kucing():
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("meow")

class Dog():
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("guk guk")

kucing1 = Kucing("persia", 18)
dog1 = Dog("bulder", 20)

for hewan in (kucing1, dog1):
    hewan.bersuara()


print("\n\nPolymorphism dengan inheritance\n")
#metode dibawah ini adalah overridiing, dimana fungsi terbang() milik parent class
# ditimpa oleh masing2 metode terbang() dari child class

class Burung():
    def intro(self):
        print("Ada beberapa type burung, ada yang bisa terbang dan ada yang tidak bisa")

    def terbang(self):
        print("hampir semua bisa terbang, tapi ada yang tidak bisa kuga")

class Elang(Burung):
    def terbang(self):
        print("elang bisa terbang")

class BurungUnta(Burung):
    def terbang(self):
        print("Burung unta tidak bisa terbang")

obj_burung = Burung()
obj_elang = Elang()
obj_burung_unta = BurungUnta()

obj_burung.intro()
obj_burung.terbang()

obj_elang.intro()
obj_elang.terbang()

obj_burung_unta.intro()
obj_burung_unta.terbang()
