from Grammar import Grammar
from FiniteAutomata import FiniteAutomata
class Main:

    if __name__ == '__main__':

        #defining grammar rules
        P = Grammar({
            "S": ["aD"],
            "D": ["bE"],
            "E": ["cF","dL"],
            "F": ["dD"],
            "L": ["aL", "bL", "c"],
        })

        #Calling function 5 times to generate strings
        print("Generated words: ")
        print(P.generate_word("S"))
        print(P.generate_word("S"))
        print(P.generate_word("S"))
        print(P.generate_word("S"))
        print(P.generate_word("S"))
        g = Grammar(P)

        print("\nConvert Grammar to Finite Automata")
        #calling function to convert from grammar object into fa
        fa = g.grammar_to_fa(P)

        print("States: ", fa.Q)
        print("Alphabet: ", fa.alphabet)
        print("Transitions: ", fa.transition)
        print("Start state: ",fa.q0)
        print("Final states: ", fa.F)
        print("\nValidation:")

        #input some strings
        input_string_1 = "abcdbdac"
        input_string_2 = "abcdbdacaaaaaaaaa"

        # should return True
        print(f"Word {input_string_1} is valid ->",fa.validation(input_string_1))
        # should return False
        print(f"Word {input_string_2} is valid ->",fa.validation(input_string_2))

        print(f"Word {input_string_1} is valid ->", fa.validation(input_string_1))
        print(f"Word {input_string_2} is valid ->", fa.validation(input_string_2))

        #task 2 from lab 2
        print("\nLaboratory 2 tasks: \n")
        gr = Grammar(P.production)
        print("Classification of grammar based on Chomsky hierarchy:")
        chomsky_class = gr.classify_chomsky()
        print(chomsky_class)

        #defining the finite automaton
        Q = {'q0', 'q1', 'q2', 'q3'}
        Sigma = {'a', 'b'}
        F = {'q3'}
        delta = {('q0', 'a'): {'q1'},
                 ('q1', 'b'): {'q2'},
                 ('q2', 'b'): {'q3', 'q2'},
                 ('q3', 'a'): {'q1'},
                 ('q1', 'a'): {'q1'}}
        q0 = 'q0'
        f=FiniteAutomata(Q,Sigma,delta,q0,F)
        print("Conversion from Finite automaton to grammar:")
        rg = f.fa_to_rg(Q, Sigma, delta, q0, F)
        print(rg)

        f.is_deterministic(delta)
        print(f.nfa_to_dfa(Q, Sigma, delta, q0, F))
         #graph representation
       # f.graph_representation(Q, delta, q0, F)

