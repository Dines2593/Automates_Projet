import unittest

class State:
    def __init__(self, name, isInitial, isFinal, transitions):
        self.name = name
        self.isFinal = isFinal
        self.isInitial = isInitial
        self.transitions = transitions

class Automate:
    def __init__(self, alphabet, states, name):
        self.alphabet = alphabet
        self.states = states
        self.name = name
      # Trouver l'état initial
        self.initial_state = next((state for state in states if state.isInitial), None)

    def accept(self, input_string):
        if not self.initial_state:
            return False
        current_state = self.initial_state
        for char in input_string:
            if char in current_state.transitions:
                current_state = next((state for state in self.states if state.name == current_state.transitions[char]), None)
                if not current_state:
                    return False
            else:
                return False
        return current_state.isFinal

class TestAutomate(unittest.TestCase):
    def test_accept(self):
        alphabet = ['a', 'b']
        states = [
            State('q0', True, False, {"a": "q1"}),
            State('q1', False, True, {"b": "q0"}),
        ]
        name = 'TestAutomate'
        automate = Automate(alphabet, states, name)
       
       #ACCEPTE
        self.assertTrue(automate.accept("aba"))  # L'automate devrait accepter "ab"


        # REFUS
        self.assertFalse(automate.accept("")) 
        self.assertFalse(automate.accept("b")) 

if __name__ == '__main__':
    unittest.main()
