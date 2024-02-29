liste=[1,2,3]

'''
*****************************RANGE*********************************
for item in range(50,100,10):# bizim icin bir liste olusturuyor(50 den basla 100 e git 10ar arttir)
    print(item)
print(list(range(50,100,10)))
'''


'''
*******************enumerate*********************
greeting='Hello There'
index=0

for letter in greeting:
    print(f"letter=>{letter}, index=>{index}")
    index+=1

# ya da daha kolayi

for letter in enumerate(greeting):
    print(letter)
'''


'''
************************zip*********************
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']

print(list(zip(list1,list2)))
'''