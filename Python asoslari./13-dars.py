<<<<<<< HEAD
hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python', 'c++0']
        },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':'oliy',
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':2003,
             'malumot':"o'rta-maxsus",
             'tillar':['python', 'php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()} ",
          f"{info['tyil']}- yilda tug'ilgan. "
          f"Malumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi: ")
    for til in info['tillar']:
        print(til.upper())
=======
hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python', 'c++0']
        },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':'oliy',
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':2003,
             'malumot':"o'rta-maxsus",
             'tillar':['python', 'php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()} ",
          f"{info['tyil']}- yilda tug'ilgan. "
          f"Malumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi: ")
    for til in info['tillar']:
        print(til.upper())
>>>>>>> 62b726922790d0a0d95d631ea93ccfa21d87ec59
    