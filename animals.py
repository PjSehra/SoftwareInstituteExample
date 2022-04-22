# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 08:57:17 2022

@author: Jit
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes
    

    #Constructors
    def __init__(self):
        self.value = "Animal"


    #Methods
    

    @abstractmethod
    def eat(self, Animal):
        pass

    def sleep(self):
        print("I am sleeping")

    def type(self):
        print(self.value)

class Mammal(Animal):
    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Mammal"


    #Methods
    @abstractmethod
    def eat(self, Animal):
        pass
    
    def reproduce(self):
        print("Live Birth")

    def sleep(self):
        print("I am sleeping now")

    def type(self):
        print(self.value)
        

class Arachnid(Animal):
    
    def __init__(self):
        self.value = "Arachnid"
        
    #Methods
    @abstractmethod
    def eat(self, Animal):
        pass
    
    def reproduce(self):
        print("Live Birth")

    def sleep(self):
        print("I am sleeping now")

    def type(self):
        print(self.value)


class Cat(Mammal):
     #Attributes


    #Constructors
    def __init__(self):
        self.value = "Cat"


    #Methods
    def type(self):
        return self.value

    def eat(self):
        print("I eat mice")
        


class Big_Fish(Animal):
    
    def __init__(self):
        self.value = "Big Fish"
        
    
    def type(self):
        return self.value
        
    def eat(self, Animal):
        
        if Animal.type() == "Little Fish":
            return True

        else:
            return False            
        
        print("I can eat little fish")
        
        
class Little_Fish(Animal):
    
    def __init__(self):
        self.value = "Little Fish"
        
    def type(self):
        return self.value
        
    def eat(self, Animal):
        print("I cannot eat anything")
        

class Antelope(Animal):
    
    
    def __init__(self):
        self.value = "Antelope"
    
    def type(self):
        return self.value
        
    def eat(self, Animal):
        
        if Animal.type() == "Grass":
            return True
        
        else:
            return False
        
#        print("I can eat grass")
    

class Grass():
    
    def __init__(self):
        self.value = "Grass"
        
    def type(self):
        return self.value

    def eat(self, Animal):
        ("I cannot eat anything")
        
        
class Bug(Animal):
    
    def __init__(self):
        self.value = "Bug"
        
    def type(self):
        return self.value

    def eat(self, Animal):
        
        if Animal.type() == "Leaf":
            return True
        
        else:
            return False
        
#        ("I can eat leaves")


class Leaf():
    
    def __init__(self):
        self.value = "Leaf"
        
    def type(self):
        return self.value

    def eat(self, Animal):
        ("I cannot eat anything") 
        

class Bear(Animal):
    
    def __init__(self):
        self.value = "Bear"
        
    def type(self):
        return self.value

    def eat(self, Animal):
        
        if Animal.type() == "Big Fish":
            return True
        
        if Animal.type() == "Bug":
            return True
        
        if Animal.type() == "Chicken":
            return True
        
        if Animal.type() == "Cow":
            return True
        
        if Animal.type() == "Leaf":
            return True
        
        if Animal.type() == "Sheep":
            return True
        
        else:
            return False
        
#        ("I can eat: big-fish, bug, chicken, cow, leaf, sheep")
        

class Chicken(Animal):
    
    def __init__(self):
        self.value = "Chicken"
        
    def type(self):
        return self.value


    def eat(self, Animal):
        
        if Animal.type() == "Bug":
            return True
        
        else:
            return False
        

class Cow(Animal):
    
    def __init__(self):
        self.value = "Cow"
        
    def type(self):
        return self.value

    def eat(self, Animal):
        
        if Animal.type() == "Grass":
            return True
        
        else:
            return False
        

class Sheep(Animal):
    
    def __init__(self):
        self.value = "Sheep"
        
    def type(self):
        return self.value

    def eat(self, Animal):
        
        if Animal.type() == "Grass":
            return True
        
        else:
            return False
        
        

class Fox(Animal):
    
    def __init__(self):
        self.value = "Fox"
        
    def type(self):
        return self.value

    def eat(self, Animal):
                
        
        if (Animal.type() == "Chicken"):            
            return True
        
        if (Animal.type() == "Sheep"):
            return True
            
        else:
            return False



