'''
soru : girilen bir sayının asal sayı olup olmadığını bulun
** asal sayılar sadece kendine ve 1 e tam bölünür
'''

sayi = int(input('sayı:'))
asalmi = True

if sayi == 1:
    asalmi = False 
    
for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print(f'{sayi} değeri asaldır')
else:
    print(f'{sayi} değeri asal değildir')    
