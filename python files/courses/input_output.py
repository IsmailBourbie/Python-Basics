# -*- coding: utf-8 -*-
"""
Input/Output
"""

# output example using print() START:
x = 3
print(x) # print the value of x : 3
x_str = str(x) # casting x to string
print("my fav num is", x, ".", "x =", x) # , used to separated btw str and values
print("my fav num is " + x_str + " ." + " x = " + x_str) # + used to concatenate strs
# output example using print() END.

# input example using input() START:
name = input("type your name... ")
print(3*name) # repeat str 3 times

## PS: input return just string !!!!
num = int(input("type ur age: ")) # turn the input str to int
print("you were born on:", 2019 - num)

# input example using input() END:
