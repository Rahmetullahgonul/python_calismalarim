# 1- girilen bir sayi 0-100 arasinda mi
'''
sayi=int(input("bir sayi gir:"))
if sayi>=0 and sayi<=100:
    print(f"girdiginiz sayi 0-100 arasinda =>{sayi}")
else:
    print(f"girdiginiz sayi 0-100 arasinda degil =>{sayi}")
    '''

#2- girilen bir sayinin pozitif ve bir cift sayi oldugunu kontrol et
'''
sayi=int(input("bir sayi gir:"))
if sayi>0 and sayi%2==0:
    print(f"girdiginiz sayi pozitif ve cift =>{sayi}")
else:
    print(f"girdiginiz sayi pozitif ve cift degil")
    '''

#3- girilen 2 sayidan buyuk olani ekrana bas
'''
sayi1=int(input("ilk sayi:"))
sayi2=int(input("ikinci sayi:"))
if sayi1>sayi2:
    print(sayi1)
elif sayi2>sayi1:
    print(sayi2)
else:
    print(f"{sayi1}={sayi2}")
    '''

#4 kullanicidan 2 vize(60) 1 final(40) notlari al
#eger ortalama 50 ustu ise gecer degilse kaldi yaz (final min =50)
#finalden 70 alirsa ortalamayi bosver
'''
vize1=int(input("1.vize:"))
vize2=int(input("2.vize:"))
final=int(input("final:"))
ortalama=((vize1/10)*3)+((vize2/10)*3)+((final/10)*4)
if final>=70:
    print(f"ortalama {ortalama} gecer")
elif final>=50 and ortalama>=50:
    print(f"ortalama {ortalama} gecer")
else:
    print(f"ortalama {ortalama} kaldi")
    '''

#5 kisimim ad kilo ve boy bilgilerini alip vucut kitle hesapla 
# 0-18.4 zayif
# 18.5-24.9 normal
# 25.0-29.9 fazla kilo
# 30.0- sisman

isim=input("isminiz:")
kilo=int(input("kilonuz:"))
boy=int(input("boyunuz:"))
boys=((boy/100)*(boy/100))
vucutkitle=(kilo/boys)
if vucutkitle>0 and vucutkitle<=18.4:
    print(f"{isim} kilo:{kilo} boy:{boy}=> vucut kitle endeksi:{vucutkitle}====> zayif")
elif vucutkitle>=18.5 and vucutkitle<=24.9:
    print(f"{isim} kilo:{kilo} boy:{boy}=> vucut kitle endeksi:{vucutkitle}====> normal")
elif vucutkitle>=25 and vucutkitle<=29.9:
    print(f"{isim} kilo:{kilo} boy:{boy}=> vucut kitle endeksi:{vucutkitle}====> fazla kilolu")
elif vucutkitle>=30:
    print(f"{isim} kilo:{kilo} boy:{boy}=> vucut kitle endeksi:{vucutkitle}====> sisman(obez)")
# else:
#     print("islemler sirasinda hatali bir giris yaptiniz")
