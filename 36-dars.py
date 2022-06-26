def kopaytir(*sonlar):
    """Sonlarni bir biriga ko'paytirish funksiyasi"""
    kopaytirish = 1
    for son in sonlar:
        kopaytirish *= son
    return kopaytirish

print(kopaytir(20,1,2,1,2,1))