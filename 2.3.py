print('''Not Hesaplama

Bilgilendirme:

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF''')

a = int(input('vize1:'))
b = int(input('vize2:'))
c = int(input('final:'))
t = (a * 30 / 100) + (b * 30 / 100) + (c * 40 / 100)
t = int(t)
print('toplam notunuz:{}'.format(t))

if t >= 90:
    print('AA')
elif t >= 85:
    print('BA')
elif t >= 80:
    print('BB')
elif t >= 75:
    print('CB')
elif t >= 70:
    print('CC')
elif t >= 65:
    print('DC')
elif t >= 60:
    print('DD')
elif t >= 55:
    print('FD')
elif t < 50:
    print('FF')
