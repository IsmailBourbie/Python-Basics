# -*- coding: utf-8 -*-
"""
--*-- if elif else --*--
"""

baby_age = 2
adult_age = 15
x = int(input("your age: "))
if (x <= baby_age):
    print("you are an infant")
elif (x > baby_age and x <= adult_age):
    print("you are a child")
else:
    print("you are an adult")
