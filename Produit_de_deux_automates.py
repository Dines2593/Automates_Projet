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
q5 = State("q5", True, False, {"a" : ["q5"],"b": ["q6"]}) 
q6 = State("q6", False, True, {})
states = [q5, q6]
automate2 = Automate(alphabet2,states, "automate2")


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

result_automate = cartesian_product(automate1, automate2)

print("Automate 1")
print_states(automate1)
print("=========================================================================================================================================")
print("Automate 2")
print_states(automate2)
print("=========================================================================================================================================")
print("Automate Produit")
print_states(result_automate)

