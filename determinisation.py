from classes import Automate, State

def is_determinist(automate):
    count=0
    for state in automate.states :
        for symbs, transi in state.transitions.items() :  #le symbs, transi correspond aux clés/valeurs du dictionnaire transitions, items()permet de les parcourir
            if len(transi)>1 :                            
                count+=1
                break
        if count != 0 :
            break
    if count == 0 :
        print("The automata is already determinist")
        return True    
    else :
        print("The automata is not determinist")
        return False

def make_determinist(automate):
    allStates = []  #liste des nouveaux et anciens états, utile pour ordonner les fusions d'états
    statesList = []  #liste des états du nouvel automate
    test = 0
    newName = []  #liste des noms d'états composant le nom d'un nouvel état fusion, me sert à chercher leurs transitions
    fusion = ''  #nom d'un état fusion
    newTransi = {}  #transition d'un nouvel état fusion
    Liste = []

    #namesList=[]  #liste de strings, chp
    if is_determinist(automate):
        allStates = allStates + automate.states
        statesList.append(automate.states[0])  # Ajout du premier etat de l'automate


        #namesList.append(automate.states[0].name)


        for state in statesList:

            for s in allStates:
                if state.name == s.name:
                    test=1
                    break
            if test==0:
                allStates.append(state)
            test=0


            for symb, transi in state.transitions.items():
                newName = list(transi)  #je recupere la liste des transitions de chaque état qui sera dans le nouvel automate, 1 par 1
                if len(newName)>1 :
                    newName = unify(newName)
                    newName = ordo(allStates, newName)
                    fusion = '_'.join(newName)  # Creer un string contenant tout les elements de newName avec '_' entre chaque element
                else :
                    fusion = transi[0]
                

                for i in statesList:
                    if fusion == i.name:
                        test=0
                        break
                    else:test=1
                
                if test==0:
                    continue
                test=0

                finalState = False  
                for i in newName :  #on va créer le dico transi du nouvel état
                    for s in allStates :  #on compare chaque etat du nouvel état avec les etats déja enregistrés
                        if i==s.name:
                            if s.isFinal :  #une fusion d'états dont un final est finale
                                finalState = True                                     
                            if len(newTransi) == 0:  #s'ils sont égaux et que le dictionnaire est vide on remplace juste
                                test = 1
                            else :
                                for symb, transi in s.transitions.items() : #si non, pour chaque symbole des vieux états, si le symbole existe deja dans le dico on fusionne les transis

                                    for Symb, Transi in newTransi.items():
                                        if symb == Symb:
                                            Liste = Transi + transi
                                            Liste = unify(Liste)
                                            Liste = ordo(allStates,Liste)
                                            newTransi.update({Symb:Liste})
                                            Liste=[]
                                            test=1
                                    if test==0 :                            #si non on ajoute simplement le symbole et ses valeurs
                                        newTransi.update({symb : transi})
                                    test=0
                            if test == 1:
                                newTransi.update(s.transitions)
                            test = 0
                newstate=State(fusion, False, finalState, newTransi)
                newTransi={}
                statesList.append(newstate)
            
        for state in statesList :
            for symb, transi in state.transitions.items():
                if len(transi)>1:
                    state.transitions.update({symb : ['_'.join(transi)]})
        for state in statesList :
            print(state.name)
            print(state.transitions)
            print('\n')
        return Automate(automate.alphabet, statesList, automate.name+"_Determinised")
    else:
        return automate

def unify(liste) : #supprime les doublons dans les liste de noms d'états
    i=0
    j=0
    while i < len(liste):
        while j < len(liste) :
            if i!=j :
                if liste[i]==liste[j]:
                    del liste[j]
                else : j+=1
            else :
                j+=1
        i +=1
        j=0
    return liste

def ordo(Liste1, Liste2):
    if len(Liste2)==1:return Liste2
    i=0
    while i<len(Liste2)-1:
        for c in range(len(Liste1)):
            if Liste1[c].name==Liste2[i]:
                for d in range(len(Liste1)):
                    if Liste1[d].name==Liste2[i+1]:
                        if d<c:
                            Liste2.append(Liste2[i])
                            del Liste2[i]
                            i=0
                            break
                        elif i+1<len(Liste2)-1 : 
                            i+=1
                        else:return Liste2

if __name__ == "__main__":
    alphabet = ['a', 'b']

    q0 = State('q0', True, False, {'a':['q1','q3'], 'b':['q1']})
    q1 = State('q1', False, False, {'a':['q2'], 'b':['q1']})
    q2 = State('q2', False, True, {'a': ['q2']})
    q3 = State('q3', False, True, {'a':['q3']})

    auto  = Automate(alphabet, [q0, q1, q2, q3],"auto")

    r0 = State('r0', True, False, {'a' :['r0'], 'b' : ['r0', 'r1']})
    r1 = State('r1', False, False, {'a': ['r2'], 'b': ['r2']})
    r2 = State('r2', False, True, {'a': ['r2'], 'b': ['r2']})

    auto2 = Automate(alphabet, [r0, r1, r2], "auto2")

    auto2 = is_determinist(auto2)
    is_determinist(auto2)
