# name = 'Rahmetullah Gönül'

# for letter in name:            #continue sadece o anki döngü turunu iptal ediyo 
#     if letter == 'm':          #ve o an kaldığı yerden devam ediyo
#         continue
#     print(letter)




# for letter in name:            # break döngüden tamamen çıkış yapıyo 
#     if letter == 'm':
#         break
#     print(letter)



# x = 0
# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x +=1



# y = 0 
# while y < 5:
#     y += 1       # eğerki artırma işlemini burda yaparsan sadece 2 yi es geçer 
#     if y == 2:
#         continue
#     print(y)




# z = 0
# while z < 5:
#     if z == 2:  # böyle yaparsan 2 ye kadar gelir ve 2 yi okumadan durur
#         continue
#     print(z)
#     z += 1    




# örnek : 1-100 e kadar tek sayıların toplamı 

# toplam = 0
# x = 0
# while x < 100:
#     x += 1
#     if(x %2 == 0):
#         continue
#     toplam += x
# print(toplam)    