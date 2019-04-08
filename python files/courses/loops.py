# -*- coding: utf-8 -*-
"""
--*-- loops --*--
"""

# While loop START:
number = input("guess a number btw 0 and 9: ")
while (number != "3"):
    number = input("Try another one: ")
print("yes the number is: " + number)
    
# While loop END:

# For loop START:
for i in range(5):
    print(i)

for i in range(3, 7): # range(start, end)
    print(i)
    

for i in range(2, 11, 2): # range(start, end, step)
    print(i)
    
# For loop END:
    
# GUESSE_CHECK exmaples START:
#___# square root example #___#

x = int(input('Enter an Integer: '))
answer = 0
negative_flag = False
if x < 0:
    negative_flag = True
while answer**2 < x:
    answer += 1
if x == answer**2:
    print("square root of " + str(x) + " is: " + str(answer))
else:
    print(x, "is not perfect square")
    if negative_flag == True:
        print("Just checking... did you mean ", -x, "?")
        
# GUESSE_CHECK exmaples END.