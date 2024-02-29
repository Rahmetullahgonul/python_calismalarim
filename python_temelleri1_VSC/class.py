# # class

# class Person: #classa vericeğimiz isim genelde büyük harfle başlar
#     pass # boş bi class tanımlamak için kullandık
#     # class attributes
#     adress = 'no information' # her zaman kullanılmayan parametre

#     # construcator (yapıcı metod)
#     def __init__(self, name, year):

#         # object attributes
#         self.name = name # mutlaka tanımlanması gereken parametre
#         self.year = year # mutlaka tanımlanması gereken parametre
#         print('init metodu çalıştı')

#     # methods
#     def intro(self):
#         print('hello there ı am ' + self.name )

#     def calculateAge(self):
#         return 2022 - self.year



# # objecti (instance)
# p1 = Person(name = 'ali',year = 1968)    # objeleri de küçük harfle tanımlıyoruz
# p2 = Person('Rahmetullah',2001)          # parametreleri isteğe bağlı olarak yazabiliriz okunurluğ daha iyi olur 

# # updating
# p1.name = 'ahmet' # değişkeni değiştirme
# p1.adress = 'kocaeli'
# p2.adress ='istanbul'
# # accessing object attribtes
# print(f'p1 : name : {p1.name} year : {p1.year} adress : {p1.adress}')
# print(f'p2 : name : {p2.name} year : {p2.year} adress : {p2.adress}')

# print(p1)
# print(p2)
# print(type(p1))
# print(type(p2))
# print(p1 == p2)

# p1.intro()
# p2.intro()

# print(f'adım : {p1.name} ve yaşım: {p1.calculateAge()}')
# print(f'adım : {p2.name} ve yaşım: {p2.calculateAge()}')






# class Circle:
#     # class object attribute
#     pi = 3.14

#     def __init__(self, yarıcap=1): # eğerki yarıçap belirtilmezse 1 değeri atansın
#         self.yarıcap = yarıcap

#     def cevre_hesapla(self):
#         return (2*self.pi*self.yarıcap)

#     def alan_hesapla(self):
#         return (self.pi * (self.yarıcap**2))


# c1 = Circle() # yarıçap belirtmezseninz 1 e eşitlenir
# c2 = Circle(2)
# c3 = Circle(6)

# print(f'1.çemberin yarıçapı : {c1.alan_hesapla()} ve çevresi : {c1.cevre_hesapla()}')
# print(f'2.çemberin yarıçapı : {c2.alan_hesapla()} ve çevresi : {c2.cevre_hesapla()}')
# print(f'3.çemberin yarıçapı : {c3.alan_hesapla()} ve çevresi : {c3.cevre_hesapla()}')



                # KENDİ DENEMEM

class Ucgen:

    def __init__(self,kenar1, kenar2, tabanKenar, yukseklık):
        self.kenar1 = kenar1
        self.kenar2 = kenar2
        self.tabanKenar = tabanKenar
        self.yukseklık = yukseklık

    def cevre_hesaplama(self):
        return (self.kenar1 + self.kenar2 + self.tabanKenar)

    def alan_hesaplama(self):
        return ((self.tabanKenar*self.yukseklık)/2)

u1 = Ucgen(5,12,13,7)
print(f'üçgenini alanı: {u1.alan_hesaplama()} üçgenin çevresi: {u1.cevre_hesaplama()}')