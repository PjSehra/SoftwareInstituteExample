# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:56:03 2022

@author: Jit
"""

no_seconds = input("What is the number of seconds you wish to input: ")

seconds_in_day = float(86400)
seconds_in_hour = float(3600)
seconds_in_minute = float(60)


def days(no_seconds):
    no_days = (float(no_seconds) // seconds_in_day)
    return (float(no_days))

def hours(no_seconds):    
    no_hours = float(no_seconds) - (float(days(no_seconds)) * seconds_in_day) // seconds_in_hour    
    return (float(no_hours))

def minutes(no_seconds):
    no_minutes = ((float(no_seconds)) - (float(days(no_seconds))) - (float(hours(no_seconds))) // seconds_in_minute)
    return (float(no_minutes))



print(days(no_seconds))
print(hours(no_seconds))
print(minutes(no_seconds))



no_days = (int(no_seconds) // seconds_in_day)

no_hours = (int(no_seconds) - (int(no_days) * seconds_in_day)) // seconds_in_hour

no_minutes = (int(no_seconds) - (int(no_days) * seconds_in_day) - (int(no_hours) * seconds_in_hour)) // seconds_in_minute

print("NUMBER OF DAYS: ", no_days)
print("NUMBER OF HOURS: ", no_hours)
print("NUMBER OF MINUTES: ", no_minutes)

