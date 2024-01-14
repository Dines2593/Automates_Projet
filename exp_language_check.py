from classes import Automate, State

def get_initial_state(states):
    for state in states:
        if state.isInitial == True:
            return state
    return None

def get_state_by_name(target_name, states):
    for state in states:
        if state.name == target_name:
            return state
    return None

""" QUESTION 8 """
def automat_to_system(automat):
    system = ""
    for state in automat.states:
        left_member = f"{state.name.upper()} = "
        right_member = ""
        count = 0
        for transition in state.transitions:
            count += 1
            right_member += f"{transition}{state.transitions[transition][0].upper()}"
            if count < len(state.transitions): right_member += " + "

        if(state.isFinal):
            if count == 0 : right_member = "''"
            else: right_member += f" + ''"
        
        system += left_member + right_member + "\n"

    print(system)
    return system

def arden_lemma(Y, Z):
    return f"({Y})*{Z}"


def apply_arden_lemma(system):
    epsilon = "''"  # représentation du mot vide

    equations = system.split('\n')
    equations.pop()
    solutions = {}
    for eq in equations:
        parts = eq.split('=')
        if len(parts) >= 2:
            state = parts[0].strip()
            expression = parts[1].strip()
            
            if " + ''" in expression:
                expression.replace(" + ''", "")
                
            # Vérifier si l'équation est de la forme X = YZ
            if '+' in expression:
                Y, Z = map(str.strip, expression.split('+'))
                if(state in Y):
                    Y = Y.replace(state, "")
                    solution = arden_lemma(Y, Z)
                    solutions[state] = solution
                elif(state in Z):
                    Z = Z.replace(state, "")
                    Y, Z = Z, Y
                    solution = arden_lemma(Y, Z)
                    solutions[state] = solution
                else:
                    solutions[state] = expression
            else:
                solutions[state] = expression

            solutions[state] = solutions[state].replace(epsilon, '')
    
    return solutions


def replace_Q_with_solution(expression, solutions):
    for state, solution in solutions.items():
        expression = expression.replace(state, solution)
    return expression

def get_regular_expression(solutions):
    all_solutions = []
    for state, solution in solutions.items():
        replaced_solution = replace_Q_with_solution(solution, solutions)
        all_solutions.append(replaced_solution)

    print(all_solutions)
    return all_solutions[0]

def print_solutions(solutions):
    for state, solution in solutions.items():
        print(f"{state} = {solution}")

def get_expression(a):
    my_system = automat_to_system(a)

    solutions = apply_arden_lemma(my_system)
    
    final_expression = get_regular_expression(solutions)
    print(f"Regular expression of automata named {a.name} : {final_expression}")

""" QUESTION 8 END """

""" QUESTION 9 """
def get_language_from_exp(expression):
    expression = expression.replace("+", "∪")
    expression = expression.replace("(","∩")
    expression = expression.replace(")","∩")
    expression = expression.replace("∩*","*")
    return expression

def get_language(a):
    my_system = automat_to_system(a)

    solutions = apply_arden_lemma(my_system)
    
    final_expression = get_regular_expression(solutions)
    language = get_language_from_exp(final_expression)
    
    print(f"Language of automata named {a.name} : {language}")



def check_same_language(a, b):
    if(a.alphabet != b.alphabet):
        print(f"L'équivalence des automates {a.name} et {b.name} : {False}")
        return 
    
    language_a = get_language(a)
    language_b = get_language(b)
    print(f"L'équivalence des automates {a.name} et {b.name} : {language_a == language_b}")

#   Automate de test

"""
alphabet = ['a', 'b']

q0 = State('q0', True, False, {'a':['q3'], 'b':['q1']})
q1 = State('q1', False, False, {'a':['q1'], 'b':['q2']})
q2 = State('q2', False, True, {})
q3 = State('q3', False, True, {'a':['q3']})

a = Automate(alphabet, [q0, q1, q2, q3], 'autobahn')
a1 = Automate(alphabet, [q0, q1, q2, q3], 'autoaaabahn')

language = get_language(a)
language1 = get_language(a1)
"""
