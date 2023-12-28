from classes import Automate, State

def isDeterminist(automate):
    countitup=0
    for state in automate.states :
        for symbs, transi in state.transitions.items() :  #le symbs, transi correspond aux clés/valeurs du dictionnaire transitions, items()permet de les parcourir
            if len(transi)>1 :                            
                return False
        if state.isInitial == True :
            countitup+=1
    if countitup != 1 :
        return False
    return True
    
    if is_determinist :
        print("L'automate est déjà déterministe")
        
    else :
        yeepee=0
        while yeepee == 0:
            chogoice=input(print("Lautomate n'est pas déterministe. Voulez vous le déterminiser?\n1:oui 2:non"))
            match chogoice:
                case 1:automate=determining(automate);yeepee=1
                case 2:yeepee=1
                case _:print("Le choix n'existe pas, veuillez rééssayer.\n")

def determining(automate):
    allStates=[]#liste des nouveaux et anciens états, utile pour ordonner les fusions d'états
    statesList=[]#liste des états du nouvel automate
    test=0
    newName=[]#liste des noms d'états composant le nom d'un nouvel état fusion, me sert à chercher leurs transitions
    fusion=''#nom d'un état fusion
    newTransi={}#transition d'un nouvel état fusion
    automateName=""


    newTransiList=[]#chp
    namesList=[]#liste de strings, chp
    

    
    allStates=allStates+automate.states
    statesList.append(automate.state[0])


    namesList.append(automate.state[0].name)


    for state in statesList:

        for s in allStates:
            if state.name==s.name:
                test=1
                break
        if test==0:
            allStates.append(state)
        test=0


        for symb, transi in state.transitions.items():
            newName=list(transi)                                        #je recupere la liste des transitions de chaque état qui sera dans le nouvel automate, 1 par 1
            if len(newName>1) :
                newName=unify(newName)
                newName=ordo(allStates, newName)
                fusion=';'.join(newName)
            else :
                fusion=''.join(newName)
            

            for i in statesList:
                if fusion == i.name:
                    test=0
                    break
                else:test=1
            
            if test==0:
                continue
            if test==1 :
                namesList.append(fusion)
            test=0

            for i in newName :                                          #on va créer le dicto transi du nouvel état
                for s in allStates :                                    #on compare chaque etat du nouvel état avec les etats déja enregistrés
                    if i==s.name:
                        if s.isFinal :                                  #une fusion d'états dont un final est finale
                            IF=1                                      
                        if len(newTransi)==0:                           #s'ils sont égaux et que le dictionnaire est vide on remplace juste
                            test=1
                        else :
                            for symb, transi in s.transitions.items() : #si non, pour chaque symbole des vieux états, si le symbole existe deja dans le dico on fusionne les transis

                                for Symb, Transi in newTransi.items():
                                    if symb==Symb:
                                        Liste=Liste+Transi+transi
                                        print(Liste)
                                        Liste=unify(Liste)
                                        print(Liste)
                                        Liste=ordo(allStates,Liste)
                                        print(Liste)
                                        newTransi.update({Symb:Liste})
                                        Liste=[]
                                        print (newTransi)
                                        test=1
                                if test==0 :                            #si non on ajoute simplement le symbole et ses valeurs
                                    newTransi.update({symb : transi})
                                test=0
                        if test==1:
                            newTransi.update(s.transitions)
                            print(newTransi)
                        test=0
            newstate=State(fusion, False, IF, newTransi)
            statesList.append(newstate)
            IF=False
    return Automate(automate.alphabet, statesList, automate.name+"Determinised")



            
           
            


            



                





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
