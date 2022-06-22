def mijoz_info ( ismi, familiyasi, tyili, t_joyi, email, raqami):
    mijoz = {'ismi':ismi,
             'familiyasi': familiyasi,
             'yosh': 2022 - tyili,
             't_joyi': t_joyi,
             'email': email,
             'raqami': raqami,
             }
    return mijoz


print('Mijoz haqidagi malumotlarni kiriting\n')
mijozlar = []
while True:
    ismi = input("Ismi: ")
    familiyasi = input("Familiyasi: ")
    tyili = int(input("yosh : "))
    t_joyi = input("T_joyi: ")
    email = input("Email: ")
    raqami = input("raqami: ")
    mijozlar.append(mijoz_info(ismi, familiyasi, tyili, t_joyi, email, raqami))
    javob = input("Davom etasizmi: (yes/no)")
    if javob == 'no':
        break


print("Mijoz haqidagi malumotlar: ")
for mijoz in mijozlar:
    print(
        f"Ismi {mijoz['ismi'].title()}   familiyasi {mijoz['familiyasi'].title()}\n"
        f"Yoshi {mijoz['yosh']} tug'ilgan joyi {mijoz['t_joyi'].title()}\n"
        f"emaili {mijoz['email']}   raqami {mijoz['raqami']}\n"
        )S