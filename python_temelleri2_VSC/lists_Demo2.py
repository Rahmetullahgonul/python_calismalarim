names=["Rahmetullah","Fatih","Omer","Efe"]
years=[2001,2004,1998,1999]

#1- selim ismini listenin sonuna eklems

names.append("selim")
print(names)


#2- listenin basina kurt ekle

names.insert(0,'kurt')
print(names)


#3- Fatihi listeden sil

del(names[2])
print(names)


#4- omar listenin bir elamani mi

if (names.count("Omer")>0):
    print("omer listenin bir elamani")
else:
    print("omer listenin bir elamani degil")


#5-omer isminin indeksi ne

print(names.index('Omer'))


#6- listeyi ters cevir

names.reverse()
print(names)


#7- liste elamanlarini alfabetik olarak sirala

names.sort()
print(names)


#8- years listesini rakamsal buyukluge gore sirala

years.sort()
print(years)


#9- years dizisinin en buyuk ve en kucuk elamani

print(years[0],years[-1])


#10-years dizisinde kac tane 2001 vardir

print(years.count(2001))


#11- years dizisinin tum elamanlarini silin

# years.clear()
# print(years)


#12- kullanicidan alinan uc tane markayi bir listede sakla

markalar=[]

for i in range(3):
    marka=input("marka adini giriniz:")
    markalar.append(marka)

print(markalar)