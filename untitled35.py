print("Buyurtmani kititing: ")
buyurtmalar = []
n=1
while True:
    savol = f"{n} chi buyurtmani kiriting: "
    nom = input(savol)
    buyurtmalar.append(nom)
    takrorlash = input("Yana buyurtma berasizmi? (ha/yo'q')")
    n+=1
    if takrorlash != 'ha':
        break

print("Buyurtmalaringizni ro'yxati: ")
for nom in buyurtmalar:
    print(nom.title())