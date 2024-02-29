# username, password => database

# 'Sadikturan' , '123456'

a, b, c, d = 5, 5, 10, 4
password = '1234'
username = 'Sadıkturan'

result = (a == b)  #true a b ye eşit mi 
result = (a == c)  #false a c ye eşit mi
result = ('sdktrn' == username)  #false 
result = ('Sadıkturan' == username) #true
result = (a != b ) #false a b ye eişt değil mi 
result = (a != c) #true a c ye eşit değil mi
result = (a > c) #false a c den büyük mü
result = (c > a) #true c a dan büyük mü
result = (a >= b) #true a b den büyük veya eşit mi
result = (a <= b) #true b a dan büyük veya eşit mi
result = (True == 1) #true, true bilgisi yazılımda 1 e eşittir
result = (False == 0) #true, false bilgisi yazılımda 0 a eşittir
result = True + False + 40 # 1 + 0 + 40



print(result)