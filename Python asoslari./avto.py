# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 02:50:52 2022

author: Fazliddin Fayzullaev 
"""
from uuid import uuid4
class Avto:
    __num_avto=0
    def __init__(self,make,model,rang,yil,narh,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.__km=km
        self.__id=uuid4()
        Avto.__num_avto +=1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    def get_km(self):
         return self.__km
     
    def get_id(self):
         return self.__id
    def add_km(self,km):
        if km>=0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")

avto1 = Avto("GM", "Nexia3", "Oq", 2021, 18000)
avto2 = Avto("GM", "Malibu", "Qora", 2022, 42000)
avto3 = Avto("Gm", "Captiva", "Oq", 2021, 45000)
#print(Avto.get)            