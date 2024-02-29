'''
1-100 arasında rastgale üretilcek bir sayıyı aşağı yukarı ifadelerle buldurmaya çalışın 
** random modülü için python random şeklinde arama yapın 
** 100 üzerinden puanlama yapın her soru 20 puan 
** hak bilgisi kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın
'''



'''
                            KENDİ DENEMEM

import random 
sayı = random.randint(1,100)
hak = int(input('kaç hakkın olsun: '))
print(sayı)

while 1 <= hak:
    if sayı > int(input('tahmin: ')):
        print('tahmininizi yükseltin')
    elif sayı < int(input('tahmin:')):
        print('alçalt')
    elif sayı == int(input('tahmin:')):
        print('doru')
    else:
        print('doğru değer gir')             
    hak = hak - 1  
'''    




import random

sayi = random.randint(1,100)
can = int(input('kaç hakkın olsun: '))
hak = can 
sayac = 0
print(sayi)
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin:'))

    if sayi == tahmin:
        print(f'tebrikler {sayac}.defada bildiniz ve puanınız {100 - ((100/can)*(sayac-1))}')
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')

    if hak == 0:
        print(f'hakkınız bitti, tutulan sayı {sayi} idi')