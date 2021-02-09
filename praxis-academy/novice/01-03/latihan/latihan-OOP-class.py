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