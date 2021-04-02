# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 05:31:06 2021

@author: Data-Science
"""
import time
import math
import datetime
import sys

def wait(seconds:int):
    time.sleep(seconds)
    return

def my_sin(number:float):
    return math.sin(number)

def iso_now():
    return datetime.datetime.now()

#https://www.geeksforgeeks.org/python-now-function/

def platform():
    return sys.platform
#https://stackoverflow.com/questions/1854/python-what-os-am-i-running-on