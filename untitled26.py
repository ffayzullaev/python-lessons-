buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'tjoy':'Buxoro',
           'asar':['Al-jome\' as-sahih', 'Al-adab al-mufrad', 'At-tarix al-kabir']
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'tjoy':'Toshkent',
           'asar':['O\'tkan kunlar', 'Obid ketmon']
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'tjoy':"Farg'ona",
           'asar':['Qo\'shiqlarim sizga', 'O\'zbegim']
           }

navoiy = {'ism':'Alisher Navoiy',
          'tyil':1441,
          'tjoy':"Xirot",
          'asar':['Hamsa']
           }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    tyil= shaxs['tyil']
    asar= shaxs['asar']
    print(f"\n{ism}ning mashxur asarlari: ")
    for a in asar:
        print(a)