# username='Rahmetullah'
# password=1234

# if username=='Rahmetullah' and password==1234:
#     print(f"hosgeldin {username}")
# elif username=='Rahmetullah' and password!=1234:
#     print("sifer hatali")
# elif username!='Rahmetullah' and password==1234:
#     print("kullanici adi hatali")
# else:
#     print("hatali bir giris yaptiniz yeniden deneyin")


ilk_sayi=int(input("ilk sayi:"))
ikinci_sayi=int(input("ikinci sayi:"))

if(ilk_sayi>ikinci_sayi):
    print(f"{ilk_sayi}>{ikinci_sayi}")
elif(ilk_sayi<ikinci_sayi):
    print(f"{ikinci_sayi}>{ilk_sayi}")
else:
    print(f"{ilk_sayi}={ikinci_sayi}")