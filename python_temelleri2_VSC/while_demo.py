sayilar =[1,3,5,7,9,12,19,21]

#1- sayilar listesini while ile ekrana bas

'''
sayi_adet=len(sayilar)
i=0
while sayi_adet>0:
    print(sayilar[i])
    sayi_adet-=1
    i+=1
    '''

#2- baslangic ve bitis degerlerini kullanicidan alip aradaki tum tek sayilari yazdir

'''
basla=int(input("baslangic degerini giriniz:"))
bit=int(input("bitis degerini giriniz:"))

while(bit>=basla):
    if(basla%2!=0):
        print(f"tek sayi bulundu : {basla}")
    basla+=1
'''

#3- 1-100 arasindaki sayilari azalan sekilde yazin

'''
i=100
while(i>=1):
    print(i)
    i-=1
    '''

#4- kullanicidan alacaginiz 5 sayiyi ekranda buyukten kucuge dogru sirali bi sekilde yazidirin

'''
i=5
sayilar=[]

while i>=1:
    sayilar.append(int(input("lutfen sayi giriniz:")))
    i-=1

sayilar.sort(reverse=True)
for sayi in sayilar:
    print(sayi)
'''

# kullanicidan alacaginiz sinirsiz urun bilgisini urunler listesi icinde saklayin
#urun sayisini kullaniciya sorun 
# dictionary yapın (name,price) seklinde 
# urun ekleme islemi bitince urunleri while ile listele


urunler=[]

adet=int(input('kac adet urun giriceksin:'))
i=0

while(adet>i):
    name=input("urun ismi:")
    price=input("urun fiyati:")
    urunler.append({
        'name':name,'price':price
    })
    i+=1
print(urunler)