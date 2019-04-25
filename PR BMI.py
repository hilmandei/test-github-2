# Menghitung nilai BMI

beratbadan = int(input('masukin berat badan (kg): '))
tinggibadan = int(input('masukkin tinggi badan (cm): '))
tinggimeter = tinggibadan/100

BMI = beratbadan/(tinggimeter**2)
z = round(BMI)

if BMI >= 30 :
    print('BMI anda adalah =', z, 'anda obesitas, silahkan diet')

elif BMI >= 25 and BMI < 30 :
    print('BMI anda adalah =', z, 'anda kelebihan berat badan, silahkan diet')

elif BMI >= 18.5 and BMI < 25 :
    print('BMI anda adalah =', z, 'anda sudah normal')

else :
    print('BMI anda adalah =', z, 'anda kekurangan berat badan')