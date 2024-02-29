# dosya açmak ve oluşturmak için open() fonksiyonu kullanılır 
# kullanımı: open(soya_adi, dosya_erişme_modu)
# dosya_erişme_modu => dosya hangi amaçla açtığımızı belirtir 

# *******************************************************************


# "w": (Write) yazma modu. dosya konumda olşturulur 
#   ** dosyayı konumda oluşturur
#   ** dosya içeriğini siler ve yeniden ekleme yapar


# file = open("newfile.txt","w")
# file.close() # dosyayı kapama
# dosyayla işimiz bittikten sonra yazılımın hızını düşürmemesi için kapatmamız lazım

# file = open("C:/users/Rahmet/desktop/newfile.txt","w")
# print(file)
# file.close()

# file = open("newfile.txt","w")
# file.write("Rahmetullah Gonul") # dosya üzerine yazı ekleme (Türkçe karakterleri tanımyo)
# Türkçe karakter tanıması için: encoding='utf-8' yazarız;
# file = open("newfile.txt","a",encoding='utf-8')
# file.write('Rahmetullah Gönül')
# file.close()

# *******************************************************************


# "a": (Append) ekleme. dosya konumda yoksa oluşturlur 

# file = open("newfile.txt","a",encoding='utf-8')
# # file.write('Ahmet Gönül')

# # yeni satıra geçmek için;
# # file.write('\nZehra Gönül')
# # file.write('\nAhmet Gönül')

# # \n yaparsak bilgi eklenir ve bi alt satıra geçer yeni bilgi için
# # file.write('Firdevs Gönül\n')
# # file.write('Hatice Gönül')
# file.close()

# *******************************************************************


# "x": (Create) oluşturma. dosya zaten varsa hata verir 
#   ** dosya oluşturmak için kullanılır 
#   ** dosya hali hazırda varsa hata verir 

# file = open("newfile2.txt","x",encoding='utf-8')

# *******************************************************************


# "r": (Read) okuma. varsayılan dosya konumda yoksa hata verir