from classes import Automate, State
        
alphabet1 = ["a", "b", "c", "d"]
q0 = State("q0", True, False, {"a": ["q1"], "c": ["q3"]})
q1 = State("q1", False, False, {"b": ["q2"]})
q2 = State("q2", False, True, {})
q3 = State("q3", False, False, {"d": ["q4"]})
q4 = State("q4", False, True, {})
states = [q0, q1, q2, q3,q4]
automate1 = Automate(alphabet1, states, "automate1")


alphabet2 = ["a", "b"]
q5 = State("q5", True, False, {"a": ["q5"], "b": ["q6"]})
q6 = State("q6", False, True, {})
states = [q5, q6]
automate2 = Automate(alphabet2,states, "automate2")

        
def cartesian_product(automate1, automate2):
    # Création des nouveaux états du produit
    new_states = []
    for state1 in automate1.states:
        for state2 in automate2.states:
            new_name = state1.name + '_' + state2.name
            new_is_initial = state1.isInitial and state2.isInitial
            new_is_final = state1.isFinal and state2.isFinal
            new_transitions = {}
            
            # Combinaison des transitions des deux automates
            for symbol in automate1.alphabet:
                transitions1 = state1.transitions.get(symbol, [])
                transitions2 = state2.transitions.get(symbol, [])
                new_transitions[symbol] = [t1 + '_' + t2 for t1 in transitions1 for t2 in transitions2]

            new_states.append(State(new_name, new_is_initial, new_is_final, new_transitions))
    
    return Automate(automate1.alphabet + automate2.alphabet, new_states, f"{automate1.name} * {automate2.name}")

result_automate = cartesian_product(automate1, automate2)



def print_states(result_automate):
    for state in result_automate.states:
        transitions_str = ', '.join([f"{symbol}: {transitions}" for symbol, transitions in state.transitions.items() if transitions])
        if transitions_str or state.isInitial or state.isFinal:
            print(f"État : {state.name}")
            if transitions_str:
                print(f"Transitions : {transitions_str}")
            print(f"Est initial : {state.isInitial}")
            print(f"Est final : {state.isFinal}")
            print()

print_states(result_automate)
