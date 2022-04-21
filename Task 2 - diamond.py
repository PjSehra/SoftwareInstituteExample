# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 09:09:57 2022

@author: Jit
"""

def diamond_shape(characters):
    number_of_characters = int(characters)
    length = round(number_of_characters/3)
    final_string = ""
    final_string += "*"
    
   
    for x in range(0,length):
        final_string += "*** \n"
        
    final_string += "*"
    
print(diamond_shape(5))

       
    