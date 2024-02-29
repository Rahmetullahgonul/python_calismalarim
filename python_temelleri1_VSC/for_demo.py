sayılar = [1,3,5,7,9,12,19,21]

#1 sayılar listesindeki hangi sayılar 3 ün katıdır
#2 sayılar listesindeki sayıların toplamı kaçtır
#3 sayılar listesindeki tek sayıların karesini alınız


#1
for num in sayılar:
    if(num %3 == 0):
        print(num)


#2
result = sum(sayılar)
print(result)

# veya döngüyle yapılrısa

toplam = 0
for sayı in sayılar:
    toplam = toplam + sayı
    print(toplam)




#3
for numbers in sayılar:
    if(numbers %2 == 1):
        print(numbers**2)





sehirler = ['Kocaeli','İstanbul','Ankara','İzmir','Rize']

#4 şehirlerden hangileri en fazla 5 karakterlidir

for cities in sehirler:
    if(len(cities)<=5):
        print(cities)



urunler = [
    {'name':'samsung s6','price': '3000'},
    {'name':'samsung s7','price': '4000'},
    {'name':'samsung s8','price': '5000'},
    {'name':'samsung s9','price': '6000'},
    {'name':'samsung s10','price': '7000'}
]


#5 urunlerin fiyatları toplamı kaçtır
#6 urunlerın fıyatı en fazla 5000 olan ürünleri gösteriniz


# 5
# toplam = 0
# for urun in urunler:
#     fiyat = (urun['price'])
#     fiyat = int(fiyat)
#     toplam = toplam + fiyat
#     print(toplam)


 
# 6
# for urun in urunler:
#     if(int(urun['price']) <= 5000):
#         print(urun['name'])