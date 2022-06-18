davlatlar = {
    'AQSh':'Washington D.C.',
    'Singapur':'Singapur',
    'Turkiya':'Ankara',
    'O\'zbekiston':'Toshkent',
    'Rossiya':'Moskva'
    }
print("Dunyo davlatlari: ")
for d in sorted(davlatlar):
    print(d.upper())
print("\nDunyo davlatlari poytaxtlari")
for p in sorted(davlatlar.values()):
    print(p.title())