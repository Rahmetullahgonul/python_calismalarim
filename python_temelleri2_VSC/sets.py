fruits={'orange','apple','banana','melon'}

#print(fruits[0])
# normal listelerden en buyuk farki indekslenemez bir liste olusu

for i in fruits:
    print(i)
# liste elamanlarina ulasmak icin dongu kullanabiliriz

fruits.add('strowberry')
print(fruits)

fruits.update(['mango','lemon'])
print(fruits)

fruits.remove('apple')
print(fruits)
fruits.discard('mango')
print(fruits)
fruits.pop() # indeksli olmadigi icin rastgele siler
print(fruits)
fruits.clear()  
print(fruits)