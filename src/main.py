from Grammar import Grammar

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

        print("\nConvert Grammar to Finite Automata")
        g=Grammar(P)
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