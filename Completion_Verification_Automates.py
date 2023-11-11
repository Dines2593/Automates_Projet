from classes import Automate
from classes import State

alphabet = ["a", "b"]
q0 = State("q0", True, False, {"a": "q3", "b": "q1"})
q1 = State("q1", False, False, {"a": "q1", "b": "q2"})
q2 = State("q2", False, True, {"a": "q7", "b": "q4"})
q3 = State("q3", False, True, {"a": "q7"})

states = [q0, q1, q2, q3]

automate = Automate(alphabet, states, "automate")


def make_complete(automate):
    if is_complete(automate) == True:
         print("L'automate est déja complet ou a été complété.")
         return
    else:
        phi_state = State("phi", False, False, {})
        automate.states.append(phi_state)
        #print_states(automate)
        for state in automate.states:
            for symbol in alphabet:
                if symbol not in state.transitions:
                    state.transitions[symbol] = "phi"
        #print_automate.states(automate)
        for state in automate.states:
            for symbol, target_state in state.transitions.items():
                if target_state == "phi":
                    state.transitions[symbol] = phi_state.name
        return automate

def is_complete(automate):
        is_complet=True
        for state in automate.states:
            if state.isFinal:
                if set(state.transitions.keys()) != set(alphabet):
                    is_complet = False
            else:
                if set(state.transitions.keys()) != set(alphabet):
                    is_complet = False
        if is_complet == True:
            print("L'automate est complet.")
        else:
            print("L'automate n'est pas complet.")
        return is_complet



def print_states(automate):
    for state in states:
        print(f"État : {state.name}")
        print(f"Transitions : {state.transitions}")
        print(f"Est initial : {state.isInitial}")
        print(f"Est final : {state.isFinal}")


print("États de l'automate avant la complétion :")
print_states(automate)
print("\n")
automate=make_complete(automate)
automate=make_complete(automate)
print("États de l'automate après la complétion :")
print("\n")
print_states(automate)



