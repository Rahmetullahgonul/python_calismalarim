#1 girilen 2 sayidan hangisi buyuk
'''
sayi1=int(input("1.sayi:"))
sayi2=int(input("2.sayi"))
if sayi1>sayi2:
    print(f"1.sayi daha buyuk=>:{sayi1}")
elif sayi2>sayi1:
    print(f"2.sayi daha buyuk=>:{sayi2}")
else:
    print(f"sayilar birbirine esittir =>:{sayi1}={sayi2}")
'''

#2 kullanicidan 2 vize(%60) ve final(%40) notunu alip ort hesapla
'''
vize1=int(input("1.vize:"))
vize2=int(input("2.vize:"))
final=int(input("final:"))
ortlama=(((vize1/10)*3)+((vize2/10)*3)+((final/10)*4))

print(ortlama)
'''

#3 girilen bir sayinin negatif pozitif durumuna bakin
'''
sayi=int(input("bir sayi girin:"))
if sayi>0:
    print("sayi pozitif")
elif sayi<0:
    print("sayi negatif")
else:
    print("sayi sifirdir")
    '''

#4 girilen bir sayinin teklik ciftligine bakin
'''
sayi=int(input("bir sayi girin:"))
if sayi%2==0:
    print("sayi cift")
else:
    print("sayi tek")
    '''


#5 parola ve mail bilgisini isteyip dogrulugunu kontrol edin
mail='rahmet'
password='123'


if mail==input("lutfen mail adresinizi girin:") and password==input("lutfen sifrenizi girin:"):
    print("islem dogru")
else:
    print("hatali girdiniz")