from classes import State
from classes import Automate

def emonde(automate):
    # Étape 1 : stocke les noms des états qui sont accessibles depuis l'état initial.
    necessary_state = set()

    # Étape 2 : Trouver les états accessibles depuis l'état initial, on l'ajoute à la pile, qui est utilisée pour suivre les états. 
    initial_state = [state for state in automate.states if state.isInitial][0]
    stack = [initial_state]

    # Ensuite, on entre dans une boucle while qui continue tant que la pile stack n'est pas vide et on retire un état de la pile 
    # => état nécessaire, car il est accessible depuis l'état initial
    while stack:
        current_state = stack.pop()
        necessary_state.add(current_state.name)

        # on parcourt les transitions sortantes de l'état actuel pour trouver les états vers lesquels il mène
        for transitions in current_state.transitions.values():
            for destination in transitions:
                state = [state for state in automate.states if state.name == destination][0]
                if state.name not in necessary_state:
                    stack.append(state)

    # Étape 3 : Filtrer les transitions pour exclure les états inutiles
    for state in automate.states:
        for symbol in list(state.transitions.keys()):
            # Pour chaque symbole de transition, supprime les destinations qui ne sont pas dans les noms d'états nécessaires
            state.transitions[symbol] = [dest for dest in state.transitions[symbol] if dest in necessary_state]

    # Étape 4 : Retourne la liste des états nécessaires
    necessary_states = [state for state in automate.states if state.name in necessary_state and state.name != 'q4']
    return necessary_states

# Affichage dans la console
def print_states(result_states):
    for state in result_states:
        transitions_str = ', '.join([f"{symbol}: {transitions}" for symbol, transitions in state.transitions.items() if transitions])
        if transitions_str or state.isInitial or state.isFinal:
            print(f"État : {state.name}")
            if transitions_str:
                print(f"Transitions : {transitions_str}")
            print(f"Est initial : {state.isInitial}")
            print(f"Est final : {state.isFinal}")
            print()

if __name__ == "__main__":
    # Example
    alphabet = ['a', 'b']

    q0 = State('q0', True, False, {'a': ['q3'], 'b': ['q1']})
    q1 = State('q1', False, False, {'a': ['q2']})
    q2 = State('q2', False, True, {'a': ['q2']})
    q3 = State('q3', False, True, {'a': ['q3'], 'b': ['q5']})
    q4 = State('q4', False, False, {'a': ['q2'], 'b': ['q1']})
    q5 = State('q5', False, False, {})

    automate = Automate(alphabet, [q0, q1, q2, q3, q4, q5], 'autobahn')

    # Appel de la fonction emonde
    result_states = emonde(automate)

    # Affichage de l'automate émondé
    print_states(result_states)
