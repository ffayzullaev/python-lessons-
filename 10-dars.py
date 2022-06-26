<<<<<<< HEAD
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'turkiya':'ankara',
    'singapur':'sungapur',
    'italiya':'rim'
    }

country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
=======
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'turkiya':'ankara',
    'singapur':'sungapur',
    'italiya':'rim'
    }

country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
>>>>>>> 096811b0346d81f08ba8e74dcbdddde6f20c5035
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")