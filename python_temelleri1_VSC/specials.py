# myList = [1,2,3]
# myString = 'my string'

# print(len(myList))
# print(len(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu')


    def __str__(self):
        return f"{self.title} {self.director} tarafından çekilmiş {self.duration} süreli bir filimdir"
        
    def __len__(self):
        return self.duration

    def __del__(self):
        print('aramakta olduğunuz film silinmiştir')    

m = Movie('Rahmetullahın hayatı', 'Ahmet Gönül', 121)


# print(type(myList))
# print(type(myString))
# print(type(Movie))

myList = [1,2,3]
# print(str(myList))
# print(str(m))

print(len(myList))
print(len(m))

print(str(m))


# https://www.informit.com/articles/article.aspx?p=453682&seqNum=6