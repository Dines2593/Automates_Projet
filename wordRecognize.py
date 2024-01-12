"""
Function to verify if a word is recognize by an automata
"""

from classes import *

def stateFinder(automata, stateName):
    # Function to find a state using the state's name 
    for state in automata.states:
        if state.name == stateName:
            return state
    return None

def wordRecognizeRec(automata, state, word):
    if word == "":
        return state.isFinal  # If the ending state is final, then the word is recognized (true)
    firstSymb = word[0]  # the first letter of the word
    for symbol, trans in state.transitions.items():
        if firstSymb == symbol:
            for potentialState in trans:  # For each transition using the same symbol
                nextState = stateFinder(automata, potentialState)  # stateFinder will turn the name "potentialState" into a real state
                if nextState != None:
                    if wordRecognizeRec(automata, nextState, word[1:]) :  # Call back the same word without the first letter
                        return True         
    return False

def wordRecognize(automata, word):
    # Function that will call the recursive function to check if the word is recognize, for EVERY initial state
    check = 0  # Value that will count the number of initial state
    for state in automata.states:  
        if state.isInitial:  # Call the function if the state is initial
            if wordRecognizeRec(automata, state, word):  
                print(f"The automate recognize the word (starting state: {state.name})")  
            else: 
                print(f"The automate DON'T recognize the word (starting state: {state.name})")
            check += 1  
    if check == 0:  # If there's no initial state in the automata...
        print("There is no initial state, the automata can't recognize the word")


if __name__ == "__main__":
    # Example
    alphabet = ['a', 'b']

    q0 = State('q0', True, False, {'a': ['q3'], 'b': ['q1']})
    q1 = State('q1', False, False, {'a': ['q2']})
    q2 = State('q2', False, True, {'a': ['q2']})
    q3 = State('q3', False, True, {'a': ['q3'], 'b': ['q5']})
    q4 = State('q4', False, False, {'a': ['q2'], 'b': ['q1']})
    q5 = State('q5', False, False, {'b': ['q4']})

    automate = Automate(alphabet, [q0, q1, q2, q3, q4, q5], 'autobahn')

    r0 = State('r0', True, False, {'a': ['r0'], 'b': ['r1']})
    r1 = State('r1', False, True, {'a': ['r0'], 'b': ['r1']})
    r2 = State('r2', True, True, {'a': ['r1'], 'b': ['r0']})

    automate2 = Automate(alphabet, [r0, r1, r2], 'automate2')

    wordRecognize(automate2, "aab")