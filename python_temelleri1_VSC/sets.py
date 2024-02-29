fruits = {'orange','apple','banana'}

#print(fruits[1]) # indekslenemez

# for x in fruits:  # bu ilerki konu
#     print(x)

fruits.add('cherry')
print(fruits)

fruits.update(['mango','grape'])
print(fruits)

# myList = [1,2,5,2,5,1,1,3]
# print(set(myList)) # tekrarlayan elamanlar liste içinden çıkar

# fruits.remove('mango')
# fruits.discard('apple')
# bunlar elaman silmek için 

fruits.pop()   # normalde son elamanı siler ama set listesinde sıra olmadığından
# rastgele bi eleman siler
print(fruits)

fruits.clear()
print(fruits)
