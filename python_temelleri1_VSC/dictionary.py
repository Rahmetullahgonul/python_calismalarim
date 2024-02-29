# key - value

# 41 => Kocaeli    34 => istanbul


# sehireler = ['Kocaeli', 'İstanbul']
# plakalar = [41,34]

# print(plakalar[sehireler.index('Kocaeli')])
# print(plakalar[sehireler.index('İstanbul')])


#print(plakalar['Kocaeli']) => 41
#print(plakalar['İstanbul']) => 34

# plakalar = {'kocaeli' : '41', 'istanbul' : 34}
# print(plakalar['kocaeli'])

# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'
# print(plakalar)


users = {
    'SadıkTruan' : {
        'age' : 36,
        'email' : 'sadık@gmail.com',
        'address' : 'kocaeli',
        'phone' : '032132131',
        'roles' : ['admin','user']
    },
    'CınarTuran' : {
        'age' : 6,
        'email' : 'cınar@gmail.com',
        'address' : 'kocaeli',
        'phone' : '021332123',
        'roles' : 'user'
    } 
}

print(users['SadıkTruan'])
print(users['SadıkTruan']['email'])
print(users['SadıkTruan']['roles'][0])
