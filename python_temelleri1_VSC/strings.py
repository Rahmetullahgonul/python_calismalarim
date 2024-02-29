name = 'Ahmet'
surname = 'Turan'
age = 36

age = str(age)        # veya age = '36' yapabilirsin    

'''
print('My name is '+ name + ' '+ surname + ' and \n I am '+ age + ' years old' ) 
'''

#\n yapınca yeni satıra geçer

greeting = 'My name is '+ name + ' '+ surname + 'and \n I am '+ age + ' years old' 
print(greeting)

print(greeting[0])      #ilk karakteri yazdırır        #M
print(greeting[3])      #üçüncü karakteri yazdırır     #n
print(len(greeting))    #kaç karakteri olduğunu söyler #45
print(greeting[44])     #son karakteri verir           #d
print(greeting[-1])     #son karakteri verir           #d




print(greeting[3:7])    #üçten yediye kadar git    #name
print(greeting[3:])     #üçten başla sona kadar git
print(greeting[:15])    #baştan başla onbeşe kadar git
print(greeting[2:40:2]) #ikiden başla kırka kadar git ve iki karakterde bir al
