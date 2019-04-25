#Password ATM

x = 0
correct = 12345

while x < 3:
    password = int(input('Masukkin Password anda : '))
    if password == correct:
        print('password anda benar, Log in sukses !!')
        break
    else :
        x += 1
        print('Password anda masih salah, silahkan coba lagi, coba ke -', x)
else :
    print('anda sudah salah 3 kali, kartu terblokir')


print('\n=============contoh lain============ \n')


