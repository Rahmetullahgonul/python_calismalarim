'''
1-100 arasinda rastgele uretilecek bir sayiyi asagi yukari ifadeleri ile buldurmaya calisin
random modulu kullan
100 uzerinden puanlama yapin hak bilgisini kullanicidan alin ve ona her soru belirtilen
can sayisi uzerinden puanlansin
'''

print("tahmin bilmece oyununa hosgeldiniz 1-100 arasindaki sayiyi bulmaya calisacaksiniz")
import random
hak_adet=int(input("kac adet hakkiniz olsun:"))
tutulan_sayi=random.randint(1,100)
#print(f"tutulan sayi {tutulan_sayi}")#admin gorur sadece
kacinci_tahmini=1
denenen_sayi=0
sayac=1
basari=0
puanlama_icin=hak_adet


while(hak_adet>0):
    print(f"{sayac}.tahmininiz:")
    denenen_sayi=int(input(""))
    if(denenen_sayi==tutulan_sayi):
        print("dogru tahmin")
        basari=1
        break
    elif(tutulan_sayi>denenen_sayi):
        print("daha yukari")
        basari=0
    elif(tutulan_sayi<denenen_sayi):
        print("daha asagi")
        basari=0
    hak_adet-=1
    sayac+=1


puan=(100/puanlama_icin)*(puanlama_icin-sayac)

if(basari==1):
    print(f"tebrikler oyuna {puanlama_icin} adet tahmin hakkiyla baslayip {sayac}.hakkinizda bildiniz ve oyunu {puan} puan ile bitirdiniz")
elif(basari==0):
    print("maalesef hic dogru tahminde bulunamadiniz")
