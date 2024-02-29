'''
name= 'Rahmetullah'

for letter in name :
    if letter =='l':
        continue
    print(letter)
print("**********************************")
for letter in name :
    if letter =='l':
        break
    print(letter)
'''
#breake girilen kosula kadar kodu calistirir sonrasinda durur
#continue is girilen kosulu gorunce atlayarak kodun calismasina devam eder

'''
x=0
while x<=10:
    x+=1
    if x==5:
        continue
    print(x)
print("************************")
'''

# 1-100 e kadartek sayilarin soplami olsun
x=0
toplam=0
while x<=100:
    x+=1
    if x%2!=0:
        continue
    toplam+=x
    
print(toplam)