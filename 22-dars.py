#cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
#while 'nexia' in cars:
#       cars.remove('nexia')
#print(cars)


talabalar = ['hasan', 'husan', 'ali', 'vali']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi: ")
    baholangan_talabalar[talaba] = int(baho)
    