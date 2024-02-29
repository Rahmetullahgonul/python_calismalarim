# with open("newfile.txt","r+",encoding='utf-8') as file:
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt","r+",encoding='utf-8') as file:
#     print(file.read())


#   **** sayfa sonunda güncelleme *******

# with open("newfile.txt","a",encoding='utf-8') as file:
#     file.write("\nÖmer Tarık Aşçı")

#  **** sayfa başında güncelleme ****


# with open("newfile.txt","r+",encoding='utf-8') as file:
#     content = file.read()
#     content = "\nAhmet Selim Bıyık " + content 
#     file.seek(0)
#     file.write(content)
#     print(content)


# with open("newfile.txt","r",encoding='utf-8') as file:
#     print(file.read())   



#   **** sayfa ortasına güncelleme yapmak

# with open("newfile.txt","r+",encoding='utf-8') as file:
#     list = file.readlines()
#     list.insert(1,"Yılmaz Vural \n")
#     file.seek(0)
#     file.writelines(list)

# with open("newfile.txt","r",encoding='utf-8') as file:
#     print(file.read())        