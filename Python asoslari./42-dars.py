# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:18:38 2022

author: Fazliddin Fayzullaev
"""
from uuid import uuid4
class Avto:
    def __init__(self,make,model,rang,yil,narh,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.__km=km
        self.__id=uuid4()
    def get_km(self):
         return self.__km
     
    def get_id(self):
         return self.__id
    def add_km(self,km):
        if km>=0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")
            


