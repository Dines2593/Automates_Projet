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

    # Function to save the automata as an .json file
    def to_json(self):
        # Sérialiser l'objet en JSON et l'enregistrer dans un fichier
        automate_dict = self.to_dict()
        if(not os.path.exists("./my_automata")):
            os.makedirs("./my_automata")
        with open("./my_automata/"+self.name+".json", 'w') as json_file:
            json.dump(automate_dict, json_file, indent=4)
            print ("The file has been created")
    
            
    # Function to delete a json file
    def del_json(self):  
        # Verify if the path exist
        if(not os.path.exists("./my_automata")):
            print("The automata file is empty")
        else:
            try:  
                os.remove("./my_automata/"+self.name+".json")  # Delete the .json file
                print("The file has been removed")
            except:
                print("The file does not exist !")  # If there's no .json file 
    """
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
        with open("./my_automata/"+filename+".json", 'r') as json_file:
            automate_data = json.load(json_file)
        return cls.from_dict(automate_data)
    """
class State:
    def __init__(self, name, isInitial, isFinal, transitions):
        self.name = name
        self.isInitial = isInitial
        self.isFinal = isFinal
        self.transitions = transitions

def from_dict(automate_dict):
        # Créer une instance de la classe Automate à partir d'un dictionnaire
        name = automate_dict["name"]
        alphabet = automate_dict["alphabet"]
        states = [
            State(state_data["name"], state_data["isInitial"], state_data["isFinal"], state_data["transitions"])
            for state_data in automate_dict["states"]
        ]
        return Automate(alphabet, states, name)

def from_json(filename):
        # Lire les données du fichier JSON et créer une instance de la classe Automate
        if not os.path.exists("./my_automata/"+filename+".json"):
            return None
        with open("./my_automata/"+filename+".json", 'r') as json_file:
            automate_data = json.load(json_file)
        return from_dict(automate_data)

if __name__ == "__main__":
    # Exemple typique d'automates (PDF Automate page 10 du Teams PYTHON ):

    alphabet = ['a', 'b']

    q0 = State('q0', True, False, {'a':'q3', 'b':'q1'})
    q1 = State('q1', False, False, {'a':'q1', 'b':'q2'})
    q2 = State('q2', False, True, {})
    q3 = State('q3', False, True, {'a':'q3'})

    a = Automate(alphabet, [q0, q1, q2, q3], "test")

    a.to_json()  # Create the 'test.json'

    a.del_json()  # Delete the 'test.json' file




