#Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
#Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def Talabalar(ism, familiya,**malumotlar):
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar

talaba1 = Talabalar("Fazliddin", "Fayzlullaev", yosh=18)
talaba2 = Talabalar("Jam", "Mavlonov", yosh=18, bolim='informatika', t_joy='Toshkent')
talaba3 =Talabalar("Ozod", "Buron",)