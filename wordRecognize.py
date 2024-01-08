"""
Function to verify if a word is recognize by an automata
"""
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
