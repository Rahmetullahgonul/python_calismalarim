import random 

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0
result = random.random() * 100
result = random.uniform(10, 100) # 10 - 100 # tam sayı olma zorunluğu yok
result = int(random.uniform(10, 100))
result = random.randint(1, 100) # 1-100 arası tam sayı


names = ['Ali', 'Yağmur', 'Deniz', 'Cenk']

result = names[random.randint(0, 3)]
result = names[random.randint(0, len(names)-1)] # elaman sayısını bilmiyorsak
result = random.choice(names) # listeden rastgele eleman seçme
result = random.sample(names, 2) # liste içinden 2 tane rastgele eleman seç

greeting = 'Hello World'
result = random.choice(greeting) # stringden random harf seçme


liste = list(range(10))
random.shuffle(liste) # elemanları liste içinde rastgele atma
result = liste


liste = range(100)
result= random.sample(liste, 3) # liste içinden 3 tane rasgele sayı getir


print(result)
