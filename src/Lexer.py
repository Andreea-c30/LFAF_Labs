from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '"' or self.current_char == "'":
                yield self.generate_string()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char.isalpha() or self.current_char == "_":
                yield self.generate_identifier_or_keyword()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.current_char == '{' or self.current_char == '}':
                self.advance()
                yield Token(TokenType.BRACES)
            elif self.current_char == '=':
                self.advance()
                yield Token(TokenType.EQUAL)
            elif self.current_char == ';':
                self.advance()
                yield Token(TokenType.SEMICOLON)
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_string(self):
        delimiter = self.current_char
        self.advance()
        string = ""
        while self.current_char != None and self.current_char != delimiter:
            string += self.current_char
            self.advance()
        if self.current_char == delimiter:
            self.advance()
            return Token(TokenType.STRING, string)
        else:
            raise Exception("Unterminated string")

    def generate_identifier_or_keyword(self):
        id = ""
        while self.current_char != None and (self.current_char.isalnum() or self.current_char == "_"):
            id += self.current_char
            self.advance()

        if id in ['main', 'cin', 'cout', 'while', 'if', 'else', 'elif', 'for', 'do', 'return', 'int', 'bool', 'float']:
            return Token(TokenType.KEYWORD, id)
        else:
            return Token(TokenType.ID, id)

    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))
