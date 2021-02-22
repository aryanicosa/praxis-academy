import csv

#input flat text internal
a = {"Type" : "A", "field1" : "value1", "field2" : "value2", "field3" : "value3"}

# input text dari file external
b = open('latihan-sample-file.py', 'r')

print("flat text internal dan external")
print(repr(a))
print(repr(b))


'''
with open('latihan-sample-file.py') as f:
    f.write(repr(a))
'''

#with open('latihan-sample-file.py', 'r') as f:inp = ast.literal_eval(f.read())

#membuka file csv
print("membuka file csv")
with open('latihan-sample-csv.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
f.close()

# menulis file csv, data lama akan tertimpa
data = ['6', 'umir', 'manao']
print("menulis file csv")
with open('latihan-sample-csv.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data) # data ini harus berupa nilai iterable agar rapi
f.close()

'''
ada banyak skema penggunaan serialisasi data, bisa menggunakan
- YAML (nested data)
- json (nested data)
- XML (nested data)
- pickle (nested data)
- binary (flat data)
'''