# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:15:34 2019

@author: Ismail Bourbie
"""
import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
"""
plt.figure('linear')
plt.title("Linear")
plt.ylim(0, 1000)
plt.ylabel("linear func")
plt.xlabel("sample points")
plt.plot(mySamples, myLinear)

plt.figure('quadratic')
plt.title("Quadratic")
plt.ylim(0, 1000)
plt.ylabel("quadratic func")
plt.xlabel("sample points")
plt.plot(mySamples, myQuadratic)

plt.figure('cubic')
plt.title("Cubic")
plt.ylabel("cubic func")
plt.xlabel("sample points")
plt.plot(mySamples, myCubic)

plt.figure('exponential')
plt.title("Exponential")
plt.ylim(0, 1000)
plt.ylabel("exponential func")
plt.xlabel("sample points")
plt.plot(mySamples, myExponential)
"""
plt.figure("linear vs quadratic")
plt.clf()
plt.plot(mySamples, myLinear, label="Linear")
plt.plot(mySamples, myQuadratic, label="Quadratic") ## label for each graph
plt.legend(loc = "upper left") ## the place of legend

