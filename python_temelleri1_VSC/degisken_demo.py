'''
1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz 

müşteri adı
müşteri soyadı
müşteri adı + soyadı
müşteri cinsiyeti
müşteri tc kimlik no
müşteri doğum yılı 
müşteri adres bilgisi
müşteri yaşı

'''


name = 'Ahmet'
lastName = ' Gönül'
#name, lastName =(name + lastName) #burda hata var, doğrusu nameLastName = 'Ahmet Gönül'
sex = 'male'
ıdentity = '123456' #hesaplamada kullanılmıyacağı için sayı olarak almamakta fayda var
birth = 1968
adress = 'Başakşehir'
age = 54 # veya (2022 - birth) diyebilirsin
print(name, lastName, sex, ıdentity, birth, adress, age)


'''
2- aşağıdaki siparişlerin toplam bilgisini hesaplayınız

sipariş 1 = 110 tl
sipariş 2 = 1100.5 tl
sipariş 3 = 356.95 tl
'''
print(110 + 1100.5 + 356.95) #veya

order1 = 110
order2 = 1100.5
order3 = 356.95

print(order1 + order2 + order3) #veya

total = order1 + order2 + order3

print(total)