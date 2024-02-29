#   ** belirtilen dosya yoksa;
# try:

#     file = open("newfile2.txt","r") # "r" yazmasak bile boş kaldığı anda r algılar
#     print(file)
# except FileNotFoundError:
#     print("girdiğiniz dosya konumda bulunamadı")
# finally:
#     print("dosya kapandı")
#     file.close  


#   ** belirtilen dosya varsa;
# try:

#     file = open("newfile.txt","r") # "r" yazmasak bile boş kaldığı anda r algılar
#     print(file)
# except FileNotFoundError:
#     print("girdiğiniz dosya konumda bulunamadı")
# finally:
#     print("dosya kapandı")
#     file.close    


# file = open("newfile.txt","r",encoding='utf-8')

#                    for döngüsüyle;
# for i in file:
#     print(i, end="") # end ="" satır atlamasını engeller

# file.close    


#               read() fonksiyonuyla;

# file = open("newfile.txt","r",encoding='utf-8')

# content1 = file.read()
# print("içerik 1")
# print(content1)

# file = open("newfile.txt","r",encoding='utf-8')

# content2 = file.read()
# print("içerik 2")
# print(content2)

# file.close()

# file = open("newfile.txt","r",encoding='utf-8')

# content = file.read(15) # nereye kadar okuyacağını belirleyebiliriz
# content = file.read(3) # kaldığı yerden devam eder
# print(content)

# file.close()


#               readline() fonksiyonu;
#   **readline fonksiyonu her seferinde 1 satır okur


# file = open("newfile.txt","r",encoding='utf-8')

# print(file.readline(), end="")
# print(file.readline(), end="")
# print(file.readline(), end="") # her seferinde kaldığı konumdan okumaya devam eder

# file.close()


#           readlines() fonksiyonu
#   ** her bir satır bilgiyi liste şeklinde çıkarır

# file = open("newfile.txt","r",encoding='utf-8')

# list = file.readlines()
# print(list[0], end="")
# print(list[1], end="")
# print(list[2],  end="")
# print(list)

# file.close()
