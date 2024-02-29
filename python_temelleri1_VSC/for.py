numbers = [1, 2, 3, 4, 5]

for r in numbers:
    print(r)

for a in numbers:
    print('hello')   # listenin eleman sayısı kadar for döngüsü döner


names = ['Çınar','Sadık','Sena']

for name in names:
    print(f'My name is {name}')


name = 'Sadık Turan' 
for n in name:
    print(n)   #stringteki her karakter tek tek yazdırılır


tuple = [(1,2),(1,3),(3,5),(5,7)]

for a,b in tuple:
    print(a) #sadece ilk elamanları yazar, b sadece ikincileri (a,b) her ikisini de

d1 = {'k1': 1, 'k2': 2, 'k3': 3}

# for item in d:
#     print(item) # bu sadece key bilgilerini verir

for key,value in d1.items():
    print(value)    #value dersen value, key dersen key, (key,value) dersen ikisi de 