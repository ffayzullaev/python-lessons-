dostlar = {
    'ali':['Rambo', 'Terminator'],
    'vali':["O'rgimchak odam", "Taksi-2"],
    'maryam':['Ozodlik', 'Qochok' ]
    }

for dost, kino in dostlar.items():
    print(f"\n{dost.title()}ning sevimli kinlari :")
    for k in kino:
        print(k.upper())