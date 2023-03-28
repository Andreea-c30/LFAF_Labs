
class Lexer:

    #function that performs lexical analysis on a number
    def lex_num(self,line):
        num = ""
        for c in line:
            if not c.isdigit():
                break
            num += c
        return 'INT', int(num), len(num)

    #function that performs lexical analysis on a string
    def lex_str(self,line):
        delimiter = line[0]
        string = ""
        for c in line[1:]:
            if c == delimiter:
                break
            string += c
        return 'STRING', string, len(string) + 2  # + 2 to account for the quotes

    #function that performs lexical analysis on a keywords and user input definitions
    def lex_id(self,line):
        keys = ['main','cin','cout', 'while', 'if', 'else', 'elif','for','do', 'return', 'int','bool','float']
        id = ""
        for c in line:
            if not (c.isdigit() or c.isalpha() or c == "_"):
                break
            id += c
        if id in keys:
            return 'KEYWORD', id, len(id)
        else:
            return 'ID', id, len(id)

    #function that performs lexical analysis on a symbol
     def lex_symb(self, line):
        #dictionary that contains the symbols
        symbols = {"BRACES": ["{", "}"],
                   "PARENTHESES": ["(",")"],
                   "RBRACK": ["[", "]"],
                   "PLUS": "+", "MINUS": "-", "MULTIPLICATION": "*", "DIVISION": "/", "MODULUS": "%",
                   "SEMICOLON": ";","COMMA": ",","EQUAL": "=","AND": "&", "OR": "|",
                   "COMPARATOR": ["<",">"]
                   }
        for symbol_type, symbol_list in symbols.items():
            if line[0] in symbol_list:
                return symbol_type + ' ' , line[0]
        return None

    #function to tokenize a given input string
    def lex(self, line):
        tokens = []
        lexeme_count = 0
        while lexeme_count < len(line):
            lexeme = line[lexeme_count]
            if lexeme.isdigit():
                typ, tok, consumed = self.lex_num(line[lexeme_count:])
            elif lexeme in ('"', "'"):
                typ, tok, consumed = self.lex_str(line[lexeme_count:])
            elif lexeme.isalpha() or lexeme == "_":
                typ, tok, consumed = self.lex_id(line[lexeme_count:])
            elif lexeme in ('{', '}', '(', ')', '[', ']',
                            '+','-','*','/','%',',',';','=',
                            '&','|','<','>'):
                typ, tok = self.lex_symb(line[lexeme_count:])
                consumed = 1
            else:
                lexeme_count += 1
                continue
            tokens.append((typ, tok))
            lexeme_count += consumed
        for token in tokens:
            print(f"Token {token}")
        return tokens

if __name__ == '__main__':
        # defining the input of the lexer
        code = 'int main() { \
               double n1, n2, n3;\
               cout << "Enter three numbers: "; \
               cin >> n1 >> n2 >> n3; \
               if(n1 >= n2 && n1 >= n3) \
                    cout << "Largest number: " << n1; \
               else if(n2 >= n1 && n2 >= n3) \
                 cout << "Largest number: " << n2; \
               else \
                    cout << "Largest number: " << n3; \
               return 0;} '
        lexer=Lexer()
        lexer.lex(code)

