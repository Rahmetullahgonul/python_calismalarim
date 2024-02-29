x = 6
hak = 5
devam = 'e'

result = 5 <= x < 10

#and

result = x > 5 and x < 10  # True, True => True
result = hak > 0 and devam == 'e' # True, True => True


#or

result = x > 10 or x > 6 # bir tane True gelirse => True


#not
result = not(x > 0)  #normlade True gelir ancak not eklersek False gelir


#r, 5-10 arasında olan bi çift sayı mi

r =int(input('r sayısı nedir :'))
result = ((r < 10) and (r > 5)) and (r %2== 0) 


print(result)