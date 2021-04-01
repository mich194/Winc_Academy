# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:05:07 2021

@author: Data-Science
"""
#PART 1

#1
gullit = "Ruud Gullit"
van_basten = "Marco van Basten"

#2
goal_0 = 32
goal_1 = 54

#3
scorers = gullit + str(goal_0), van_basten, str(goal_1)

#4
report = (f'{gullit} scored in the {goal_0}nd minute\
          \n{van_basten} scored in the {goal_1}th minute')
print(report, '\n')

#PART 2

#1
player = gullit

#2
first_name = player[player.find('Ruud'):player.find('Ruud')+4]
print(first_name, '\n')

#3
last_name_len = len(player[player.find('Gullit'):])
print(last_name_len)

#4
name_short = player[0]+". "+ player[player.find('Gullit'):]
print(name_short)

#5
chant = len(first_name) * "{first_name}!"

#6
good_chant = print(chant[-1] != " ")