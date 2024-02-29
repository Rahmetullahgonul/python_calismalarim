with open("newfile.txt","r",encoding='utf-8') as file:
    content = file.read(20)
    print(content)
    file.seek(0) # en başa gönderme
    print(file.tell())
    content2 = file.read()
    print(content2)

# with kullandıktan sonra file.close() demene gerek yok