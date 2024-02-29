x,y,z =2,5,107

numbers=1,5,7,10,6

#1- kullanicidan aldiginiz 2 sayinin carpimi ile x,y,z toplaminin farki nedir
'''
sayi1=int(input("bir sayi girin:"))
sayi2=int(input("bir sayi daha girin:"))
print((sayi1*sayi2)-(x+y+z))
'''

#2- y'nin x'e kalansiz bolumunu hesapla

print(y//x)


#3-x,y ve z nin toplaminin mod 3 u nedir

print((x+y+z)%3)


#4- y nin x.kuvveti?

print(y**x)


#5- x,*y,z numbers islemine gore z nin kupu kactir

x,*y,z=numbers
print(z**3)


#6- x,*y, z = numbers islemine gore y nin degerleri toplami

x,*y,z=numbers
print(y[0]+y[1]+y[2])