import json 
import os

from classes import Automate, State, from_json, from_dict

from completion import is_complete, make_complete
from determinisation import make_determinist, is_determinist, ordo, unify
# from display import draw_automaton
from manipulate import create_automat, edit_automat, printAEF
from otherOperations import make_completion, mirror, cartesian_product, concatenate_automate
from pruned import emonde
from wordRecognize import word_recognize, wordRecognizeRec, stateFinder  
from exp_language_check import get_expression, get_language, check_same_language



#menu central
def menu():
    Menu=1
    choice=""
    automate=Automate([],[],"")
    #automate=Automate([],[],"")
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

        wrongChoice = True
        while wrongChoice:
            option = input("Your choice>> ")
            match option:
                case "1":
                    automate=create_automat()
                    wrongChoice = False
                case "2":
                    choice=input("What is the name of the automata you want to import?\n")
                    temp = from_json(choice)
                    if(temp != None):
                        automate = temp
                        wrongChoice = False
                    else:
                        print("The file does not exist")
                        wrongChoice = True

                case "3":exit()
                case _:print("Choice not valid. Please select the right choice.\n")


        while Menu==1:
            for i in range (10):
                print("\n")  
            print("----------------------------")
            print("Select an option :")
            print("1. Verifications on an automata")
            print("2. Do an operation to an automata")
            print("3. Use an other automata ")
            print("4. Delete the Automata")             #1-3
            print("5. Save the automata")               #1-4
            print("----------------------------")

            option = input("Your choice>> ")
            match option:
                case "1":
                    verif(automate)
                case "2":automate = operation(automate)
                case "3":Menu=0
                case "4":
                    automate.del_json()
                    Menu=0
                case "5":
                    automate.to_json()
                    print("The automata json file has been created")
                case _:print("Choice not valid.\n")
        Menu=1

def new_automate():
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
                case "1":
                    automate=create_automat()
                    return automate
                case "2":
                    choice=input("What is the name of the automata you want to import?")
                    automate = from_json(choice)
                    return automate
                case _:print("Choice not valid.\n")
    


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
            case "1":
                word=input("What word")
                word_recognize(automate, word)
            case "2":is_complete(automate)
            case "3":is_determinist(automate)
            case "4": get_language(automate)
            case "5": 
                automate2 = new_automate()
                check_same_language(automate, automate2)
            case "6": get_expression(automate)
            case "7": Menu=0
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
                automate = edit_automat(automate)
                printAEF(automate)
            case "2":
                automate = make_complete(automate)
                printAEF(automate)
            case "3":
                automate = make_determinist(automate)  # Function to determin an automata
                printAEF(automate)
            case "4":
                automate = emonde(automate)
                printAEF(automate)
            case "5":
                automate2=new_automate() 
                automate = concatenate_automate(automate,automate2)
                printAEF(automate)
            case "6":
                automate2=new_automate()
                automate = cartesian_product(automate,automate2)
                printAEF(automate)
            case "7":
                automate=mirror(automate.states,automate.alphabet,automate.name)
                printAEF(automate)
            case "8":
                automate = make_completion(automate)
                printAEF(automate)
            case "9":
                Menu=0
                return automate
            case _:print("Choice not valid")

if __name__ == "__main__":
    menu()
