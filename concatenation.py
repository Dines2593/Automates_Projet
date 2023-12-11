from classes import Automate
from classes import State

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

#on affiche le new automate 
def print_states(result_automate):
    for state in result_automate.states:
        transitions_str = ', '.join([f"{symbol}: {transitions}" for symbol, transitions in state.transitions.items() if transitions])
        if transitions_str or state.isInitial or state.isFinal:
            print(f"État : {state.name}")
            if transitions_str:
                print(f"Transitions : {transitions_str}")
            print(f"Initial : {state.isInitial}")
            print(f"Final : {state.isFinal}")
            print()

# Exemple d'utilisation 
alphabet = ['a', 'b']

q0_A = State('q0', True, False, {'a': ['q3'], 'b': ['q1']})
q1_A = State('q1', False, False, {'a': ['q1'], 'b': ['q2']})
q2_A = State('q2', False, True, {})
q3_A = State('q3', False, True, {'a': ['q3']})
automatonA = Automate(alphabet, [q0_A, q1_A, q2_A, q3_A], 'autobahn')

alphabet_B = ['c', 'd']
q0_B = State('q4', True, False, {'c': ['q6'], 'd': ['q5']})
q1_B = State('q5', False, False, {'c': ['q5'], 'd': ['q4']})
q2_B = State('q6', False, True, {})
automatonB = Automate(alphabet_B, [q0_B, q1_B, q2_B], 'autoway')

# Fusionner les automates
concatenated_automate = concatenate_automate(automatonA, automatonB)

# Afficher le résultat de la fusion
print("\nAutomate résultant de la fusion (A.B):\n")
print_states(concatenated_automate)
