# def greeting(name):
#     print("Hello", name)

# greeting('Rahmetullah')
# print(greeting)    

# sayHello = greeting

# print(sayHello)
# print(greeting)

# print(greeting('Rahmetullah'))
# print(sayHello('Rahmetullah'))

# del sayHello
# print(sayHello)
# # print(greeting)


# ** encapsulation

# def outer(num1):
#     print('outer çalıştı')
#     def inner_increment(num1):
#         print('inner çalıştı')
#         return num1 + 1
#     num2 = inner_increment(num1)    
#     print(num1,num2)

# outer(10)
# inner_increment(15) # hata verir, çalışmaz



# def factorial(number):
#     if not isinstance(number,int):
#         raise TypeError("number must be an integer")    

#     if not number >=0:
#         raise ValueError("number must be zero or positive")
    
#     def inner_factorial(number):
#         if number <= 1:
#             return 1


#         return number * inner_factorial(number - 1)

#     return inner_factorial(number)
# try:
#     print(factorial('4'))
# except Exception as ex:
#     print(ex)    

# print(factorial(4))