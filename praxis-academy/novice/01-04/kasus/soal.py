'''
Buat suatu variabel a dan b, dimana a dan b adalah nilai bertipe data numeric
Berikan suatu nilai bertipe data integer, hasil pembagian dari a dengan b
Berikan suatu nilai bertipe data float, hasil pembagian dari a dengan b

masukan nama depan kamu kedalam suatu variable firstname
masukan nama belakang kamu kedalam suatu variable lasname
tampilkan suatu kalimat 'Hello Praxis, saya firstname lastname! saya siap belajar enterprise python developer.'

lengkapi code berikut
p = 9.99999
q = 'the number: '
print(.....)

jawaban the number : 9.99999
'''

def pembagianInt(a=0, b=0):
    return int(a / b)

def pembagianFloat(a, b):
    return float(a / b)

a = 10
b = 3
print("pembagian dengan hasil integer: ", pembagianInt(a,b))
print("pembagian dengan hasil float  : ", pembagianFloat(a,b))

firsname = "Arya"
lastname = "Nicosa"
print('Hello Praxis, saya {} {}! saya siap belajar enterprise python developer.'.format(firsname,lastname))

p = 9.99999
q = 'the number : '
print(q, p)