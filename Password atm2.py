#Password ATM

x = 0
correct = 12345

while x < 3:
    password = int(input('Masukkin Password anda : '))
    if password == correct:
        print('password anda benar, Log in sukses !!')
        break
    else:
        x += 1
        if x < 3:
            print('Password anda masih salah, silahkan coba lagi, coba ke -', x)
        elif x == 3:
            print('Password semuanya salah, coba ke -', x)
            print('Anda sudah salah 3 kali, kartu terblokir')
#else :
    #print('Anda sudah salah 3 kali, kartu terblokir')


print('\n=============contoh lain============ \n')



