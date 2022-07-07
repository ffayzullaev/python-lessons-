
"""
Created on Thu Jul  7 14:26:59 2022

author: Fazliddin Fayzullaev
"""
"""PYTHON STANDART KUTUBXONASI"""

import datetime as dt

## datetime()

hozir  = dt.datetime.now()
print(hozir)


print(hozir.hour)

## date()

bugun = dt.date.today()
print(f"Buguni sana: {bugun}")
ertaga = dt.date(2022, 7, 8)
print(f"Ertangi sana: {ertaga}")

## time()
hozir =dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat : {vaqtHozir}")
vaqtKeyin = dt.time(23,45,30)
print(vaqtKeyin)

## sanalar orasidagi farq

bugun = dt.date.today()
ramazon = dt.date(2022,7, 13)
farq = ramazon-bugun
print(farq)
print(f"Ramazongacha {farq.days} kun qoldi")

## soatlar orasidagi farq

hozir  = dt.datetime.now()
futbol = dt.datetime(2022, 8, 10, 23, 45, 00)
farq = futbol-hozir

sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga  {farq.days} kunu {soatlar} soat qoldi") 
