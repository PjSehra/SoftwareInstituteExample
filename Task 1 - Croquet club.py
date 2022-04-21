# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 09:01:30 2022

@author: Jit
"""

final_list = []

example_input = [[18,20], [45,2], [61,12], [37,6], [21,21], [78,9]]

for x in example_input:
    if x[0] >= 55:
        if x[1] > 7:
            final_list.append("Senior")
        else:
            final_list.append("Open")
    else:
        final_list.append("Open")
        
print(final_list)