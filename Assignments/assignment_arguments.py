# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 22:15:45 2021

@author: Data-Science
"""

# https://board.wincacademy.nl/unit/view/id:7987

# Part 1: Greet Template
def greet (name:str = '<name>', greeting_template:str = 'Hello, '):
    return print(str(f'{greeting_template}{name}!'))

if __name__ == '__main__':
    greet()
    
# Part 2: Force
def force (mass:float, body:str = 'earth'):
    return body.lower(), round(mass*9.8, 1)

print(force(10, 'moon'))

#Part 3: Gravity
def pull (m1:float, m2:float, d:float):
    return round(9.8 * ((m1 * m2**2)/d**2),1)

print(pull(10,20,30))