from classes import Automate, State


#Fonctions générique

def printAEF(automat):
    print(f"Name of the automaton : {automat.name}")
    print(f"Alphabet : {automat.alphabet}\n")
    print("States : ")
    for i in range(len(automat.states)):
        state = automat.states[i]
        initial_marker = " (Initial)" if state.isInitial else ""
        final_marker = " (Final)" if state.isFinal else ""
        print(f"State {state.name}{initial_marker}{final_marker}; Transitions : {state.transitions}")

    print("\n")


def get_state_by_name(target_name, states):
    for state in states:
        if state.name == target_name:
            return state
    return None

def state_exists(state_name, state_array):
    for state in state_array:
        if state.name == state_name:
            return True
    return False

def get_initial_state(states):
    for state in states:
        if state.isInitial:
            return state
    return None

def get_final_states(states):
    return [state for state in states if state.isFinal]



def create_automat():
    states = []
    alphabet = []
    transitions = []  # Pour stocker les transitions dans une liste

    print("You choosed : 'Create an automaton'.")
    automate_name = input("Enter the name of the automaton : ")

    # Demander à l'utilisateur l'état initial et l'état final
    initial_state_name = input("Enter the initial state of the automaton (Only one) : ")

    # Vérification si l'utilisateur a entré plusieurs valeurs avec ','
    if ',' in initial_state_name:
        print("\033[91mError : A finite automaton only have one initial state and several final state.\033[0m\n")
        return                  
        
    if ' ' in initial_state_name:
        print("\033[91mError : A finite automaton only have one initial state and several final state.\033[0m\n")
        return
        
    initial_state = State(initial_state_name, True, False, {})
    states.append(initial_state)

    final_state_string = input("Enter the final state(s) of the automaton (separated with comma ','): ")
        
    if ' ' in final_state_string:
        print("\033[91mError : A finite automaton only have one initial state and several final state.\033[0m\n")
        return
        
    final_states = final_state_string.split(',')
    
    for state in final_states:
        new_state = State(state, False, True, {})
        states.append(new_state)

    # Demander à l'utilisateur de saisir les transitions sous forme de matrice
    print("\nEnter your automaton transitions in matrix form (separated with space ' ') :")
    print("To finish the process put 'ok'\n")
    
    
    #on effectue une boucle tant qu'il n'appuie pas sur ok on continu
    while True:
        transition_input = input()
        if transition_input == 'ok':
            break
        else: #et on regarde la forme 
            transition_data = transition_input.split()
            if len(transition_data) != 3:
                print("\033[91mError : Invalid transition format.\033[0m")
            else:
                transitions.append(transition_data)
    #Création de l'automate en fonctions des données enregistrées dans les listes
    for transition in transitions:
        starting_state_name = transition[0]
        ending_state_name = transition[1]

        if not state_exists(starting_state_name, states):
            #print("Il existe pas le starting")
            new_starting_state = State(transition[0], False, False, {})
            states.append(new_starting_state)
        if not state_exists(ending_state_name, states):
            #print("Il existe pas le ending")
            new_ending_state = State(transition[1], False, False, {})
            states.append(new_ending_state)

        if not transition[2] in alphabet:
            alphabet.append(transition[2])

        updated_state = get_state_by_name(transition[0], states)
        if transition[2] in updated_state.transitions:
            updated_state.transitions[transition[2]].append(transition[1])
        else:
            updated_state.transitions[transition[2]] = []
            updated_state.transitions[transition[2]].append(transition[1])
    
    new_auto = Automate(alphabet,states, automate_name)
    print("Automaton created successfully !")
    return new_auto
   
# Fonction modify_automate

def edit_automat(automat):
    print("You choosed 'Modify an automaton'.")
    
    states = []
    alphabet = []
    transitions = []  # Pour stocker les transitions dans une liste

    automate_name = input(f"Enter the automaton's name (current name : {automat.name}): ")

    # Demander à l'utilisateur l'état initial et l'état final
    initial_state_name = input(f"Enter the initial state of the automaton (Only one) (current state : {get_initial_state(automat.states).name}) : ")

    # Vérification si l'utilisateur a entré plusieurs valeurs avec ','
    if ',' in initial_state_name:
        print("\033[91mError : A finite automaton only have one initial state and several final state.\033[0m\n")
        return
    
    initial_state = State(initial_state_name, True, False, {})
    states.append(initial_state)

    final_state_string = input(f"Enter the final state(s) of the automaton (current state(s) : {', '.join([state.name for state in get_final_states(automat.states)])}) (separated with comma ',') : ")
    final_states = final_state_string.split(',')
    
    for state in final_states:
        new_state = State(state, False, True, {})
        states.append(new_state)

    # Demander à l'utilisateur de saisir les transitions sous forme de matrice
    print("\nEnter your automaton transitions in matrix form (separated with space ' ') :")
    print("|!|\nBy modifying this automaton, you create a new one. The old one will be erased.\nTo stop the modification process, please put 'stop'.\n|!|")
    print("To finish the process put 'ok'\n")
    
    #on effectue une boucle tant qu'il n'appuie pas sur ok on continu
    while True:
        transition_input = input()
        if transition_input == 'ok':
            break
        if transition_input == 'stop':
            print("The editing is canceled")
            return automat
        else: #et on regarde la forme 
            transition_data = transition_input.split()
            if len(transition_data) != 3:
                print("\033[91mError : Invalid transition format.\033[0m")
            else:
                transitions.append(transition_data)
    #Création de l'automate en fonctions des données enregistrées dans les listes
    for transition in transitions:
        starting_state_name = transition[0]
        ending_state_name = transition[1]

        if not state_exists(starting_state_name, states):
            #print("Il existe pas le starting")
            new_starting_state = State(transition[0], False, False, {})
            states.append(new_starting_state)
        if not state_exists(ending_state_name, states):
            #print("Il existe pas le ending")
            new_ending_state = State(transition[1], False, False, {})
            states.append(new_ending_state)

        if not transition[2] in alphabet:
            alphabet.append(transition[2])

        updated_state = get_state_by_name(transition[0], states)
        if transition[2] in updated_state.transitions:
            updated_state.transitions[transition[2]].append(transition[1])
        else:
            updated_state.transitions[transition[2]] = []
            updated_state.transitions[transition[2]].append(transition[1])
    
    new_auto = Automate(alphabet,states, automate_name)
    print("Automaton successfully modified !")
    return new_auto

"""
def deleteAEF():
    if(len(AUTOMATES) == 0):
        print("Vous n'avez aucun automate dans cette session. Veuillez en créer un dans un premier temps. \n")
        return
    for i in range(len(AUTOMATES)):
        print(f"AUTOMATE N°{i+1} : \n")
        printAEF(AUTOMATES[i])
    
    chosen_aef = int(input("Veuillez entrer le numéro de l'automate que vous souhaitez modifier : "))

    if not (0<=chosen_aef-1<=len(AUTOMATES)):
        chosen_aef = int(input("Numéro invalide. Veuillez entrer le numéro de l'automate que vous souhaitez modifier : "))
    AUTOMATES.pop(chosen_aef-1)
    
    for i in range(len(AUTOMATES)):
        print(f"AUTOMATE N°{i+1} : \n")
        printAEF(AUTOMATES[i])
"""
