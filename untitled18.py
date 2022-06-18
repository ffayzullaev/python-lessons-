telefonlar = {
    'ali':'Iphone x',
    'vali':'Samsung Galaxy S9',
    'olim':'Nokia 3310',
    'orif':'mi 10 pro',
    'maryam':'Iphone x',
    'sardor':'Samsung Galaxy S9',
    'rana':'Nokia 3310',
    'tohir':'Iphone x', 
    'umar':'Nokia 3310'
    }

#for k, q in telefonlar.items():
#    print(f'{k.title()} ning  yelefoni {q}')
    
print('Foydalanuvchilarning telefonlari:')
for tel in set(telefonlar.values()):
    print(tel)
