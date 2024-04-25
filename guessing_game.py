# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 17:19:09 2024

@author: Clus1986
"""

from random import randint 

guess_is = randint(1,100)
num_guesses = 0 

while True: 
    result = int(input('Guess a number 1-100: '))
    num_guesses +=1 

    if result == guess_is:
        print(f"Congrats your number {result} is correct!")
        break 
    elif result <1 or result >100:
        print('Out of Bounds')
         
    elif abs(result - guess_is)<=10: 
        print("warm")
         
    elif abs(result-guess_is)>10:
        print('cold')
         
    else:
        print('Try again')