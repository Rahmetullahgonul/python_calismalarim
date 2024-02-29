class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
        

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedin=False
        self.currentUser={}

        #load users from .json file
        self.loaduser()
                       
    def loaduser():
        pass


    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("kullanici olusturuldu\n")

    def login(self):
        pass
    def savetoFile(self):
        pass

repository=UserRepository()

while True:
    print("Menu".center(50,'*'))
    secim = input("1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\nSeciminiz")
    if secim=='5':
        break
    else:
        if secim=='1':
            username=input(print("lutfen bir kullanici adi giriniz"))
            password=input(print("lutfen bir sifre belirleyiniz"))
            email=input(print("lutfen emailinizi1 giriniz"))

            user= User(username=username,password=password,email=email)
            repository.register(user)
        
        
        
        
        
        
        elif secim=='2':
            #login
            pass
        elif secim=='3':
            #logout
            pass
        elif secim=='4':
            # identity
            pass
        else :
            print("yanlis secim")