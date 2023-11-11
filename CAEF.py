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
        
alphabet = ['a', 'b']


q0 = State("q0", True, False, {"a": "q3", "b": "q1"})
q1 = State("q1", False, False, {"a": "q1", "b": "q2"})
q2 = State("q2", False, True, {"a": "q7", "b": "q4"})
q3 = State("q3", False, True, {"a": "q7"})

states = [q0, q1, q2, q3]

automate = Automate(alphabet, states, "automate")


CAEF = automate
def make_completion(automate):
    for state in CAEF.states:
        state.isFinal = not state.isFinal
    return automate


def print_states(automate):
    for state in states:
        print(f"État : {state.name}")
        print(f"Transitions : {state.transitions}")
        print(f"Est initial : {state.isInitial}")
        print(f"Est final : {state.isFinal}")

print("États de l'automate avant la complétion :")
print_states(automate)
print("\n")
automate2 = make_completion(automate)
print("États de l'automate après la complétion :")
print("\n")
print_states(automate2)

