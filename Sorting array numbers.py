# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:26:15 2022

@author: Jit
"""

array = []


number_of_elements = input("How many numbers would you like to input in your array: ")

for x in range(int(number_of_elements)):
    element = input("What number would you like to input in your array: ")
    array.append(int(element))
    
    
print(array)

for i in range(0, len(array)):
    for j in range(i+1, len(array)):
        if array[j] > array[i]:
            continue
        else:
            holding = array[j]
            array[j] = array[i]
            array[i] = holding
            
print("Ordered array: ", array)

