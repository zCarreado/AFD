from automata.fa.dfa import DFA

states = {f'qA{a}B{b}P{p}' for a in range(3) for b in range(2) for p in range(3)}
states.add('qTRAP')

final_states = {f'qA1B0P{p}' for p in range(3)}

transitions = {
    'qTRAP': {'a': 'qTRAP', 'b': 'qTRAP', 'c': 'qTRAP'}
}

for a in range(3):
    for b in range(2):
        for p in range(3):
            current_state = f'qA{a}B{b}P{p}'
            
            trans_a = f'qA{(a + 1) % 3}B{b}P1'
            
            trans_b = f'qA{a}B{(b + 1) % 2}P{2 if p == 1 else 0}'
        
            trans_c = f'qA{a}B{b}P0' if p == 2 else 'qTRAP'
            
            transitions[current_state] = {'a': trans_a, 'b': trans_b, 'c': trans_c}

dfa = DFA(
    states=states,
    input_symbols={'a', 'b', 'c'},
    transitions=transitions,
    initial_state='qA0B0P0',
    final_states=final_states
)

print(dfa.accepts_input('aababca'))