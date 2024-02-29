from audioop import reverse


sayılar = [1,3,5,7,9,12,19,21]

# 1 sayılar listesini while ile ekrana yazdır 
# 2 başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdır 
# 3 1-100 arasındaki sayıları azalan şekilde yazdır 
# 4 kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bi şekilde yazdır 
# 5 kullanıcıdan alacağınız sınırısz ürün bilgisini ürünler içinde sakla 
# ** ürün sayısını kullanıcıya sorun 
# ** dictionary listesi yapısı (name, price) şeklinde olsun 
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listele



# 1
# x = 1

# while x <= 21:
#     if(x %2 == 1):
#         print(x)
#     x = x + 1    



#2
# baslangıc =int(input('başlangıç: '))
# bitis = int(input('bitiş :'))

# i = baslangıc

# while i < bitis:
#     print(i)
#     i =i + 1



# 3
# i = 100
# while i > 0:
#     print(i)
#     i = i -1




#  4
# sayilar = []
# i = 0
# while i<5:     # beş tane değer istediğimiz için döngüyü beş kez çalıştırıyo
#     sayı =int(input('sayılar :'))
#     sayilar.append(sayı)
#     i += 1
# sayilar.sort()
# print(sayilar)    



# 5
# urunler = []
# urunAdet =int(input('kaç adet ürün ekliceksiniz: '))

# i = 0
# while i < urunAdet:
#     name = input('ürün ismi: ')
#     price = input('ürün fiyatı: ')
#     urunler.append({
#         'name': name,
#         'price':price
#     })
#     i += 1


# for urun in urunler:
#     print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')