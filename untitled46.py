def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishidia qaytaruvchi funksiya"""
    malumotlar['kompaniya']= kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info("GM", "Malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "k5", rang='qizil', narh=35000, yil=2022, karobka='avtomat')