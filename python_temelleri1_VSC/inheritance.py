# inheritance (kalıtım) : miras almasıyla olan bi durum

# Preson => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person) #studenet ve teacher için persondaki bilgileri kullanabiliriz
# yani student veya teacher için tekrar aynı özellikleri oluştumama gerek yok
# miras aldım ve sıfırdan başlamama gerek yok gibi düşün
# studenet ve teacherın özellikleri personı ilgilendirmicek


# Animal => Dog(Animal), Cat(Animal)
# dog ve cate sıfırdan hayvan özellikleri eklememe gerek yok


class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('person created')


    def who_am_ı(self):
        print('I am a person')    


    def eat(self):
        print('ı am eating')    
        



class Student(Person):  # studentın persondan türetildiğini bildiriyorum
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)  # bunu yazmazsak student personu ezer
        self.number = number
        print('Student created')


    # override  # metodu eziyoruz(geçersiz kılıyoruz)
    def who_am_ı(self):          # persondaki who am ı metodunu eziyoruz
        print('ı am a student')

    def say_hello(self):
        print('Hello ı am a student')    


class Teacher(Person):
    def __init__(self, fname, lname, branch):
        Person.__init__(self, fname, lname)
        self.branch = branch

    def who_am_ı(self):
        print(f'ı am a {self.branch} teacher')    

p1 = Person('Rahmetullah', 'Gönül')
s1 = Student('Ahmet', 'Gönül',378)
t1 = Teacher('Zuhal', 'Topal', 'chemistry')

print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname)

p1.who_am_ı()
s1.who_am_ı()
p1.eat()
s1.eat()
s1.say_hello()
t1.who_am_ı()

print(f'Selam benim adım {s1.firstname} {s1.lastname} ve okul numaram {s1.number}')
print(f'selam benim adım {t1.firstname} {t1.lastname} ve mesleğim {t1.branch} teacher')