# Error handling => hata yönetimi

# try:
#     x = int(input('X: '))
#     y = int(input('y: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('y için sıfır girilemez')
# except ValueError:
#     print('lütfen sayısal değer giriniz')


# HATALARI TEK TEK YAZMAK YERİNE BİR YERDE TOPLAYABİLİRİZ ;


# try:
#     x = int(input('X:'))
#     y = int(input('Y:'))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e: # her bir hatanın özeline girmek istersen e gibi bir değişken ver
#     print('yanlış bilgi girdiniz')
#     print(e)    


# try:
#     x = int(input('X:'))
#     y = int(input('Y:'))
#     print(x/y)
# except: # her hataya karşı bildiri verir ancak hatanın türüne ulaşamıyoruz
#     print('yanlış bilgi girdiniz')
# hataların kaydını tutan bi uygulamada kullanma


# try:
#     x = int(input('X:'))
#     y = int(input('Y:'))
#     print(x/y)
# except:
#     print('yanlış bilgi girdiniz')
# else:
#     print('her şey yolunda')  

# ÖRNEĞİN LOOPLA BİRLİKTE KULLANIRKEN

# while True:
#     try:
#         x = int(input('X:'))
#         y = int(input('Y:'))
#         print(x/y)
#     except:
#         print('yanlış bilgi girdiniz')
#     else:
#         break

# böylelikle döngüye soktuğumuz için kullanıcı doğru bilgileri girene kadar sürekli
# uygulama sormaya devam eder    


# while True:
#     try:
#         x = int(input('X:'))
#         y = int(input('Y:'))
#         print(x/y)
#     except Exception as ex:
#         print(f'yanlış bilgi girdiniz: {ex}')
#     else:
#         break

# hatayı daha rahat düzeltebilmek adına exception girebiliriz


# while True:
#     try:
#         x = int(input('X:'))
#         y = int(input('Y:'))
#         print(x/y)
#     except Exception as ex:
#         print(f'yanlış bilgi girdiniz {ex}')
#     else:
#         break
#     finally:
#         print('try except sonlandı.')

# finally amacı tanımlanmış olan değişkenlerin sonlandırılması için kullanıyoruz