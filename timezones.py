# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:51:52 2022

@author: Jit
"""

from datetime import date

##################  using a dictionary

my_timezones = {"London": '15:53:55', "Tokyo": '23:53:55', "New York": '10:53:55'}

timezone_input = input("What is the name of the timezone you wish to seek: ")


print(my_timezones[timezone_input])


#################   using a 2d list

number_of_timezones = input("How many timezones do you wish to enter: ")

list_timezone = []

index = 0

#This actually gives the user the choice of which timezones they wish to add times for in their own specified list

for x in (0, range(int(number_of_timezones))):

    timezone_name = input("What is the timezone name you wish to enter: ")
    timezone = input("What is the time: ")    

    if index == "0":
        list_timezone[0] = [timezone_name, timezone]
        
    else:    
        list_timezone.append([timezone_name, timezone])
        
    
    index += 1

print ("Here is your specified time zone list: ", list_timezone)

print("Here are the timezones: ", list_timezone)



    