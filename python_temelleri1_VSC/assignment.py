# x = 5
# y = 10
# z = 20

# x,y,z = 5,10,20

# x,y = y,x

# x = x + 5 # veya
# x += 5
# x -= 5
# x *= 5
# x /= 5
# x %= 5
# x //= 2
# x **= 2
# x *= y


# print(x,y,z)


# values = 1, 2, 3

# x,y,z = values
# print(x,y,z)

# print(type(values))
# print(values)


values = 1, 2, 3, 4, 5
x, y, z = 5, 10, 20

x, y, *z = values
print(x,y,z)
print(x,y,z[1])
