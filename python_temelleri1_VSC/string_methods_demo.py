from distutils import core
from email import message
from turtle import window_width
from unittest import result


website = 'https://www.sadikturan.com'
course = 'Python kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)'

# 1 ' Hello World ' karakter dizisinin baş ve sondaki boşllukları silin
  

# result = ' Hello World '.strip()
# print(result)



# 2 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin 


# result = 'www.sadikturan.com'.strip('w.moc')
# print(result)



# 3 'course' karakter dizisinin tüm harflerini küçük harf yapın


# course = course.lower()
# print(course)



# 4 'website' içinde kaç tane a hari var 


# website = website.count('a')
# print(website)


# 5 'website' www ile başlayıp .com ile mi bitiyo


# result = website.startswith('www')
# print(result)
# result = website.endswith('.com')
# print(result)


# 6 'website' içinde com ifadesi var mı 


# website = website.find('com')
# print(website)


# 7 'course' içindeki karakterlerin hepsi alfabetik mi(sayı var mı) (isalpha, isdigit)

# result = course.isalpha()
# print(result)

# result = course.isdigit()
# print(result)


# 8 'Contents' ifadesini satırda 50 karakter boşluk bırakıp * ile yazdırın


# message = 'Contents'
# result = message.center(50,'*')
# print(result)



# 9 'course' daki boşlukları - ile değiş


# result = course.replace(' ','-')
# print(result)


# 10 'Hello World ' Worldü There ile değiş


# message = 'Hello World'
# result = message.replace('World','There')
# print(result)



# 11 'course' karakter dizisini boşluk karakterlerinden ayırın


# result = course.split(' ')
# print(result)