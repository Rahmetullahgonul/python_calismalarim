'''
ogrenciler={
    378:{
        'name':'Rahmetullah',
        'surname':'Gonul',
        'phone number':12345
    },
    400:{
        'name':'Hasan Fatih',
        'surname':'Topal',
        'phone number':54321
    },
    450:{
        'name':'Omer Tarik',
        'surname':'asci',
        'phone number':67890
    }

}
'''

#1- bilgileri verilen ogrencileri kullanicidan aldiginiz bilgilerle dictionaryde sakla

ilk_ogrenci=int(input('ilk ogrenci numarasini girin:'))
ikinci_ogrenci=int(input('ikinci ogrenci numarasini girsin:'))
ucuncu_ogrenci=int(input('ucuncu ogrenci numarasini girsin:'))

ogrenciler={
    ilk_ogrenci:{
        'name':input('ilk ogrencinin adini gir:'),
        'surname':input('ilk ogrencinin soyadini gir:'),
        'phone number':int(input('ilk ogrencinin telefon numarasini gir:')),
        'student number':ilk_ogrenci
    },
    ikinci_ogrenci:{
        'name':input('ikinci ogrencinin adini gir:'),
        'surname':input('ikinci ogrencinin soyadini gir:'),
        'phone number':int(input('ikinci ogrencinin telefon numarasini gir:')),
        'student number':ikinci_ogrenci
    },
    ucuncu_ogrenci:{
        'name':input('ucuncu ogrencinin adini gir:'),
        'surname':input('ucuncu ogrencinin soyadini gir:'),
        'phone number':int(input('ucuncu ogrencinin telefon numarasini gir:')),
        'student number':ucuncu_ogrenci
    }
}

#2- ogrenci numarasini kullanicidan alip ilgili ogrencinin bilgilerini goster
hangi_ogrenci=int(input('hangi ogrencinin bilgilerini gormek istiyosan ogrenci numarasini yaz:'))
print(ogrenciler[hangi_ogrenci])
