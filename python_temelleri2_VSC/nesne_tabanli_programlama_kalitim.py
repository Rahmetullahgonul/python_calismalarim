#inheritance (kalitim): miras alma 

# Person => name, lastname, age, eat(), run(), drink()

# Student(Person), Teacher(Person) #student veya person için tekrar yazmaya gerek yok

class Person():
    def __init__(self,fname,lname):
        self.firstName=fname
        self.lastName=lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")


class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname) # kodlarin birbirini ezmesini engelliyo
        self.studentNumber=number
        print("Student Created")
    
    # override
    def who_am_i(self):
        print("bu kod persondaki kodu ezer")


p1=Person("Rahmetullah","Gonul")
s1=Student("Ahmet","Gonul",200)

print(p1.firstName + " " +p1.lastName)
print(f"{s1.firstName} {s1.lastName} {s1.studentNumber}")


p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()