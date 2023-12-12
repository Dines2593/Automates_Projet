from classes import Automate, State

def isDeterminist(automate):
    countitup=0
    for state in automate.states :
        for symbs, transi in state.transitions.items() :  #le symbs, transi correspond aux clés/valeurs du dictionnaire transitions, items()permet de les parcourir
            if len(transi)>1 :                            
                return False
        if state.isInitial == True :
            countitup+=1
    if countitup != 1 :
        return False
    return True
    
    if is_determinist :
        print("L'automate est déjà déterministe")
        
    else :
        yeepee=0
        while yeepee == 0:
            chogoice=input(print("Lautomate n'est pas déterministe. Voulez vous le déterminiser?\n1:oui 2:non"))
            match chogoice:
                case 1:automate=determining(automate);yeepee=1
                case 2:yeepee=1
                case _:print("Le choix n'existe pas, veuillez rééssayer.\n")

def determining(automate):
    statesList=[]
    transList=[]
    for stagate in automate.states :
        if stagate.isInitial == True :
            statesList.append(stagate)
            break
    for state in automate.states :
        for symbs, transi in state.transitions.items() :  #le symbs, transi correspond aux clés/valeurs du dictionnaire transitions, items()permet de les parcourir
            print('aah')
