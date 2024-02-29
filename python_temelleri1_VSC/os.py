import os 
# genel olarak işletim sistemi üzerindeki dosyalar/bilgiler için kullanılır
# result = dir(os)
# result = os.name # nt = windows
# C:\Users\Rahmet\Desktop\python_temelleri


#       klasör değiştirme 
# os.chdir('c\\') # c ye dosya aktarma
# os.chdir('..') # bir üst dosyaya geçer
# os.chdir('../..') # iki kez üst dosyaya geçer

#        klasör oluşturma
# os.mkdir("new_directory") # klasör oluşturma
# os.makedirs("new_directory/yeni_klasör") # dosya içine dosya açma
# os.rename("ilk_isim","ikinci isim") # klasörün adını değiştirme
# os.rmdir("silmek istedğin dosya adı") # dosya silme
# os.removedirs("üst klasör/alt dosya") # altındaki dosyayı silme


#        etkin klasörü öğrenme
# result = os.getcwd() # dosyanın nerde bulunduğunu söyler

#       listeleme işlemleri
# result = os.listdir() # dosyaları listeleme
# result = os.listdir('C:\\') # c nin altındakileri listeleme

#       dosyaları filtreden geçirme;
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


# result = os.stat("bankamatik.py") # istediğiniz dosya hakkında bilgi sahibi olma
# import datetime
# result = result.st_size/1024 # 1024 bölme işlemi nedei mb a dönüştürmek için
# result = datetime.datetime.fromtimestamp(result.st_ctime) # dosyanın oluşturulma tarihi 
# result = datetime.datetime.fromtimestamp(result.st_atime) # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi


# os.system("notepad.exe") # istedğimiz ygulamayı çalıştırma

#        path
