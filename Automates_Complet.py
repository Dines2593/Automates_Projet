from classes import Automate
from classes import State

alphabet = ['a', 'b']
q0 = State('q0', True, False, {'a': 'q3', 'b': 'q1'})
q1 = State('q1', False, False, {'a': 'q1', 'b': 'q2'})
q2 = State('q0', True, False, {'a': 'q7', 'b': 'q4'})
q3 = State('q1', False, False, {'a': 'q7'})


states = [q0, q1, q2, q3]


def is_complete(self):
        is_complete=True
        for state in states:
            if state.isFinal:
                if set(state.transitions.keys()) != set(alphabet):
                    is_complete = False
                    print(f"L'état {state.name} n'est pas complet.")
                else:
                    print(f"L'état {state.name} est complet.")
            else:
                if set(state.transitions.keys()) != set(alphabet):
                    is_complete = False
                    print(f"L'état {state.name} n'est pas complet.")
                else:
                    print(f"L'état {state.name} est complet.")
        if is_complete:
            print("L'automate est complet.")
        else:
            print("L'automate n'est pas complet.")
        return is_complete 
is_complete(Automate)

