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