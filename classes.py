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

"""
# Exemple typique d'automates (PDF Automate page 10 du Teams PYTHON ):

alphabet = ['a', 'b']

q0 = State('q0', True, False, {'a':'q3', 'b':'q1'})
q1 = State('q1', False, False, {'a':'q1', 'b':'q2'})
q2 = State('q2', False, True, {})
q3 = State('q3', False, True, {'a':'q3'})

a = Automate(alphabet, [q0, q1, q2, q3])


"""
