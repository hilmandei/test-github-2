#membuat file json

import csv
import json

mydata = []

with open('./../8.4.2019/karyawan.csv', 'r') as filegw :
    baca = csv.DictReader(filegw)
    for i in baca:
        mydata.append(dict(i))

print('dalam bentuk dict :\n', mydata)

xx = json.dumps(mydata)
jsonku = open('karyawanjs.json', 'w')
jsonku.write(xx)
print('dalam bentuk json :\n', xx)

# with open('karyawanjs.json') as filegw2 :
#     data2 = json.load(filegw2)
#
# print(data2)