# 1- "Bmw, Mercedes, Opel, Mazda" elamanlarina sahip bir liste olustur

car_brands=["Bmw", "Mercedes", "Opel", "Mazda"]


# 2-liste kac elamanli
car_adet=len(car_brands)
print(f"car_brands listesi {car_adet} elamanli")


# 3- listenin ilk ve son elamani nedir

print(f"listenin ilk elamani => {car_brands[0]} listenin son elamani => {car_brands[-1]}")


#4- mazda degerini toyota ile degis

#****** liste bozulamasin
# car_brands[3]="Toyota"
# print(car_brands)


#5- mercedes listenin bi elamani mi

isThereMercedes=car_brands.count("Mercedes")
if isThereMercedes>=1:
    print("evet Mercedes listenin bir elamani")
else:
    print("hayir Mercedes listenin bir elamani degil")


#6- listenin -2.indeksindeki elaman?
print(car_brands[-2])


#7- listenin ilk üc elamnani ne

print(car_brands[0:3]) 


#8- listenin son iki elamani yerine toyota ve audi ekle

#********liste yine bozulmasin

# car_brands[-1]='audi'
# car_brands[-2]="toyota"
# print(car_brands)


#9- listenin uzerine audi ve nissan ekle

#*******listeye zeval gelmesi XD

# car_brands.append("Audi")
# car_brands.append("Nissan")
# print(car_brands)


#10- listenin son elamanini silin

#************ 

# car_brands.pop(-1)
# print(car_brands)


#11- liste elamanlarini tersten yazdir

print(car_brands.reverse())
print(car_brands[::-1])


#12 asagidakileri verileri tek bir listede saklayin
    # studentA: Rahmetullah Gonul 2001,(100,100,100)
    # studentB: Hasan Topal 2001,(10,10,10)
    # studentC: Omer Asci 2001,(60,70,80)

studentA=['Rahmetullah','Gonul',2001,[100,100,100]]
studentB=['Hasan','Topal',2001,[10,10,10]]
studentC=['Omer','Asci',2001,[60,70,80]]

allStudents=[studentA,studentB,studentC]
print(allStudents)