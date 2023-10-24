from classes import Automate, State

class Question1:
    def menu(self):
        choice = int(input("Que souhaitez vous effectuer ? \n 1 - Saisir un AEF \n 2 - Importer un AEF à partir d'un fichier \n 3 - Modifier un AEF \n 4 - Sauvegarder un AEF dans un fichier \n 5 - Supprimer un AEF \n "))
        match choice:
            case 1:print("Saisir un AEF\n"); self.createAEF()
            case 2:print("Importer un AEF\n")
            case 3:print("Modifier un AEF\n")
            case 4:print("Sauvegarder un AEF\n")
            case 5:print("Supprimer un AEF\n")
            case _:print("Le choix n'existe pas, veuillez rééssayer.\n"); self.menu()

    def inputAlphabet(self):
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

    def inputStates(self,alphabet):
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

    def printAEF(self, automat):
        print(f"Alphabet : {automat.alphabet}\n")
        print("Etats : ")
        for i in range(len(automat.states)):
            print(f"( {automat.states[i].name} ); Transition : {automat.states[i].transitions}")

    def createAEF(self):
        alphabet = self.inputAlphabet()
        states = self.inputStates(alphabet)
        automat = Automate(alphabet, states)
        self.printAEF(automat)
        

alphabet = ['a', 'b']

q0 = State('q0', True, False, {'a':'q3', 'b':'q1'})
q1 = State('q1', False, False, {'a':'q1', 'b':'q2'})
q2 = State('q2', False, True, {})
q3 = State('q3', False, True, {'a':'q3'})

auto  = Automate(alphabet, [q0, q1, q2, q3])

def find_state_by_name(automat, name):
    for state in automat.states:
        if state.name == name:
            return state
    return None

def word_is_recognized(word, aef):
    temp_state = aef.states[0]
    for symbol in word:
        if(temp_state.transitions.get(symbol)):
            temp_state = find_state_by_name(aef,temp_state.transitions.get(symbol))
        else:
            continue
    return temp_state.isFinal
    
def main():
    print("Hello World!")
    question1 = Question1()
    is_knowned = word_is_recognized("ab", auto) #Renvoie true
    print(is_knowned)
    is_knowned = word_is_recognized("ba", auto) #Renvoie false
    print(is_knowned)
    #question1.menu()

if __name__ == "__main__":
    main()
