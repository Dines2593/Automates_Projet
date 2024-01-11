import json 
import os
import networkx as nx
import matplotlib.pyplot as plt

from classes import Automate
from classes import State

from completion import *
from determinisation import *
from display import *
from manipulate import *
from otherOperations import *
from pruned import *
from wordRecognition import *

#menu central
def menu():
    Menu=1
    choice=""
    automate=Automate([],[],"")
    automate=Automate([],[],"")
    while Menu==1:                      #We make the menu loop every time
        choice=""
        for i in range (10):
            print("\n")  
        print("----------------------------")
        print("Select an option :")
        print("1. Create an automata (if an automata was already in use, it will be erased if not saved)") #1-1
        print("2. Import an automata (same)")                                                              #1-2
        print("3. Exit")
        print("----------------------------")

        option = input("Your choice>> ")
        match option:
            case "1":automate=createAEF()
            case "2":choice=input("What is the name of the automata you want to import?"),automate.from_json(choice)
            case "3":exit()
            case _:print("Choice not valid.\n")
        while Menu==1:
            for i in range (10):
                print("\n")  
            print("----------------------------")
            print("Select an option :")
            print("1. Verifications on an automata")
            print("2. Do an operation to an automata")
            print("3. Use an other automata")
            print("4. Delete the Automata")             #1-3
            print("5. Save the automata")               #1-4
            print("----------------------------")

            option = input("Your choice>> ")
            match option:
                case "1":verif(automate)
                case "2":operation(automate)
                case "3":Menu=0
                case "4":automate.del_json, Menu=0
                case "5":automate.to_json
                case _:print("Choice not valid.\n")
        Menu=1

def new_automate ():
    automate=Automate([],[],"")
    choice=""
    loop=1
    while loop==1 :
        for i in range (10):
            print("\n")  
            print("----------------------------")
            print("Select an option :")
            print("1. Create an automata")
            print("2. Import an automata (same)") 
            print("----------------------------")

            option = input("Your choice>> ")
            match option:
                case "1":automate=createAEF()
                case "2":choice=input("What is the name of the automata you want to import?"),automate.from_json(choice)
                case _:print("Choice not valid.\n")
    return automate


    

    

# menu pour acceder a toutes les verifications
def verif(automate):
    Menu=1
    word=""
    while Menu==1:
        for i in range (10):
            print("\n")
            
        print("#######################")
        print("Select a verification option :")
        print("1. Word recognition")                            #2
        print("2. Is the automata complete")                    #3
        print("3. Is the automata determinised")                #5
        print("4. What language is recognized")                 #9
        print("5. Are the automata and another one equivalent") #10
        print("6. Extract a regular expression")                #8
        print("7. Back")                            
        print("########################")

        option = input("Your choice>> ")
        match option:
            case "1":word=input("What word"),word_is_recognized(word, automate)
            case "2":is_complete(automate)
            case "3":is_determinist()
            case "4":
            case "5":automate2=new_automate(),
            case "6":
            case "7":Menu=0
            case _:print("Choice not valid.")

#menu pour acceder aux améliorations possibles
def operation(automate):
    Menu=1
    while Menu==1:
        for i in range (10):
            print("\n")

        print("|||||||||||||||||||||||||||")
        print("Select an option to improve the automata :")
        print("1. Do some modifications on the automata")    #1-5
        print("2. Make an automata complete")                #4
        print("3. Make an automata determinist")             #6
        print("4. Prune an automata")                        #11
        print("5. Concatenate 2 automatas")                  #7-4
        print("6. Product of 2 automatas")                   #7-3
        print("7. Mirror of the automata")                   #7-2
        print("8. Complement of the automata")               #7-1
        print("9. Back")                    
        print("|||||||||||||||||||||||||||")

        option = input("Your choice>> ")
        match option:
            case "1":
            case "2":make_complete(automate)
            case "3":make_determinist(automate)
            case "4":emonde(automate)
            case "5":automate2=new_automate,concatenate_automate(automate,automate2)
            case "6":automate2=new_automate,cartesian_product(automate,automate2)
            case "7":automate=mirror(automate.states,automate.alphabet,automate.name)
            case "8":make_completion(automate)
            case "9":Menu=0
            case _:print("Choice not valid")


