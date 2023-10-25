from classes import Automate
from classes import State

alphabet = ['a', 'b']
q0 = State('q0', True, False, {'a': 'q3', 'b': 'q1'})
q1 = State('q1', False, False, {'a': 'q1', 'b': 'q2'})
q2 = State('q2', True, False, {'a': 'q7', 'b': 'q4'})
q3 = State('q3', False, False, {'a': 'q7', 'b' : 'phi'})


states = [q0, q1, q2, q3]


def is_complete(Automate):
        is_complete=True
        for state in states:
            if state.isFinal:
                if set(state.transitions.keys()) != set(alphabet):
                    is_complete = False
            else:
                if set(state.transitions.keys()) != set(alphabet):
                    is_complete = False
        if is_complete == True:
            print("L'automate est complet.")
        else:
            print("L'automate n'est pas complet.")
        return is_complete 
is_complete(Automate)



