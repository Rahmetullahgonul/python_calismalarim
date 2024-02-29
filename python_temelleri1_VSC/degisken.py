from msvcrt import kbhit


maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

#print(5000 - (5000*0.27))
#print(4000 - (4000*0.27))


# Değişken tanımla kuralları 

# rakam ile başlayamaz. 1number = 10 olamaz
# aynı değişken ismini iki kez kullanamayız. number = 10 varken number = 20 kullanılamaz
# number = 20 olsun number += 30 dersek 50 sonucu çıkar
number = 20 
number += 30 
print(number)

# büyük küçük harf duyarlılığı vardır
age = 55
AGE = 45 
print(age)
print(AGE)

# türkçe karakter kullanmayalım yaş yerine yas veya age olarak kullanalım

x = 1                  #int
y = 2.3                #float
name ='Çınar'          #string  
isStudent = True       #bool

a = '10'
b = '20'
print(a+b) # 30 => 1020 

firstName = 'Sadık' 
lastName = ' Turan'

print(firstName + lastName) # Sadık Turan 

x, y, name, isStudent = (1, 2.3, 'Çınar', True) #üstteki bilgileri tek satıra kodlama 