'''
class person:
    address='no information'

    def __init__(self,name ,year ):
        self.name=name
        self.year=year

    # instance methods
    def intro(self):
        print("Hello There. I am "+ self.name)
    # instance methods
    def calculateAge(self):
        return 2023 - self.year
        


p1=person("Rahmetullah",2001)
p2=person("Ahmet",1968)

p1.intro()
p2.intro()

print(f"adim {p1.name} ve yasim {p1.calculateAge()}")
print(f"adim {p2.name} ve yasim {p2.calculateAge()}")
'''



'''
class Circle:
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap
    
    def cevreHesapla(self):
        # 2pi r
        return 2*self.pi*self.yaricap 
    def alanHesapla(self):
        #pi r^2
        return self.pi*self.yaricap*self.yaricap
    
daire1=Circle(3) # paranteze hicbi sey koymazsak 1 alir
daire2=Circle(4)

print(f"1.dairenin cevresi = {daire1.cevreHesapla()} ve alani {daire1.alanHesapla()}")
print(f"2.dairenin cevresi = {daire2.cevreHesapla()} ve alani {daire2.alanHesapla()}")
'''


# special methods


# myList=[1,2,3]
# myString="my string"

# print(len(myList))
# print(len(myString))

# __init__

class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie objesi olusturuldu")
    
    # __str__
    def __str__(self):
        return f"{self.title} filmi {self.director} tarafindan yonetilen ve uzunlugu {self.duration} dk olan bir filmdir"
    # __len__
    def __len__(self):
        return self.duration
    # __del__
    def __del__(self):
        print("movie silindi")




m= Movie("movie","ali",130)

myList=[1,2,3]

# print(str(myList)) # aslinda arka tarafta def __str__(self): calisiyo
# print(str(m))


print(m)

# del m  # m objesini silmek istersek 
# print(m)

# daha fazla metod için
# https://www.informit.com/articles/article.aspx?p=453682&seqNum=6