class Giraffe(Animal):
    
    def __init__(self):
        self.value = "Giraffe"
        
    def type(self):
        return self.value

    def eat(self, Animal):
        
        if Animal.type() == "Leaf":
            return True
        
        else:
            return False
            
        
        
class Lion(Animal):
    
    def __init__(self):
        self.value = "Lion"
        
    def type(self):
        return self.value

    def eat(self, Animal):
        
        if Animal.type() == "Antelope":
            return True
        
        if Animal.type() == "Cow":
            return True
        
        else:
            return False
        
        

class Panda(Animal):
    
    def __init__(self):
        self.value = "Panda"
        
    def type(self):
        return self.value

    def eat(self, Animal):
        
        if Animal.type() == "Leaf":
            return True
        
        else:
            return False
        
        
#fox = Fox()
#sheep = Sheep()
#chicken = Chicken()
#panda = Panda()

#print("TYPE : ", chicken.type())

#print(fox.eat(sheep))
#print(fox.eat(panda))
#print(fox.eat(chicken))


array = ["Fox", "Bug", "Chicken", "Grass", "Sheep"]
final_array = []
final = []




for x in range(0,len(array)):
    
    temporary_animal = array[x]
    
    if (temporary_animal == "Big Fish"):
        Big_Fish = Big_Fish()
        temporary_animal = Big_Fish
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Little Fish"):
        Little_Fish = Little_Fish()
        temporary_animal = Little_Fish
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Bug"):
        Bug = Bug()
        temporary_animal = Bug
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Leaf"):
        Leaf = Leaf()
        temporary_animal = Leaf
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Bear"):
        Bear = Bear()
        temporary_animal = Bear
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Antelope"):
        Antelope = Antelope()
        temporary_animal = Antelope
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Grass"):
        Grass = Grass()  
        temporary_animal = Grass
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Chicken"):
        Chicken = Chicken()
        temporary_animal = Chicken
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Cow"):
        Cow = Cow()
        temporary_animal = Cow
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Fox"):
        Fox = Fox()
        temporary_animal = Fox
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Sheep"):
        Sheep = Sheep()
        temporary_animal = Sheep
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Giraffe"):
        Giraffe = Giraffe()
        temporary_animal = Giraffe
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Lion"):
        Lion = Lion()
        temporary_animal = Lion
        final_array.append(temporary_animal)
        
    elif (temporary_animal == "Panda"):
        Panda = Panda()
        temporary_animal = Panda
        final_array.append(temporary_animal)
        
    else:
        continue


for x in range(0,len(final_array)):
    
    temporary_animal = final_array[x]
    
    for j in range(0,len(final_array)):
        
        testing_eating_animal = final_array[j]
        
        print(temporary_animal.value)
        print(testing_eating_animal.value)

        #temporary_animal = Fox
        #testing_eating_animal = Bug
        
        print(temporary_animal.eat(testing_eating_animal))

        if (temporary_animal.eat(testing_eating_animal) == True):
            print(temporary_animal.value)
            print(testing_eating_animal.value)
            final.append(temporary_animal.value + " eats " + testing_eating_animal.value)
            
        else:
            
            final.append(temporary_animal.value + " can't eat " + testing_eating_animal.value)


#for x in range(0,len(final_array)):
    
#    temporary_animal = final_array[x]
    
#    for j in range(x+1,len(final_array)):
        
#        testing_eating_animal = final_array[j]
        
#        temporary_string = ""
        
        
#        print(temporary_animal.value)
#        print(testing_eating_animal.value)

        
#        print(temporary_animal.eat(testing_eating_animal))

#        if (temporary_animal.eat(testing_eating_animal) == True):
#            print(temporary_animal.value)
#            print(testing_eating_animal.value)
#            final.append(temporary_animal.value + " eats " + testing_eating_animal.value)
            
#        else:
            
#            final.append(temporary_animal.value + " can't eat " + testing_eating_animal.value)
        
print(final)
            
            
    
