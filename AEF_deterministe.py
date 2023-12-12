from classes import Automate, State

# Function to check if the automata is determinist : 
# Condition 1 : Only 1 initial state
# Condition 2 : 0 or 1 transition using a symbol of the alphabet for each state
def isDeterminist(automate):
    initState_count = 0
    for state in automate.states :
        for transi in state.transitions.values() :  #le symbs, transi correspond aux clés/valeurs du dictionnaire transitions, items()permet de les parcourir
            print(transi)
            if len(transi) != 0 and len(transi) != 1 :  # Condition 2 : Check for each state if there's only 0 or 1 transition                        
                return False    
        if state.isInitial == True :  # Check the first condition
            initState_count += 1
    # Condition 1 : Check if there is only 1 initial State
    if initState_count != 1 :
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

alphabet = ['a', 'b']

q0 = State('q0', True, False, {'a':['q3'], 'b':['q1']})
q1 = State('q1', False, False, {'a':['q1'], 'b':['q2']})
q2 = State('q2', False, True, {})
q3 = State('q3', False, True, {'a':['q3']})

a = Automate(alphabet, [q0, q1, q2, q3], "test")
if isDeterminist(a):
    print("oui")
else:
    print("non")