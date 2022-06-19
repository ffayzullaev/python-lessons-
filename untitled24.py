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
        print(f"{til.upper()} ", end='')