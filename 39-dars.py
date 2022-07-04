# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:26:01 2022

author: Fazliddin Fayzullaev
"""

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
    def get_name(self):
        return self.ism
    def last_name(self):
        return self.familiya
    def get_age(self,yil):
        return yil-self.tyil
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}, tug'lhan yilim {self.tyil}"
talaba1= Talaba("Olim", "Hakimov", 2002)
talaba2= Talaba("Ali", "Hakimov", 2002)
talaba3= Talaba("Hasan", "Hakimov", 2002)
