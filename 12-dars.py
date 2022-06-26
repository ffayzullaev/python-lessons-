<<<<<<< HEAD
dasturchilar = {
    'ali':['python', 'c++'],
    'vali':['html', 'css', 'js'],
    'hasan':['php', 'sql'], 
    'husan':['python', 'php'],
    'maryam':['c++', 'c#']         
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi ")
    for til in tillar:
=======
dasturchilar = {
    'ali':['python', 'c++'],
    'vali':['html', 'css', 'js'],
    'hasan':['php', 'sql'], 
    'husan':['python', 'php'],
    'maryam':['c++', 'c#']         
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi ")
    for til in tillar:
>>>>>>> 62b726922790d0a0d95d631ea93ccfa21d87ec59
        print(f"{til.upper()} ", end='')