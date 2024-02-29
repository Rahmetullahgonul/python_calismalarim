#1 'Bmw,mercedes.opel,mazda' elamanlarına sahip bi liste oluşturun
#2 liste kaç elamanlı
#3 listenin ilk ve son elamanı hangisi
#4 mazdayı toyata ile değiş
#5 mercedes listenin bi elamanı mı
#6 listenin -2 indeks değeri nedir
#7 listenin ilk üç elamanını alın
#8 listenin son 2 elamanı yerine toyota ve renault değerini ekleyin
#9 listenin üzerine audi ve nissan değerlerini ekleyin
#10 listenin son elamanını silin
#11 listenin elamanlarını tersten yazdırın




markalar = ['bmw','mercedes','opel','mazda']
# print(len(markalar))

# print(markalar[0])
# print(markalar[-1])

# markalar[-1] = 'toyota'
# print(markalar)

# result = 'mercedes' in markalar
# print(result)

#print(markalar[-2])

# result = markalar[0:3]
# print(result)

# markalar[-1] = 'toyota'
# markalar[-2] = 'renault'
# print(markalar)

# markalar.append('audi')
# markalar.append('nissan')
# print(markalar)

# markalar.pop(-1)
# print(markalar)
#veya
#del(markalar[-1])
#print(markalar)

# markalar.reverse()
# print(markalar)
#veya
# result = markalar[::-1]
# print(result)



studentA = ['yiğit','bilgi',2010,[70,80,90]]
studentB = ['sena','turan',1999,[80,80,70]]
studentC = ['ahmet','turan',1998,[80,70,90]]
students = studentA + studentB + studentC
# print(students)
# result = studentA[3][2]
# print(result)

result = f'{studentA[0]} {studentA[1]} {2022 - studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}'
print(result)
