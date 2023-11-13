from classes import Automate
from classes import State

#meme partie du code
class Automate:
    def __init__(self, alphabet, states, name):
        self.alphabet = alphabet
        self.states = states
        self.name = name


class State:
    def __init__(self, name, isInitial, isFinal, transitions):
        self.name = name
        self.isInitial = isInitial
        self.isFinal = isFinal
        self.transitions = transitions

#ajout du code miroir
def mirror(automate):
    mirrored_states = []

    # on parcours pour créer des états miroirs avec les mêmes noms, mais des transitions inversées
    for state in automate.states:

       # on inverse les clés et les valeurs des transitions. et on ajoute l'état miroir à la liste
        mirrored_transitions = dict(zip(state.transitions.values(), state.transitions.keys()))
        #Création directe de l'état miroir avec les transitions inversées.
        mirrored_state = State(state.name, state.isInitial, state.isFinal, mirrored_transitions)
        mirrored_states.append(mirrored_state)

    # Inverser les états initiaux et finaux
    for state in mirrored_states:
        state.isInitial, state.isFinal = state.isFinal, state.isInitial

    # Créer un nouvel automate miroir
    mirrored_automate = Automate(automate.alphabet, mirrored_states, f"{automate.name}_mirror")
    return mirrored_automate


#code pris dans completition_verification...
def print_states(automate):
    for state in automate.states:
        print(f"État : {state.name}")
        print(f"Transitions : {state.transitions}")
        print(f"Est initial : {state.isInitial}")
        print(f"Est final : {state.isFinal}")

#l'automate
alphabet = ['a', 'b']
q0 = State("q0", True, False, {"a": "q3", "b": "q1"})
q1 = State("q1", False, False, {"a": "q1", "b": "q2"})
q2 = State("q2", False, True, {"a": "q7", "b": "q4"})
q3 = State("q3", False, True, {"a": "q7"})

states = [q0, q1, q2, q3]
automate = Automate(alphabet, states, "automate")

# Appliquer la fonction make_mirror
mirrored_automate = mirror(automate)

# Afficher les états de l'automate original
print("Automate original:")
print_states(automate)

# Afficher l'automate miroir
print("\nAutomate miroir:")
print_states(mirrored_automate)
