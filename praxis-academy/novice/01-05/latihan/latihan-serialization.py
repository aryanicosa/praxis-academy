# serialization, merubah data ke format yang dapat disimpan/dibagikan.
# memungkinkan untuk dikembalikan kembali (deserialization)

# serialization process in python called "pickling"
# dengan pickling kita dapat mengkonversi tingkatan object ke binary format dan dapat disimpan
# contoh
import pickle

class Animal():
    def __init__(self, number_of_paws, color):
        self.number_of_paws = number_of_paws
        self.color = color

class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)

#step 1 create sheep Mary
mary = Sheep("white")
#print(str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_paws))

# step 2 : pickle Mary
my_pickled_mary  = pickle.dumps(mary) # pickling data

'''
# cek data hasil pickling
print("Would you like to see her pickled? Here she is!")
print(my_pickled_mary) # cetak data yang sudah di pickling
'''

'''
# membuat sebuah file binary
binary_file = open('my_pickled_mary.bin', mode='wb')
my_pickled_mary  = pickle.dump(mary, binary_file) # akan digunakan untuk cetak file binary
binary_file.close()
'''

# step 3 unpickle Mary and create new instance from clone/pickled data
dolly = pickle.loads(my_pickled_mary)

# create color for dolly to divers with mary
dolly.color = "black"

# step 4, cek hasil
print(str.format("Dolly is {0} ", dolly.color))
print(str.format("Mary is {0} ", mary.color))