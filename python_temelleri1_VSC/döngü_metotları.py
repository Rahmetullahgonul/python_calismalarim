#   RANGE METODU

# for item in range(10): # sıfırdan başlayarak 10 indeks sayı yazdırır
#     print(item)


# for item in range(2,10): # ikiden başlaya 9 a kadar git
#     print(item)    


# for item in range(50,100,10): # 50 den başla 100 e kadar git ve 10ar 10ar art
#     print(item)

# print(list(range(50,100,20))) # listeye çevirmek



#    ENUMERATE METODU

# index = 0
# greeting = 'Hello'

# for letter in greeting:
#     print(f'index : {index} letter : {letter}')
#     index += 1


# veya enumerate ile yapalım ;


# greeting = 'Hello'
# for index,letter in enumerate(greeting):
#     print(f'index:{index} letter:{letter}')


# veya daha do  kolayı ;


# greeting = 'Hello'
# for rastgele in enumerate(greeting):
#     print(rastgele)




#    ZİP METODU

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3))) # listeler bire bir birleştiriliyo
 
for rastgele in zip(list1,list2,list3):  # tüm listeyi yazdırı
    print(rastgele)


for a,b,c, in zip(list1,list2,list3):  # sadece 1.-2. veya 3.listeyi yazdırabilirsin
    print(a)