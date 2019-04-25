#membuat file csv tanpa dict


import csv

mydata = []

with open('./../8.4.2019/karyawan.csv', 'r') as filegw :
    baca = csv.reader(filegw)
    #print(baca)                 #jika langsung dibaca maka ga akan keluar
    for i in baca:
        mydata.append(i)

print('masih dalam bentuk list :\n', mydata)

print()

mydata2 = []

for j in range(len(mydata)-1):

    dx = {}
    dx[mydata[0][0]] = mydata[j + 1][0]
    dx[mydata[0][1]] = mydata[j + 1][1]
    dx[mydata[0][2]] = mydata[j + 1][2]

    print(dx)
    mydata2.append(dx)

print('\nini dalam bentuk dictionary :\n', mydata2)
print('\n-------view lain-------\n')
for x3 in mydata2:
    print('=================')
    #print(list(x3.values()))
    for y3 in x3:
        print(y3, ':', x3[y3])

