# 1 gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın 
# 2 kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yaz 
# 3 gönderilen 2 sayı arasındaki tüm asal sayıları bulun 
# 4 kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür



# 1
#             KENDİ DENEMEM
# tekrarSayisi =int(input('kaç kez yazdırmak istersiniz : '))

# def ltr(kelime):
#     print(ltr * tekrarSayisi)    
# ltr('rahmet')

                   # DOĞRUSU

# def yazdır(kelime,adet):
#     print(kelime * adet)

# yazdır('merhaba\n', 10)



# 2
#             KENDİ DENEMEM
# def add(a,b,c,*args, **kwargs):
#     print(a,b,c,args,kwargs)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
# add(100, 200, 300, 400, 500, 600, key1 = 'nbr hacı', key2 = 'ii sndn nbr')



# 2
               #  DOĞRUSU

# def listeyeCevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)

#     return liste

# result = listeyeCevir(1,2,3,4,5,6,8,'merhaba')
# print(result)





# 3
# def asalSayılarıBul(sayi1, sayi2):
#     for sayi in range(sayi1, sayi2+1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)  


# sayi1 = int(input('sayı 1:'))
# sayi2 = int(input('sayı 2:'))

# asalSayılarıBul(sayi1,sayi2)




# def tamBolenleriBul(sayi):
#     tamBolenler = []

#     for i in range(2, sayi):
#         if (sayi % i == 0):
#             tamBolenler.append(i)
#     return tamBolenler        

# print(tamBolenleriBul(20))