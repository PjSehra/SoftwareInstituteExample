# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 13:14:42 2022

@author: Jit
"""

from abc import ABC, abstractmethod


#Vet - staff members - (attributes) name, age, job role : (methods) get name, get age, get job role
#Treat animal (going to take in an animal, and staff member) - examine, treat wounds, surgery, x-ray 


class Staff_Members(ABC):
    
    
    def __init__(self, name, age, job_role):
        self.name = name
        self.age = age
        self.job_role = job_role
        

    def display_name(self):
        print("The name of the staff member is: ", self.name)
        
    def display_age(self):
        print("This is the age of the staff member: ", self.age)
        
    def display_job_role(self):
        print("The job role is: ", self.job_role)
        #job role includes - examiner, surgeon, radiographer(x-rays)
        
    


class Animal(ABC):

    #Attributes
    

    #Constructors
    def __init__(self):
        self.value = "Animal"


    #Methods
    @abstractmethod
    def reproduce(self):
        pass

    @abstractmethod
    def eat(self):
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
    def eat(self):
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
    def eat(self):
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
        print(self.value)

    def eat(self):
        print("I eat mice")
        

class Treatment():
    
    def calculate_price(treatment):
        
        for animal in self.animals:
            if animal.value == "Mammal":
                
                if treatment == "examine":
                    print("The cost is...")
                    
                if treatment == "treat wounds":
                    print("The cost is...")
                    
                if treatment == "surgery":
                    print("The cost is...")
                

            elif animal.value == "Arachnid":
                
                if treatment == "examine":
                    print("The cost is...")
                    
                if treatment == "treat wounds":
                    print("The cost is...")
                    
                if treatment == "surgery":
                    print("The cost is...")
                
                print("The cost is...")
        
        print("The cost is...")
        return 100
    
    def __init__(self, treatment_type):
        self.animals = []
        self.staff = []
        self.treatment_type = treatment_type
        
    
    def add_animals(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)
        
        


    
staff_members_available = input("What staff member would you like to treat your animal?: ") #must be a staff member of all job roles available

surgeon = Staff_Members("Jennifer Lopez", 50, "surgeon")
examiner = Staff_Members("Mariah Carey", 50, "examiner")

animal = input("What is the animal you wish to treat?: ")

if animal == "Cat":
    cat_object = Cat()

treatment = input("What is the treatment you wish for your animal to receive?: ")

treatment_of_animal = Treatment(treatment)

treatment_of_animal.add_animals(animal)
    
  


