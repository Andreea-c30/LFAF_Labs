from Lexer import Lexer
from Parser import Parser

if __name__ == '__main__':
    while True:
        text = input("input: ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        '''for i in tokens:
            print(i)'''
        parser = Parser(tokens)
        tree = parser.parse()
        print(tree)


