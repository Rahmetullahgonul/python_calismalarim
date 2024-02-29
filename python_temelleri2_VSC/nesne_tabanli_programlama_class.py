# class 

class Person:

    # class attributes
    address='no information'
    #constructor(yapici method)
    def __init__(self, name, year):
        # object attributes
        self.name=name
        self.year=year
        # print("init metodu calisti")

    # methods


# object,instance
p1=Person("Rahmetullah",2001)
p2=Person("Ahmet",1968)

# print(p1)
# print(type(p1))
# print(p2)
# print(type(p2))


# accessing object attributes
print(f"1.kullanicinin adi: {p1.name} dogum tarihi :{p1.year}\n2.kullanicinin adi: {p2.name} dogum tarihi:{p2.year}")
print(p1.address)

# updating
p1.address='istanbul'
print(p1.address)