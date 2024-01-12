"""
from classes import Automate
from classes import State
"""
class Automate:
    def __init__(self, alphabet, states,name):
        self.alphabet = alphabet
        self.states = states
        self.name = name

class State:
    def __init__(self, name, isInitial, isFinal, transitions):
        self.name = name
        self.isInitial = isInitial
        self.isFinal = isFinal
        self.transitions = transitions
    

def make_completion(automate):
# Function to create a completion automate, every final state of the automata is reversed
    for state in automate.states:  # avant : for state in CAEF.states:
        state.isFinal = not state.isFinal
    return automate

def mirror(states, alphabet, name):
    mirrored_states = []

    # Inverser les états finaux et non finaux
    for state in states:
        mirrored_state = State(state.name, state.isFinal, state.isInitial, {})
        mirrored_states.append(mirrored_state)

    # Mettre à jour les transitions des états miroirs
    #pour chaque etat de l'etat miroir, et pour chaque symbole de l'alphabet alors on le met dans une transition 
    for state in mirrored_states:
        for symbol in alphabet:
            new_transitions = []
            for target_state in states:
                if state.name in target_state.transitions.get(symbol, []):
                    new_transitions.append(target_state.name)
            state.transitions[symbol] = new_transitions

    # Créer et retourner l'automate miroir
    mirrored_automaton = Automate(alphabet, mirrored_states, name + '_mirror')
    return mirrored_automaton

def cartesian_product(automate1, automate2):
    # Création des nouveaux états du produit
    new_states = []

    # Créer un ensemble des états finaux de automate2
    final_states_automate2 = {state.name for state in automate2.states if state.isFinal}
    final_states_automate1 = {state.name for state in automate1.states if state.isFinal}

    for state1 in automate1.states:
        for state2 in automate2.states:
            new_name = state1.name + '_' + state2.name
            new_is_initial = state1.isInitial and state2.isInitial
            new_is_final = (state1.name in final_states_automate1 and state2.name in final_states_automate2)

            # Combinaison des transitions des deux automates
            new_transitions = {}
            for symbol in automate1.alphabet:
                transitions1 = state1.transitions.get(symbol, [])
                transitions2 = state2.transitions.get(symbol, [])
                combined_transitions = [t1 + '_' + t2 for t1 in transitions1 for t2 in transitions2]
                new_transitions[symbol] = combined_transitions

            # Vérifier si l'état a des transitions entrantes (sauf pour l'état initial)
            has_incoming_transitions = any(new_name in t for t in sum([transitions for other_state in new_states for transitions in other_state.transitions.values()], []))

            # Ajouter l'état au produit cartésien s'il a des transitions entrantes, sortantes ou est initial
            if new_is_initial or has_incoming_transitions or any(combined_transitions for combined_transitions in new_transitions.values()):
                new_states.append(State(new_name, new_is_initial, new_is_final, new_transitions))

    return Automate(automate1.alphabet + automate2.alphabet, new_states, f"{automate1.name} * {automate2.name}")

def concatenate_automate(automatonA, automatonB):
    # Étape 1 : Créer un nouvel alphabet en combinant les alphabets des deux automates
    alphabet_concat = list(set(automatonA.alphabet + automatonB.alphabet))

    # Créer une copie des états des deux automates
    statesA_copy = [State(state.name, state.isInitial, state.isFinal, state.transitions.copy()) for state in automatonA.states]
    statesB_copy = [State(state.name, state.isInitial, state.isFinal, state.transitions.copy()) for state in automatonB.states]

    # Étape 2 : Modifier l'automate A
    for state in statesA_copy:
        if state.isFinal:
            # Recherchez l'état initial de l'automate B
            initial_state_B = next(stateB for stateB in statesB_copy if stateB.isInitial)
            # Créez une transition ε vers l'état initial de B depuis l'état final de A
            state.transitions['ε'] = [initial_state_B.name]
            state.isFinal = False

    # Étape 3 : Modifier l'automate B pour que l'etat initial devient juste un etat basique
    for state in statesB_copy:
        if state.isInitial:
            state.isInitial = False

    # Créer l'automate concaténé
    concatenated_states = statesA_copy + statesB_copy
    concatenated_automaton = Automate(alphabet_concat, concatenated_states, 'concatenated')

    return concatenated_automaton

def print_states(automate):
    for state in automate.states:  # avant : for state in states :
        print(f"État : {state.name}")
        print(f"Transitions : {state.transitions}")
        print(f"Est initial : {state.isInitial}")
        print(f"Est final : {state.isFinal}")

if __name__ == "__main__":
    alphabet = ['a', 'b']


    q0 = State("q0", True, False, {"a": "q3", "b": "q1"})
    q1 = State("q1", False, False, {"a": "q1", "b": "q2"})
    q2 = State("q2", False, True, {"a": "q7", "b": "q4"})
    q3 = State("q3", False, True, {"a": "q7"})

    states = [q0, q1, q2, q3]

    automate = Automate(alphabet, states, "automate")
    print("États de l'automate avant la complétion :")
    print_states(automate)
    print("\n")
    automate2 = make_completion(automate)
    print("États de l'automate après la complétion :")
    print("\n")
    print_states(automate2)

