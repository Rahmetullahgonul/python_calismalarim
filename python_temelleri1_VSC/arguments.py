# def changeName(n):
#     n = 'Rahmet'
# name = 'Ahmet'

# changeName(name)
# print(name) 



# def change(n):
#     n[0] = 'İstanbul'

# sehirler = ['Ankara','İzmir']
# change(sehirler)
# print(sehirler)



# def change(n):
#     n[0] = 'İstanbul'

# sehirler = ['Ankara','İzmir']
# n = sehirler[:] #slicing

# n[0] = 'İstanbul'

# print(sehirler)
# print(n)




# def change(n):
#     n[0] = 'İstanbul'

# sehirler = ['Ankara','İzmir']

# change(sehirler[:])
# print(sehirler)




# def add(a,b,c = 0, d = 0, e = 0): # burdaki c,d,e 0 olmasının sebebi parametre girilmezse
#     return sum((a,b,c))           # dahi fonksiyonun çalışmaya devam ettirme


# print(add(10,20))
# print(add(20,30,40))

                        # VEYA

# def add(*params):      # istediğimiz kadar parametre girebiliriz
#     print(params)      # gönderdiğinimiz elamanlar liste olarak yazdırılır
#     print(params[2])   # isteğimiz elamana gidebiliriz
#     return sum(params)

# print(add(1,2,3,4))
# print(add(15,25,35,45))

                    # DÖNGÜ İLE YAPMAK İSTERSEK

# def add(*params):
#     sum = 0 

#     for n in params:
#         sum = sum + n
#     return sum    

# print(add(1,2,3,4))
# print(add(15,25,35,45))    


                    # DİCTİONARY KULLANIMI

# def displayUser(**args):     # dictionary geliceği için iki yıldız kullandık
#     for key,value in args.items():
#         print(f'{key} is {value}')
# displayUser(name = 'Rahmet', age = 21, city = 'istanbul')
# displayUser(name = 'Duygu', age = 26, city = 'kocaeli', phone = '1234')
# displayUser(name = 'Mert', age = 11, city = 'ankara', mail = 'maille')



# def myFunc(a, b, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)

# myFunc(10, 20, 30, 40, 50, key1 ='value1', key2 = 'value2')
# #ilk 2 parametre a ve b ile 3-4-5.parametre ise args ile keyler ise kwargs a gider