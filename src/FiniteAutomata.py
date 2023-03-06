import networkx as nx
import matplotlib.pyplot as plt

#class to define a FA
class FiniteAutomata:
    def __init__(self, Q, alphabet, transition, q0, F):
        self.Q = Q
        self.alphabet = alphabet
        self.transition = transition
        self.q0 = q0
        self.F = F

    # get the next state
    def transition_to(self, state, symbol):
        return self.transition[(state, symbol)]

    #validation function
    def validation(self, word):
        current_state = self.q0
        #going through each symbol in word
        for symbol in word:
           #checking if there is any transition from the current state on the current symbol
            if (current_state, symbol) not in self.transition:
                return False
            current_state = self.transition_to(current_state, symbol)
        return current_state in self.F

    #convert finite automaton to grammar
    def fa_to_rg(self, Q, Sigma, delta, q0, F):
        #start symbol
        S = 'S'
        #nonterminal values
        nonterminals = {q: f'{q}' for q in Q}

        #add production rules for each transition
        productions = []
        for (q, a), ps in delta.items():
            for p in ps:
                A = nonterminals[q]
                B = nonterminals[p]
                productions.append(f'{A} -> {a}{B}')

        #add production rules for each final state
        for f in F:
            B = nonterminals[f]
            productions.append(f'{B} -> epsilon')

        #define inital production rule
        A = nonterminals[q0]
        productions.append(f'{S} -> {A}')

        return '\n'.join(productions)

    #function to determine if the finite automaton is DFA of NFA
    def is_deterministic(self, delta):
        for state in delta:
            inputs = set(symbol for symbol, _ in delta[state])
            if len(inputs) < len(delta[state]):
                print("NFA- nondeterministic")

                return 0
        print("DFA- deterministic")

    #function to convert NFA to DFA if the finite automaton is DFA of NFA
    def nfa_to_dfa(self, Q, Sigma, delta, q0, F):
        print("\nConvert NFA to DFA\n")

        #create a dictionary for the new states
        dfa_delta = {}
        dfa_Q = set()

        #compute the epsilon closure of the initial state
        q0_closure = self.epsilon_closure(q0, delta)
        dfa_Q.add(frozenset(q0_closure))

        #compute the transitions for each set of states
        unmarked_states = [frozenset(q0_closure)]
        while unmarked_states:
            q_set = unmarked_states.pop()
            print(f"Processing state: {sorted(q_set)}")
            for symbol in Sigma:
                new_set = set()
                for q in q_set:
                    if (q, symbol) in delta:
                        new_set |= delta[(q, symbol)]
                new_set = self.epsilon_closure_set(new_set, delta)
                if new_set:
                    new_set = frozenset(new_set)
                    if new_set not in dfa_Q:
                        dfa_Q.add(new_set)
                        unmarked_states.append(new_set)
                    if (q_set, symbol) not in dfa_delta:
                        dfa_delta[(q_set, symbol)] = new_set
                        print(f"  Transition on '{symbol}': {sorted(q_set)} -> {sorted(new_set)}")

        #compute the final states
        dfa_F = set()
        for q_set in dfa_Q:
            for q in q_set:
                if q in F:
                    dfa_F.add(q_set)
                    break

        #convert the sets to lists for readability
        dfa_Q = [sorted(q_set) for q_set in dfa_Q]
        dfa_F = [sorted(q_set) for q_set in dfa_F]
        dfa_delta = {tuple(sorted(q_set)): sorted(next_set) for (q_set, symbol), next_set in dfa_delta.items()}
        dfa_q0 = sorted(q0_closure)
        dfa = (dfa_Q, Sigma, dfa_delta, dfa_q0, dfa_F)

        print(f"\nConversion complete. DFA has {len(dfa_Q)} states:")
        for q_set in dfa_Q:
            if q_set in dfa_F:
                print(f"  *{q_set}")
            else:
                print(f"   {q_set}")

        return dfa

    #fonction to compute the epsilon closure
    def epsilon_closure(self, q, delta):
        closure = set()
        unprocessed = [q]
        while unprocessed:
            curr = unprocessed.pop()
            closure.add(curr)
            if (curr, '') in delta:
                for next_state in delta[(curr, '')]:
                    if next_state not in closure:
                        unprocessed.append(next_state)
        return closure

    def epsilon_closure_set(self, states, delta):
        closure = set(states)
        unprocessed = list(states)
        while unprocessed:
            curr = unprocessed.pop()
            if (curr, '') in delta:
                for next_state in delta[(curr, '')]:
                    if next_state not in closure:
                        closure.add(next_state)
                        unprocessed.append(next_state)
        return closure

    #function to draw the graph
    def graph_representation(self, Q, delta, q0, F):
        #create a new directed graph
        G = nx.DiGraph()

        # set node and edge attributes
        node_attrs = {'shape': 'circle'}
        final_node_attrs = {'shape': 'doublecircle'}
        edge_attrs = {'arrowstyle': '->'}

        #add nodes and edges to the graph
        for q in Q:
            if q in F:
                G.add_node(q, **final_node_attrs)
            else:
                G.add_node(q, **node_attrs)
        for t, q_next in delta.items():
            q, a = t
            for next_q in q_next:
                G.add_edge(q, next_q, label=a, **edge_attrs)

        #set initial state
        G.nodes[q0]['style'] = 'bold'

        #set node and edge labels
        node_labels = {q: q for q in Q}
        edge_labels = {(q, next_q): a for (q, a), next_q_set in delta.items() for next_q in next_q_set}

        pos = nx.spring_layout(G)

        #draw the graph
        nx.draw_networkx_nodes(G, pos, nodelist=Q, node_color='white', node_size=1000, linewidths=3, edgecolors='black')
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=15)
        nx.draw_networkx_edges(G, pos, width=2, arrowsize=20)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, label_pos=0.3)
        nx.draw_networkx_nodes(G, pos, nodelist=[q0], node_color='white', node_size=1000, linewidths=1,
                               edgecolors='black', node_shape='o')
        nx.draw_networkx_nodes(G, pos, nodelist=F, node_shape='o', node_size=1000, node_color='white', linewidths=5,
                               edgecolors='black')

        plt.axis('off')
        plt.title("NFA Graph representation")
        plt.show()
