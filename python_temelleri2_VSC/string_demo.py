website = "https://www.linkedin.com"
course ="https://github.com/Rahmetullahgonul"

# 1- course karakter dizisinde kac karakter bulunmaktadir

adet=len(course)
print(f"course karakter dizisinde {adet} karakter bulunur")

# 2- website icinden www karakterlerini alin

print(f"sadece www ekrana gelecek => {website[8:11]}")

# 3-website icinden com ifadesini alin 

adet_website=len(website)
print(f"sadece com ifadesi ekrana gelecek => {website[adet_website-3:]}")

# 4- course icindeki ilk ve son 15 karakterleri alin ve yazdirin

print(f"course ifadesindeki ilk 15 karakter => {course[:14]}\ncourse ifadesindeki son 15 karekter =>{course[adet-15:]}")

#5- course ifadesindeki karakterleri tersten yazdirin

#*****ilk yontemi

print(f"(ilk yontemle) course tersten yazilmis hali => {course[::-1]} ")

#*****ikinci yontemi reversed() fonksiyonu 

ters_dize = ''.join(reversed(course))
print(f"(ikinci yontemle) course tersten yazilmis hali => {ters_dize}")



name, surname, age, job='Rahmetullah','Gonul',22,'engineer'
# 6- 'My name is Rahmetullah Gonul I am 22 years old and I am an engineer' yazdir

print(f"My name is {name} {surname} I am {age} years old and I am an {job}")
print("My name is {} {} I am {} years old and I am an {}".format(name,surname,age,job))
print("My name is "+name +' ' + surname +" I am "+ str(age)+ " and I am an "+job)


#7- 'Hello world' ifadesindeki w harfini W ile degistir

word='Hello world'
yeni_cumle = word.replace('w','W')
print(yeni_cumle)


#  8-'abc' ifadesini 3 kere yazdir

print('abc'*3)