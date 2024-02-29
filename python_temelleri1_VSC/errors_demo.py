liste = ['1','2','5a','10b','abc','10','50']

# 1)liste elemanları içindeki sayısal değerleri bulunuz  

# 2) kullanıcı 'q' değerini girmedikçe aldığınız her input sayı olduğundan emin olunuz aksi 
# halde hata mesajı yazın 

# 3) girilen parola içinde türkçe karakter hatası veriniz 

# 4) faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin 



# 1

# list = []
# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue
#     list.append(result)    

# print(list)    



# 2
# list = []

# while True:
#     sayi = input('Sayı:')
#     if sayi == 'q' :
#         break

#     try:
#         result = float(sayi)
#         print('girdiğiniz değer başarılı')
#         list.append(result)
#     except:
#         print('geçersiz sayı')
#         continue
    
# print(list)    


# 3
# parola = input('parola:')

# def check_password(parola):
#     turkce_karakterler = 'şçğüöıİ'
#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError('Parola türkçe karakter içeremez')
#         else:
#             pass    
#     print('geçerli parola')

# try:
#     check_password(parola)
# except TypeError as error:
#     print('girdiğiniz parolada tr karakter var')    



# 4
# def faktoriyel(x):
#     x = int(x)

#     if x < 0 :
#         raise ValueError('Negatif değer')

#     result = 1 

#     for i in range(1, x+1):
#         result *= i
    
#     return result    

# for x in [5,10,20,-3,'10a']:
#     try:
#         y = faktoriyel(X)
#         print(error)    
#         continue
#     print(y)    