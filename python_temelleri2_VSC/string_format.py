name = "Rahmetullah"
surname = "Gonul"
age=22

# print("my name is {} {}".format(name,surname))
# print("my name is {1} {0}".format(name,surname)) # yerlerini degisebiliriz
# print("my name is {s} {n}".format(n=name,s=surname)) # degisken atayabiliriz
# print("my name is {} {} and I am {} years old".format(name,surname,age)) #sayilar icinde gecerli

result = 200/700
print("the result is {r:1.3}".format(r=result)) # sadece ilk uc degeri yazdirmak istersek
# r:1.3 => 1 tam kisimda kac karakter olucak .3 ise virgulden sonra kac karakter alacak


#f string ile yazdirma
#cok daha kullanisli
print(f"My name is {name} {surname} and I am {age} years old") 