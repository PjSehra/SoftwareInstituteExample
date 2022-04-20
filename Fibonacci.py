# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:02:17 2022

@author: Jit
"""

file = open("filename.txt", "w")

for n in range(1,11):
    newline = "This is line " + str(n) + "\n"
    file.write(newline)

#fibonacci numbers

final_sequence = []

def Fibonacci(fibonacci_element):
    
    #FIRST 2 NUMBERS IN FIBONACCI SEQUENCE WILL BE 1
    if fibonacci_element == 0:
        final_sequence.append(1)
        return 1
    if fibonacci_element == 1:
        final_sequence.append(1)  
        return 1
    if fibonacci_element == 2:
        final_sequence.append(1)
        return 1
    else:
        final_number = Fibonacci(fibonacci_element-1) + Fibonacci(fibonacci_element-2) + Fibonacci(fibonacci_element-3)

        final_sequence.append(final_number)
        return final_number

fibonacci_element = input("Which element from the fibonacci sequence would you like to see?: ")    

print(Fibonacci(int(fibonacci_element)))
        


print(final_sequence)