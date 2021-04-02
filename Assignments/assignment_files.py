# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 05:46:33 2021

@author: Data-Science
"""

import os
import zipfile
   
#1   
def clean_cache():
    try:
        os.mkdir("/cache")
    except OSError:
        print('error')
        os.remove("/cache")

#https://stackabuse.com/creating-and-deleting-directories-with-python/
#https://www.geeksforgeeks.org/create-a-directory-in-python/#:~:text=Using%20os.-,mkdir(),to%20be%20created%20already%20exists.


#2        
def cache_zip(file_path:str, cache_path:str = '/cache'):
    os.mkdir("/cache")
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_path)

#https://stackoverflow.com/questions/3451111/unzipping-files-in-python

#3
def cache_files():
    for root, dirs, files in os.walk("."):
        for filename in files:
            return(os.getcwd()+ """\\""" + filename)
#https://stackabuse.com/python-list-files-in-a-directory/
        
#4
def find_password(paths):
    with open(paths) as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if "password" in line:
            return True
        else:
            return False

print(find_password('file.txt'))
        
#https://www.delftstack.com/howto/python/python-find-string-in-file/#:~:text=file%20in%20Python.-,Use%20the%20File%20readlines()%20Method%20to%20Find%20a%20String,the%20line%20in%20every%20iteration.
#

if __name__ == "__main__":
    clean_cache()