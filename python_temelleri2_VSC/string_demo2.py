website="https://www.linkedin.com"
course ="Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"

# 1- ' Hello World ' karakter dizisinin bas ve sondaki bosluk karakterlerini silin

helloworld=' Hello World '
bosluk_silme = helloworld[1:6]+helloworld[6:12]
print(bosluk_silme)


# 2-"https://www.linkedin.com" linkedin haric her bilgiyi sil 

yeni_website=website[12:20]
print(yeni_website)


# 3- course hepsini kucuk yap

yeni_course=course.lower()
print(yeni_course)


# 4- website icinde kac tane i karakteri var

kac_adet=website.count('i')
print(kac_adet)


# 5- website www ile baslayip comla bitiyo mu
if website[0:3]=='www' and website[:-3:-1]=='com':
    print("evet websitesi www ile baslayip com ile bitiyo")
else:
    print("hayir websitesi www ile baslayip com ile bitmiyo")



# 6-website icinde .com var mi
varmi=website.find(".com")
if varmi>0:
    print("evet metnin icinde .com ifadesi vardir")
else:
    print("hayir metnin icinde .com ifadesi yoktur")


# 7- course icindeki hepsi alfabetik mi

alfabe=course.isalpha()
if alfabe==True:
    print("evet alfabetik")
else:
    print("hayir alfabetik degil")

# 8 'Contents' ifadesini satirda 50 karaktere yerlestirip sagina soluna * ekle

yerlestirme='Contents'
yeni_yerlestirme=yerlestirme.center(50,'*')
print(yeni_yerlestirme)


# 9 coursedaki tum boslukları - ile degistir

degisim_sart=course.replace(" ","-")
print(degisim_sart)


# 10- 'hello world' ifafesindeki world yerine there yaz

yeni_hello=helloworld.replace("World","there")
print(yeni_hello)


# 11- coursedaki ifadeleri bosluklarla birlikte ayir

bosluk=course.split(" ")
print(bosluk)