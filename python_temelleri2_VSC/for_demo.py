sayilar = [1,3,5,7,9,12,19,21]

#1- sayilar dizisindeki hangi sayilar ucun bir katidir

'''
for i in sayilar:
    if(i%3==0):
        print(f"{i} sayisi ucun bir katidir")
        '''

#2- sayilar listesindeki sayilarin toplami kactir

'''
toplam = 0

for i in sayilar:
    toplam+=i

print(f"sayilar dizisindeki sayilarin toplami ={toplam}")
'''

#3- sayilar listesindeki tek sayilarin karasini aliniz

'''
for i in sayilar:
    if(i%2!=0):
        print(f"sayilar dizisindeki tek sayi ={i} ve karesi ={i**2}")
'''


sehirler=['kocaeli','istanbul','ankara','izmir','rize']
'''
#4- sehirlerden hangileri en fazla 5 karakterlidir
en_fazla_bes=[]

for i in sehirler:
        if len(i)<=5:
            en_fazla_bes.append(i)
print(en_fazla_bes)
'''

urunler=[
    {'name':'samsung s6','price':'3000'},
    {'name':'samsung s7','price':'4000'},
    {'name':'samsung s8','price':'5000'},
    {'name':'samsung s9','price':'6000'},
    {'name':'samsung s10','price':'7000'}
]

#5 urunlerin fiyatlari toplami kactir

'''
toplam_fiyat=0
for urun in urunler:
    toplam_fiyat+=int(urun['price'])
print(f"urunlerin toplam fiyati = {toplam_fiyat}")
'''

#5- urunlerden fiyati en fazla 5000 olan urunleri gosteriniz

'''
for urun in urunler:
    if(int(urun['price'])<=5000):
        print(urun['name'])
'''