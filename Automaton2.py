from automata.fa.dfa import DFA

dfa = DFA(
    states={
        'q0','q1','q2','q3','q4','q5','q6','q7','q8',
        'q9','q10','q11','q12','q13','q14','q15','q16','q17','trap'
    },

    input_symbols={'a','b','c'},

    transitions={
        'q0': {'a': 'q7', 'b': 'q3', 'c': 'trap'},
        'q1': {'a': 'q7', 'b': 'q5', 'c': 'trap'},
        'q2': {'a': 'q7', 'b': 'q3', 'c': 'q0'},

        'q3': {'a': 'q10', 'b': 'q0', 'c': 'trap'},
        'q4': {'a': 'q10', 'b': 'q2', 'c': 'trap'},
        'q5': {'a': 'q10', 'b': 'q0', 'c': 'q3'},

        'q6': {'a': 'q13', 'b': 'q9', 'c': 'trap'},
        'q7': {'a': 'q13', 'b': 'q11', 'c': 'trap'},
        'q8': {'a': 'q13', 'b': 'q9', 'c': 'q6'},

        'q9': {'a': 'q16', 'b': 'q6', 'c': 'trap'},
        'q10': {'a': 'q16', 'b': 'q8', 'c': 'trap'},
        'q11': {'a': 'q16', 'b': 'q6', 'c': 'q9'},

        'q12': {'a': 'q1', 'b': 'q15', 'c': 'trap'},
        'q13': {'a': 'q1', 'b': 'q17', 'c': 'trap'},
        'q14': {'a': 'q1', 'b': 'q15', 'c': 'q12'},

        'q15': {'a': 'q4', 'b': 'q12', 'c': 'trap'},
        'q16': {'a': 'q4', 'b': 'q14', 'c': 'trap'},
        'q17': {'a': 'q4', 'b': 'q12', 'c': 'q15'},

        'trap': {'a':'trap','b':'trap','c':'trap'}
    },

    initial_state='q0',

    final_states={'q6', 'q7', 'q8'}
)

print(dfa.accepts_input('aababca'))
