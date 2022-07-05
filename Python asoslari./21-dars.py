print("Do'stlaringizni yoshini saqlaymiz, ")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingizni ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)
    
    javob = input("Yana malumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False
        
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshida")