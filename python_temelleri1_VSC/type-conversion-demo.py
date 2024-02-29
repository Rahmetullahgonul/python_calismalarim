'''
daire alanı : pi r kare
daire çevresi : iki pi r 


* yarı çapı verilen bi dairenin alanı ve çevresini hesaplayınız. (r : 3.14)
'''

pi = 3.14
r = input('daire yarıçapı : ')
r = float(r)

daireAlanı = pi * r * r        # veya daireAlanı = pi * (r ** 2 )
daireCevresi = 2 * pi * r

print(daireAlanı)
print(daireCevresi)

#kullanıcıya neyi bulduğunu gösterebiliriz
print('daireAlanı: '+ str(daireAlanı)+ ' '+ 'daireCevresi: '+ str(daireCevresi))
