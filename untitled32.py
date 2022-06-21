print("Yaqib do'stlaringizni ro'yxatini tuzamiz")
ismlar = []
n=1
while True:
    savol = f"{n} - do'stingizni kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qoshasizmi? (ha/yo'q) ")
    n+=1
    if takrorlash != 'ha':
        break
    
print("Do'stlaringizni ro'yxati:")
for ism in ismlar:
    print(ism.title())