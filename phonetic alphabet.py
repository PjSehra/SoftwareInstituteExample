# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 09:45:16 2022

@author: Jit
"""

#Alpha, Bravo, Charli, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, 
#November, Oscar, PaPa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu

file = open("filename.txt")
text = file.read()


dictionary = {"A":'Alpha', "B":'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu', 'a':'alpha', 'b':'bravo','c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf','h':"hotel", 'i':'india', 'j':'juliet', 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'xray', 'y':'yankee', 'z':'zulu'}


#UNHASH THIS WHEN FINISHED
#sentence = input("What is your sentence: ")


def split(word):
    return list(word)


split_sentence = split(text)

index = 0
full_stop = "."
comma = ","
exclamation_mark = "!"
question_mark = "?"



# this part replaces the letter with the dictionary word
for characters in range(0, len(split_sentence)):
    
    if split_sentence[characters] not in (" ", "!", "?", ",", "."):
    
        temporary_word = split_sentence[characters]
        first_character = temporary_word[0]
        replaced_word = (dictionary[first_character]) 

        split_sentence[characters] = replaced_word
    
    else:
        continue
    


final_string = " "
for x in split_sentence:
    final_string += x + " "
        
print(final_string)
        
file = open("new_filename.txt", "w")
file.write(final_string)
            
file.close()


 