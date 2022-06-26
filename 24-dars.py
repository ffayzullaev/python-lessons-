print("E bozor uchun ro'xat tuzamiz")
buyurtmalar = {}
ishora = True
while ishora:
    ism = input("Buyum nomini kiriting: ")
    narh = input("Buyum narhini kiriting: ")
    buyurtmalar[ism] = int(narh)
    
    javob = input("Yana buyurtma berasizmi? (ha/yo'q')")
    if javob == 'yo\'q':
        ishora = False
        
print("Buyurtmalar ro'yxati: ")
for ism, narh in buyurtmalar.items():
    print(f"{ism.title()} - {narh} ")
        