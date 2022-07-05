# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 20:15:28 2022

author: Fazliddin Fayzullaev 
"""
class User:
    def __init__(self,user_name,toliq_ism,tyil,email):
        self.user_name=user_name
        self.toliq_ism=toliq_ism
        self.tyil=tyil
        self.email=email
    def get_name(self):
        return self.user_name
    def full_name(self):
        return self.toliq_ism
    def get_age(self,yil):
        return yil-self.tyil
    def get_email(self):
        return self.email
    def tanishtir(self):
        return f"Foydalanuvchi: {self.user_name}, ismi: {self.toliq_ism}, yoshi {self.tyil}, email: {self.email}"
        
user1 =User("@alijon1994", "Alijon Valiyev", 1994, "alijon1994@gmail.com")
user2 =User("@mansur1995", "Mansurjon Shamshiyev", 1995, "mansurjon1995@gmail.com")
user3 =User("@alisher2002", "Alisher Aliyev", 2003, "alisher2003@gmail.com")
user4 =User("@valijon2005", "Valijon Olimov", 2005, "valijon2005@gmail.com")
