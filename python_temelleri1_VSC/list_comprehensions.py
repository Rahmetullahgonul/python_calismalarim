# sayilar = []
# for in x range(10):
#     sayilar.append(x)
# print(sayilar)


# numbers = [x for x in range(10)]  # kolayca listeye ekleme
# print(numbers)


# for x in range(10):
#     print(x**2)
# numbers=[x**2 for x in range(10)]    
# print(numbers)


numbers = [x*x for x in range(10) if x%3==0]
print(numbers)


myString = 'hello'
myList = []
for letter in myString:
    myList.append(letter)
print(myList)    


myList = [letter for letter in myString]
print(myList)


years = [1983,1999,2000,2001,2019]
ages = [2022-year for year in years]
print(ages)


results = [x if x%2==0 else 'TEK' for x in range(1,10)]
print(results)


result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)        



numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)