a,b,c,d=5,5,10,4
password='1234'
username='rahmetullah'

result = a==b # True
result=a==c # false
result= username=='rahmet'#false
result=username=='rahmetullah' #true
result=a!=b #false
result=a!=c #true
result= a<c # true
result = a>=b #true
result= username=='rahmetullah'and password=='1234'#true
result= username=='rahmetullah'and password=='4321'#false
result= username=='rahmetullah'or password=='4321'#true


print(result)