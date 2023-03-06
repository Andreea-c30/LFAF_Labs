import random
from FiniteAutomata import FiniteAutomata

# class to define grammar
class Grammar:
    def __init__(self, production):
        self.production = production

    # function to generate a word from the grammar
    def generate_word(self, symbol):
        rule = self.production.get(symbol)
        # case when is no rule for the symbol
        if rule is None:
            return symbol
        else:
            #choose a random rule and generate a word
            var = random.choice(rule)
            return "".join(self.generate_word(r) for r in var)

    #function to convert the grammar to a finite automata
    def grammar_to_fa(self,grammar):

        Q = set(grammar.production.keys())
        alphabet = set()
        #using for loop to iterate through the grammar rules
        for rule in grammar.production.values():
            for symbols in rule:
                for symbol in symbols:
                    if symbol not in Q:
                        #adding non-terminal symbols to the alphabet
                        alphabet.add(symbol)
        transition = {}
        #using for loops to add transitions
        for state, rule in grammar.production.items():
            for symbols in rule:
                for i, symbol in enumerate(symbols):
                    if symbol in Q:
                        transition[(state, symbols[i - 1])] = symbol
                    if symbol in alphabet:
                        transition[(state, symbol)] = "C"

        #initialize the initial and final states
        q0 = "S"
        F = {"C"}
        #creating the finite automaton
        fa = FiniteAutomata(Q=Q,
                            alphabet=alphabet,
                            transition=transition,
                            q0=q0,
                            F=F)
        return fa

    #determine the grammar type
    def classify_chomsky(self):
        #check if the grammar is type3
        if all(len(r) <= 2 and (len(r) == 1 or r[0].islower() or r[1].isupper()) for rhs in self.production.values() for r
               in rhs):
            return "Type-3: Regular grammar"

        #check if the grammar is type2
        if all(len(r) == 1 and r[0].islower() for rhs in self.production.values() for r in rhs):
            return "Type-2: Context-free grammar"

        #check if the grammar is type1
        if all(len(r) >= len(lhs) for lhs, rhs in self.production.items() for r in rhs):
            return "Type-1: Context-sensitive grammar"

        return "Type-0: Unrestricted grammar"




