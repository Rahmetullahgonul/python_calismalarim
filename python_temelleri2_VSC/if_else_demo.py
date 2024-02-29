#1- kullanicidan isim tas ve egitim bilgilerine isteyip ehliyet alabilme durumunu kontrol edin
# ehliyet alma kosulunu en az 18 ve egitim durumu lise veya uni olmali

'''
name=input("isminiz:")
age=int(input("yasiniz:"))
school=input("egitiminiz:")

if(age>=18):
    if(school=='lise'or school=='universite'):
        print("ehliyet alabilirsiniz")
    else:
        print("ehliyet alamazsiniz")
else:
    print("ehliyet alamazsiniz")
    '''

#2- bir ogrenicinin 2 yazili bir sozlu notunu alip hesaplanan ortalamaya gore not araligina
# karsilik gelen not bilgisini yazdir
# 0-24=0
# 25-44=1
# 45-54=2
# 55-69=3
# 70-84=4
# 85-100=5

'''
ilk_sinav=int(input("ilk yazili notunuz:"))
ikinci_sinav=int(input("ikinci yazili notunuz:"))
sozlu=int(input("sozlu notunuz:"))

ortalama=(ilk_sinav+ikinci_sinav+sozlu)/3

if ortalama<=24:
    print(f"ortalamaniz {ortalama} ve notunuz 0")
elif ortalama>=25 and ortalama<=44:
    print(f"ortalamaniz {ortalama} ve notunuz 1")
elif ortalama>=45 and ortalama<=54:
    print(f"ortalamaniz {ortalama} ve notunuz 2")
elif ortalama>=55 and ortalama<=69:
    print(f"ortalamaniz {ortalama} ve notunuz 3")
elif ortalama>=70 and ortalama<=84:
    print(f"ortalamaniz {ortalama} ve notunuz 1")
elif ortalama>=85:
    print(f"ortalamaniz {ortalama} ve notunuz 5")
else:
    print("hatali bir giris yaptiniz")
    '''

#3- trafige cikis tarihi alinan bir aracin servis zamani asagidaki bilgilere gore hesapla
# 1.bakim=>1.yil 
# 2.bakim=>2.yil 
# 3.bakim=>3.yil
#süre hesabini alinan gun ay ve yila gore yap datetime modulunu kullan

import datetime

gunumuz = datetime.datetime(2023, 7, 8)
arac_cikis = input('aracin yola cikis tarihini girin (yil,ay,gün): ')
arac_cikis_yil, arac_cikis_ay, arac_cikis_gun = map(int, arac_cikis.split(','))
arac_cikis_tarih = datetime.datetime(arac_cikis_yil, arac_cikis_ay, arac_cikis_gun)

fark = gunumuz - arac_cikis_tarih

if fark.days <= 365:
    print(f"arac {fark.days} gündür trafikte ({fark.days/365} yildir) aracin ilk bakim dönemi")
elif 365 < fark.days < 365 * 2:
    print(f"arac {fark.days} gündür trafikte ({fark.days/365} yildir) aracin ikinci bakim dönemi")
elif 365*2 <= fark.days < 365*3:
    print(f"arac {fark.days} gündür trafikte ({fark.days/365} yildir) aracin üçüncü bakim dönemi")
elif fark.days >= 365*3:
    print(f"arac {fark.days} gündür trafikte ({fark.days/365} yildir) aracin en az 4. bakim dönemi")
else:
    print("hatali giriş yaptiniz, lütfen tekrar giriniz")
    
