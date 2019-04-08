# -*- coding: utf-8 -*-
"""
Square root of number using NEWTON-RASPHON algorithm.
p = x² - number
guess - p(guess)/p'(guess)
"""

epsilon = 0.01
y = 24.0
guess = y/2
countGuesses = 0
while abs(guess*guess - y) >= epsilon:
    guess = guess - (((guess**2) - y)/ (2*guess))
    countGuesses += 1

print("Number of guesses:", countGuesses)
print('Square root of:', y, 'is about:', guess)