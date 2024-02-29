#key - value

#41=> kocaeli, 34=> istanubl

# sehirler=['istanbul','kocaeli']
# plakalar=[34,41]

# print(plakalar[sehirler.index('kocaeli')])
# print(plakalar[sehirler.index('istanbul')])
#ustteki metodun calismasi icin bire bir ayni sirada olmasi gerek

#dictionaryde ise dogrudan print(plakalar['kocaeli'])=> 41 ciktisi almamizi saglar

# plakalar={'kocaeli':41,'istanbul':34}
# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara']=6
# print(plakalar)

# plakalar['istanbul']=85
# print(plakalar)

users={
    'Rahmetullah Gonul':{
        'age':22,
        'job':'student of engineering',
        'gender':'male'
    },
    'Ahmet Gonul':{
        'age':55,
        'job':'electrician',
        'gender':'male'
    },
    'Ahmet Selim Biyik':{
        'age':'23',
        'job':'student of engineering',
        'gender':'male'
    }
}
print(users['Rahmetullah Gonul']['age'])