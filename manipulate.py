from classes import Automate, State
import os


def menu():
    choice = int(input("Que souhaitez vous effectuer ? \n 1 - Saisir un AEF \n 2 - Importer un AEF à partir d'un fichier \n 3 - Modifier un AEF \n 4 - Sauvegarder un AEF dans un fichier \n 5 - Supprimer un AEF \n "))
    match choice:
        case 1:print("Saisir un AEF\n"); createAEF()
        case 2:print("Importer un AEF\n")
        case 3:print("Modifier un AEF\n")
        case 4:print("Sauvegarder un AEF\n")
        case 5:print("Supprimer un AEF\n")
        case _:print("Le choix n'existe pas, veuillez rééssayer.\n"); menu()

def inputAlphabet():
    can_input = True
    result = []
        
    while can_input:
        symbol = ""
        while len(symbol) != 1:
            symbol = input("Entrez un symbole valide de votre alphabet : ")
        keep_input = int(input("Voulez vous continuez ? : 0=Non, 1=Oui : "))
        result.append(symbol)
        if keep_input : can_input = True
        else : can_input = False

    return result

def inputStates(alphabet):
    result = []
    numOfStates = int(input("Veuillez entrer le nombre d'état de votre automate : "))
    q0 = State('q0', True, False, {})
    result.append(q0)
    for i in range(1,numOfStates):
        q = State(f'q{i}', False, False, {})
        result.append(q)

    choice_of_state = dict(zip( range(len(result)), [s.name for s in result]))
        
    for i in range(len(result)):
        q = result[i]
        if(i!=0) :
            isFinal = int(input("L'état est-il final ? : 0=Non, 1=Oui"))
            q.isFinal = bool(isFinal)
        for symbol in alphabet:
            can_add_transition = bool(int(input(f"Souhaitez vous créer une transition pour {symbol} ? : 0=Non, 1=Oui")))
            if not can_add_transition : continue
            else : 
                transition_key = int(input(f"Quel transition souhaitez-vous ajouter pour le symbole {symbol} ? \n {choice_of_state} \n"))
                q.transitions[symbol] = choice_of_state[transition_key]

    return result

def printAEF(automat):
    print(f"Alphabet : {automat.alphabet}\n")
    print("Etats : ")
    for i in range(len(automat.states)):
        print(f"( {automat.states[i].name} ); Transition : {automat.states[i].transitions}")

def createAEF():
    nom=input("How do you want to call the automate?")
    alphabet = inputAlphabet()
    states = inputStates(alphabet)
    automat = Automate(alphabet, states, nom)
    Print_states(automat)
    return automat
        
def print_states(result_automate):
    print(result_automate.alphabet)
    for state in result_automate.states:
        transitions_str = ', '.join([f"{symbol}: {transitions}" for symbol, transitions in state.transitions.items() if transitions])
        if transitions_str or state.isInitial or state.isFinal:
            print(f"État : {state.name}")
            if transitions_str:
                print(f"Transitions : {transitions_str}")
            print(f"Est initial : {state.isInitial}")
            print(f"Est final : {state.isFinal}")
            print()

def Print_states(automate):
    print(f"Alphabet : {automate.alphabet}")
    for state in automate.states:  # avant : for state in states :
        print(f"État : {state.name}")
        print(f"Transitions : {state.transitions}")
        print(f"Est initial : {state.isInitial}")
        print(f"Est final : {state.isFinal}")



if __name__ == "__main__":
    alphabet = ['a', 'b']

    q0 = State('q0', True, False, {'a':'q3', 'b':'q1'})
    q1 = State('q1', False, False, {'a':'q1', 'b':'q2'})
    q2 = State('q2', False, True, {})
    q3 = State('q3', False, True, {'a':'q3'})

    auto  = Automate(alphabet, [q0, q1, q2, q3], "auto")