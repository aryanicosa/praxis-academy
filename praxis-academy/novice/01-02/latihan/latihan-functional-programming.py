# poin utama kelebihan functional programming adalah "the absence of side effect"
# artinya tidak bergantung pada data diluar fungsi dan tidak merubah data yang ada diluar fungsi

'''
kelebihan penerapan fungsional programming
- minim bug, karena setiap komponen diisolasi
- hemat baris kode
- penguraian problem kedalam satu set fungsi
- hanya mengambil input dan memproduksi output 
- modular
- formal provability
- 
'''

# menguji iterator
L = [1, 2, 3]
it = iter(L)
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
# print(it.__next__()) # akan menghasilkan error karena tidak ada lagi next komponen atau StopIteration()

# cara diatas sama dengan menggunakan fungsi for berikut
for i in L:
    print(i)

# pada python, iter() dapat digunakan pada list, tuple, dictionaries dan mengubah material struktur data
# contoh pada dictionaries, yang akan dikembalikan hanyalah key
m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
     'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
month = iter(m)
print(month)
print(month.__next__())
print(month.__next__())

# masih ada banyak lagi function yang dapat digunakan untuk functional programming
# latihan di file selanjutnya