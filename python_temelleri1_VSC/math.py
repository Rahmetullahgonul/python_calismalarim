#                    YÖNTEM BİR

# import math 

# value = dir(math)
# value =help(math)
# value =help(math.factorial)
# print(value)


# value = math.sqrt(49)
# value = math.factorial(5)
# value = math.floor(5.9)
# value = math.ceil(5.9)

# print(value)

# import math as islem

# value = islem.factorial(4)
# print(value)


#                    YÖNTEM İKİ
# bunu yaparsak artık metodun ismini her satırda yazmamız gerekmez

# from math import * # burdaki yıldız math mödülündeki her şeyi al demek
from math import factorial, sqrt # sadece faktöriyel ve karakök aldırır

# value = factorial(5)
value = sqrt(9)
# value floor(6.1)

# print(value)

def sqrt(x):
    print('x:' + str(x))


print(value)    

# son kısımda iki tane sqrt değişkeni var hangisine öncelik verdi;
# ilgili dosya içindeki dosyalardan hangisi en son tanımlanırsa o yazdırılır