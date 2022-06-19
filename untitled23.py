car0 = {
        'model':'gentra',
        'rang':'qora',
        'yil':2013,
        'narh':18000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'malibu',
        'rang':'oq',
        'yil':2019,
        'narh':32000,
        'km':100,
        'korobka':'avtomat'
        }

car2 = {
        'model':'BMW',
        'rang':'qizil',
        'yil':2021,
        'narh':56000,
        'km':25000,
        'korobka':'avtomat'
        }

#car = car0
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']} - yil, {car['narh']}$")

#car = car1
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']} - yil, {car['narh']}$")

#car = car2
#print(f"{car['model'].title()}, "
#      f"{car['rang']} rang, "
#      f"{car['yil']} - yil, {car['narh']}$")


cars = [car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()}, "
#          f"{car['rang']} rang ",
#          f"{car['yil']}- yil, {car['narh']}$")

#print(f"{cars[2]['rang'].title()} "
#      f"{cars[2]['model']}")


malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang': None,
        'yil': 2020,
        'narh': None,
        'km':0, 
        'korobka':'avto'
    }   
    malibus.append(new_car)
    
#for malibu in malibus:
#    print(malibu)
    
for malibu in malibus[:3]:
    malibu['rang']='qizil'
    
#for malibu in malibus:    
#    print(malibu)

for malibu in malibus[3:6]:
    malibu['rang']='oq'

for malibu in malibus[6:]:
    malibu['rang']='qora'
    malibu['korobka']='mexanika'

#for malibu in malibus:
#        print(malibu)


for malibu in malibus:
    if malibu['korobka']=='avto':
       malibu['narh']=40000
    else:
        malibu['narh']=35000
        
for malibu in malibus:
    print(malibu)