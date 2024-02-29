x,y,z=5,10,20

x=x+5 #=> x+=5
x=x-5 #=> x-=5
x=x*5 #=> x*=5
x=x/5 #=> x/=5
print(x)

values = 1,2,3
x,y,z= values
print(x,y,z)

degerler = 1,2,3,4,5

x,y,*z=degerler #z yi liste seklinde algilar
print(x,y,z)
print(z[0])