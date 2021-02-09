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
