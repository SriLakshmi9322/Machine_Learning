# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 21:43:51 2022

@author: HP
"""

#In python, strings can be stored in Double Quotes/Single Quotes
nameDQ = "Sreeni DQ"
print(type(nameDQ))

nameSQ = 'Sreeni SQ'
print(type(nameSQ))

#Access string content
name = 'Sreeni DS'
print(name[0])

#slicing
print(name[0:5])

#Modify string content
name = name + 'xyz' #You can concatinate
print(name)

#Replace function
name = name.replace(name, name.upper())
print(name)

#instance: Check for instance comparision
isinstance(name, str) 
isinstance(name, int) 