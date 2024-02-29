# def sayHello(name):
#     print('hello ' + name) 

# sayHello('Rahmet') #print demene gerek yok, istediğin zaman çağırabilirsin



# def sayHello(name = 'user'): #parametre yoksa user yazar
#     print('Hello '+ name )   # parametre varsa o değişkeni yazdırır

# sayHello()




# def sayHello(name = 'user'):
#     return 'hello ' + name

# msg = sayHello('Rahmet')    

# print(msg)




# def total(num1, num2,):
#     return num1 + num2 

# result = total(10,20)
# print(result)    





def yasHesapla(birth):
    return 2022 - birth

ageRahmet = yasHesapla(2001)
ageFirdevs = yasHesapla(1998)
ageHatice = yasHesapla(2005)
ageZehra = yasHesapla(1975)
ageAhmet = yasHesapla(1968)   

print(ageAhmet)
print(ageZehra)
print(ageFirdevs)
print(ageRahmet)
print(ageHatice)


def emekliligeKacYılVar(birth , isim):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğe kaç yıl kaldı
    İNPUT: Doğum yılı
    OUTPUT: Hesaplanan yıl bilgisi  
    '''
    yas = yasHesapla(birth)
    emeklilik = 65 - yas 

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı ')
    else:
        print('zaten emeklisin')

emekliligeKacYılVar(1968, 'Ahmet')
emekliligeKacYılVar(1948, 'Ali')
emekliligeKacYılVar(2001, 'Rahmet')


print(help(emekliligeKacYılVar)) # kod içindeki bilgilendirme yazısı çıkar