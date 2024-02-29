'''

ogrenciler = {
    '120' : {
        'ad' : 'Ali',
        'soayad' : 'Yılmaz',
        'telefon' : '532 000 00 01'
    },
    '125' : {
        'ad' : 'Can',
        'soyad' : 'Korkmaz',
        'telefon' : '532 000 00 02'  
    },
    '128' : {
        'ad' : 'Volkan',
        'soyad' : 'Yükselen',
        'telefon' : '532 000 00 03'
    },
}
'''

# 1 bilgileri verilen öğrencilerin kullanıcıdan aldığınız bilgilerle 
# dictionary içinde saklayın




# 2 öğrenci numarasını kullanıcadan alıp ilgili öğrenci bilgisini gösterin



ogrenciler = {}




number = input('öğrenci no:')
ad = input('öğrenci adı:')
soyad = input('öğrenci soyadı:')
telefon = input('öğrenci telefon no:')

# ogrenciler[number] = {
#     'ad' : ad,
#     'soyad' : soyad,
#     'telefon' : telefon
# }


# print(ogrenciler)

# veya

ogrenciler.update({
    number: {
        'ad': ad,
        'soyad': soyad,
        'telefon': telefon
    }
})


number = input('öğrenci no:')
ad = input('öğrenci adı:')
soyad = input('öğrenci soyadı:')
telefon = input('öğrenci telefon no:')

ogrenciler.update({
    number: {
        'ad': ad,
        'soyad': soyad,
        'telefon': telefon
    }
})

number = input('öğrenci no:')
ad = input('öğrenci adı:')
soyad = input('öğrenci soyadı:')
telefon = input('öğrenci telefon no:')

ogrenciler.update({
    number: {
        'ad': ad,
        'soyad': soyad,
        'telefon': telefon
    }
})


print(ogrenciler)


ogrNo = input('öğrenci no:')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)
