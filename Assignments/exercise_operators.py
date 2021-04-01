# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:39:48 2021

@author: Data-Science
"""

# 1
language_swiss = "German"
language_spain = "Spanish"
print(language_swiss == language_spain)

# 2
religion_swiss = "Roman Catholic"
religion_spain = "Roman Catholic"
print(religion_swiss == religion_spain)

# 3
print(len('Bern') != len('Madrid'))

# 4
print(67885 > 20900)

# 5
print(0.067 < 1 and 0.66 < 1)

# 6
print(8400000 > 10000000 or 50000000 > 10000000)

# 7
var_1 = (8400000 > 10000000)
var_2 = (50000000 > 10000000)
print(var_1 == True or var_2 == True and not var_1 == True and var_2 == True)

