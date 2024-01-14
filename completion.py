from classes import Automate
from classes import State

# Function to make an automata complete
def make_complete(automate):
    if is_complete(automate) == True:
         print("The automaton is already complete or has been completed")
         return automate
    else:
        # Create a phi state that will contains all the alphabet's symbol transitioning in himself
        phi_state = State("phi", False, False, {})  
        automate.states.append(phi_state)  # Add the phi state to the automata
        #print_states(automate)
        for state in automate.states:
            for symbol in automate.alphabet:
                if symbol not in state.transitions:
                    state.transitions[symbol] = "phi"  # Add "phi" for the alphabet's symbol who'is not in the actual state
        #print_automate.states(automate)
        for state in automate.states:
            for symbol, target_state in state.transitions.items():
                if target_state == "phi":
                    state.transitions[symbol] = phi_state.name
        return automate

def is_complete(automate):
    is_complet=True
    for state in automate.states:
        # We put "set()" to have the same type of value (exemple {'a', 'c'})
        if set(state.transitions.keys()) != set(automate.alphabet):
            is_complet = False
    if is_complet == True:
        print("The automaton is complete..")
    else:
        print("The automaton is not complete.")
    return is_complet



# Affichage dans la console
def print_states(automate):
    for state in automate.states:
        transitions_str = ', '.join([f"{symbol}: {transitions}" for symbol, transitions in state.transitions.items() if transitions])
        if transitions_str or state.isInitial or state.isFinal:
            print(f"État : {state.name}")
            if transitions_str:
                print(f"Transitions : {transitions_str}")
            print(f"Est initial : {state.isInitial}")
            print(f"Est final : {state.isFinal}")
            print()

if __name__ == "__main__":
    # exemple automata
    alphabet = ['a', 'b']

    q0 = State('q0', True, False, {'a': ['q3'], 'b': ['q1']})
    q1 = State('q1', False, False, {'a': ['q2']})
    q2 = State('q2', False, True, {'a': ['q2']})
    q3 = State('q3', False, True, {'a': ['q3'], 'b': ['q5']})
    q4 = State('q4', False, False, {'a': ['q2'], 'b': ['q1']})
    q5 = State('q5', False, False, {})

    automate = Automate(alphabet, [q0, q1, q2, q3, q4, q5], 'autobahn')

    print("The automaton is not complete :")
    print_states(automate)
    print("\n")
    automate=make_complete(automate)
    automate=make_complete(automate)
    print("The automaton is complete : ")
    print("\n")
    print_states(automate)



