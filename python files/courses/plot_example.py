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
    

plt.figure('linear')
plt.plot(mySamples, myLinear)

plt.figure('quadratic')
plt.plot(mySamples, myQuadratic)

plt.figure('cubic')
plt.plot(mySamples, myCubic)

plt.figure('exponential')
plt.plot(mySamples, myExponential)