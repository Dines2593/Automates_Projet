from classes import Automate, State

def determine(automate):
    is_determinist = True
    for state in automate.states :
        for symbs, transi in state.transitions.items() :  #le symbs, transi correspond aux clés/valeurs du dictionnaire transitions, items()permet de les parcourir
            if len(transi)>1 :                            
                is_determinist = False
                break
    
    if is_determinist :
        print("L'automate est déjà déterministe")
        
    else :

        print("pas deter")


    

    
