#membuat file csv tanpa dict


import csv

mydata = []

with open('./../8.4.2019/karyawan.csv', 'r') as filegw :
    baca = csv.reader(filegw)
    #print(baca)                 #jika langsung dibaca maka ga akan keluar
    for i in baca:
        mydata.append(i)

print('masih dalam bentuk list :\n', mydata)

print(len(mydata[0]))

mydata2 = []

for j in range(len(mydata)-1):

    dx = {

    }
    for k in range(len(mydata[0])):
        dx[mydata[0][k]] = mydata[j + 1][k]


    print(dx)
    mydata2.append(dx)

print('\nini dalam bentuk dictionary :\n', mydata2)


