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