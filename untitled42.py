#Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
def hisobla (radius, pi=3.14):
    data = {'radius':radius,
            'pi':3.14
        }
    return data
    
print("Radiusini qabul qilib olib, uning radiusini, diametrini, perimetri  qaytaruvchi funksiya")
dannie = []
while True:
    radius = int(input("Radiusni kiriting: "))
    dannie.append(hisobla(radius))
    break

for  data in dannie:
    print(f"diametr {data['radius']*2}\n"
          f"perimetr {data['radius']*2*3.14}\n"
          f"yuza {data['radius']**2*3.14}"
          )