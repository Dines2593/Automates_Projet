class State:
    def __init__(self, name, initial, final, transitions):
        self.name = name
        self.initial = initial
        self.final = final
        self.transitions = transitions

class Automate:
    def __init__(self, alphabet, states, name):
        self.alphabet = alphabet
        self.states = states
        self.name = name

    def mirror(self):
        mirrored_states = []

        # Inverser les états finaux et non finaux
        for state in self.states:
            mirrored_state = State(state.name, not state.final, not state.initial, {})
            mirrored_states.append(mirrored_state)

        # Inverser les transitions
        for state in mirrored_states:
            for symbol in self.alphabet:
                new_transitions = []
                for target_state in self.states:
                    if state.name in target_state.transitions.get(symbol, []):
                        new_transitions.append(target_state.name)
                state.transitions[symbol] = new_transitions

        # Créer et retourner l'automate miroir
        mirrored_automaton = Automate(self.alphabet, mirrored_states, self.name + '_mirror')
        return mirrored_automaton

# Exemple d'utilisation
alphabet = ['a', 'b']

q0 = State('q0', True, False, {'a': ['q3'], 'b': ['q1']})
q1 = State('q1', False, False, {'a': ['q1'], 'b': ['q2']})
q2 = State('q2', False, True, {})
q3 = State('q3', False, True, {'a': ['q3']})

automaton = Automate(alphabet, [q0, q1, q2, q3], 'autobahn')
mirrored_automaton = automaton.mirror()

# Afficher l'automate miroir
for state in mirrored_automaton.states:
    print(f"State: {state.name}, Initial: {state.initial}")
    print(f"Final: {state.final}, Transitions: {state.transitions}")
