'''

maasRahmet = 5000
maasAhmet = 4000
vergi = 0.27

print(maasRahmet-(maasRahmet*vergi))
print(maasAhmet-(maasAhmet*vergi))
'''

'''
degisken tanimlama kurallari:
* rakam ile baslayamaz
* degiskenin icine deger atmak zorundayiz 
* bir degisken ismine sadece tek deger atanabilir
* buyuk kucuk harf duyarliligi vardir
* turkce karakter kullanma
* metinsel tanimlamak icin name = 'rahmet' ya da name = "rahmet"

'''
"""
1- bir musterinin asagidaki bilgileri icin degisken olustur
adi 
soyadi
musteri ad + soyad
cinsiyet
tc kimlik
dogum yili 
adres
yasi
"""

ad,soyad,cinsiyet,tcno,yil,adres,yas=("Rahmetullah","gonul","erkek",123,2001,"istanbul",22)
ad_soyad=ad +' '+ soyad
print(ad_soyad)