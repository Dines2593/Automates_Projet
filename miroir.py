from classes import State, Automate
from affichage import draw_automaton

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

q0 = State('q0', True, False, {'a': ['q3'], 'b': ['q1']})
q1 = State('q1', False, False, {'a': ['q1'], 'b': ['q2']})
q2 = State('q2', False, True, {})
q3 = State('q3', False, True, {'a': ['q3']})

automaton = Automate(alphabet, [q0, q1, q2, q3], 'autobahn')
mirrored_automaton = mirror(automaton.states, automaton.alphabet, automaton.name)

print_states(mirrored_automaton)
draw_automaton(mirrored_automaton)
