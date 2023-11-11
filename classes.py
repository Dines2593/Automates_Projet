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
import json 
import os

class Automate:
    def __init__(self, alphabet, states, name):
        self.alphabet = alphabet
        self.states = states
        self.name = name

    def to_dict(self):
        # Convertir l'objet Automate en un dictionnaire
        automate_dict = {
            "alphabet": self.alphabet,
            "name" : self.name,
            "states": [
                {
                    "name": state.name,
                    "isInitial": state.isInitial,
                    "isFinal": state.isFinal,
                    "transitions": state.transitions
                }
                for state in self.states
            ]
        }
        return automate_dict

    def to_json(self, filename):
        # Sérialiser l'objet en JSON et l'enregistrer dans un fichier
        automate_dict = self.to_dict()
        if(not os.path.exists("./mes_automates")):
            os.makedirs("./mes_automates")
        with open("./mes_automates/"+filename, 'w') as json_file:
            json.dump(automate_dict, json_file, indent=4)

    @classmethod
    def from_dict(cls, automate_dict):
        # Créer une instance de la classe Automate à partir d'un dictionnaire
        alphabet = automate_dict["alphabet"]
        states = [
            State(state_data["name"], state_data["isInitial"], state_data["isFinal"], state_data["transitions"])
            for state_data in automate_dict["states"]
        ]
        return cls(alphabet, states)

    @classmethod
    def from_json(cls, filename):
        # Lire les données du fichier JSON et créer une instance de la classe Automate
        with open("./mes_automates/"+filename, 'r') as json_file:
            automate_data = json.load(json_file)
        return cls.from_dict(automate_data)

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


