def katta_harf(matnlar):
    for m in range(len(matnlar)):
        matnlar[m]= matnlar[m].lower()
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()

ismlar = ["ali", "vali", "hasan", "husan"]
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)