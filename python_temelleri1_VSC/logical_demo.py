# 1 girilen bir sayının 0-100 arasında olup olmadığını kontol edin 
# 2 girilen bir sayının pozitif cift sayı olup olmadığını kontrol edin 
# 3 email ve parola bilgileri ile giriş kontrolü yapın 
# 4 girilen 3 sayıyı büyüklük olarak karşılaştırınız 

# 5 kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplayın 
# eğer ortalama 50 ve üstüyse geçti değilse kaldı yazdırın 
# a) ortalama 50 olsa bile final notu en az 50 olmalıdır 
# b) finalden 70 aldığında ortalamanın önemi kalmasın 

# 6 kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesapla 
# formül : (kilo / boy uzunluğu karesi)
# aşağıdaki tabloya göre kişi hangi gruba aittir 
# 0 - 18.4 = zayıf 
# 18.5 - 24.9 = normal 
# 25.0 - 29.9 = fazla kilolu 
# 30.0 - 34.9 = şişman 




# 1
# r =int(input('Sayı giriniz :'))
# result = (r < 100 ) and (r > 0)
# if(result == True):
#     print(f'Girdiğiniz {r} değeri sıfırla yüz arasındadır.')
# if(result != True):
#     print(f'Girdiğiniz {r} değeri sıfır yüz arasında değildir.')



# 2
# r = int(input('Bir sayı giriniz :'))
# result = (r > 0) and (r %2 == 0)
# if(result == True):
#     print(f'Girdiğiniz {r} değeri pozitif bir çift sayıdır.')
# if(result != True):
#     print(f'Girdiğiniz {r} değeri pozitif bir çift sayı değildir.')    




# 3
# mail = str(input('mail adresiniz : '))
# şifre = str(input('şifrenizi girin : '))
# email = 'comp'
# parola = '123'
# if(mail == email) and (şifre == parola):
#     print('Girdğiniz mail ve şifre doğrudur')
# if(mail != email) and (şifre == parola):
#     print('Girdiğiniz mail adresini bulamadık')
# if(mail == email) and (şifre != parola):
#     print('Girdiğiniz şifre bu mail adresi için doğru değildir')        
# if(mail != email) and (şifre != parola):
#     print('Böyle bi kullanıcı bulamadık') 





# 4
# a = float(input('1.sayı : '))
# b = float(input('2.sayı : '))
# c = float(input('3.sayı : '))
# if(a > b) and (a > c) and (b > c):
#     print(f'Girdiğiniz {a} değeri en büyük sayıdır,{c} ise en küçük sayıdır.')
# if(a > b) and (a > c) and (c > b):
#     print(f'Girdiğiniz {a} değeri en büyük sayıdır,{b} ise en küçük sayıdır.')
# if(b > a) and (b > c) and (a > c):
#     print(f'Girdiğiniz {b} değeri en büyük sayıdır,{c} ise en küçük sayıdır.') 
# if(b > a) and (b > c) and (c > a):
#     print(f'Girdiğiniz {b} değeri en büyük sayıdır,{a} ise en küçük sayıdır.') 
# if(c > a) and (c > b) and (a > b):
#     print(f'Girdiğiniz {c} değeri en büyük sayıdır,{a} ise en küçük sayıdır.')     
# if(c > a) and (c > b) and (b > a):
#     print(f'Girdiğiniz {c} değeri en büyük sayıdır,{b} ise en küçük sayıdır.')   




# 5
# vize1 = float(input('1.vize : '))
# vize2 = float(input('2.vize : '))
# final = float(input('final : '))
# ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final *0.4)

# if(ortalama > 50) and (final >= 50):
#     print(f'dersi {ortalama} ortalama ile geçtiniz ')
# if(ortalama < 50):
#     print(f'dersi {ortalama} ortalama ile geçemediniz')    
# if(ortalama > 50) and (final < 50):
#     print(f'Final notunuz 50 den düşük olduğu için ({final}) dersten kaldınız')
# if(final > 70):
#     print('dersten final notunuz {final} olduğu için')   # bu kod ikinci satırla çelişiyo 





# 6
# ad = str(input('isminiz : '))
# kilo = float(input('kilonuz : '))
# boy = float(input('boyunuz(metre cinsinden) : '))
# indeks = (kilo / (boy * boy))
# if(indeks > 0) and (18.4 > indeks):
#     print(f'vücut kitle endeksiniz {indeks}tir ve zayıf katagorisindesiniz')
# if(indeks > 18.5) and (24.9 > indeks):
#     print(f'vücut kitle endeksiniz {indeks}tir ve normal katagorisindesiniz')       
# if(indeks > 25.0) and (29.9 > indeks):
#     print(f'vücut kitle endeksiniz {indeks}tir ve fazla kilolu katagorisindesiniz')
# if(indeks > 30.0) and (34.9 > indeks):
#     print(f'vücut kitle endeksiniz {indeks}tir ve şişman(obez) katagorisindesiniz')