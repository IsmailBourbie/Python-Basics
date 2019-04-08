# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:21:50 2019

@author: Ismail Bourbie
"""
import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lname = name.split(" ")[-1]
        

    def get_lname(self):
        return self.lname
    
    def setBirthday(self, day, month, year):
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        if self.birthday == None:
            raise ValueError("Birthday is None")
        return (datetime.date.today() - self.birthday).days
    
    def __str__(self):
        return self.name
    