from tokens import TokenType
from ast_nodes import *
class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.get_token()

    def raise_error(self, message="Invalid syntax"):
        if self.current_token:
            token_type = self.current_token.type
            token_value = self.current_token.value
            raise Exception(f"{message} (Token: {token_type}, Value: {token_value})")
        else:
            raise Exception(message)

    def get_token(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None

        result = self.parse_expression()

        if self.current_token != None:
            self.raise_error()

        return result

    def parse_expression(self):
        result = self.parse_term()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.get_token()
                result = AddNode(result, self.parse_term())
            elif self.current_token.type == TokenType.MINUS:
                self.get_token()
                result = SubtractNode(result, self.parse_term())

        return result

    def parse_term(self):
        result = self.parse_factor()

        while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.get_token()
                result = MultiplyNode(result, self.parse_factor())
            elif self.current_token.type == TokenType.DIVIDE:
                self.get_token()
                result = DivideNode(result, self.parse_factor())

        return result

    def parse_factor(self):
        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.get_token()
            result = self.parse_expression()

            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()

            self.get_token()
            return result

        elif token.type == TokenType.NUMBER:
            self.get_token()
            return NumberNode(token.value)

        elif token.type == TokenType.PLUS:
            self.get_token()
            return PlusNode(self.parse_factor())

        elif token.type == TokenType.MINUS:
            self.get_token()
            return MinusNode(self.parse_factor())

        elif token.type == TokenType.STRING:
            self.get_token()
            return StringNode(token.value)

        elif token.type == TokenType.KEYWORD:
            self.get_token()
            return KeywordNode(token.value)

        elif token.type == TokenType.ID:
            self.get_token()
            return IdentifierNode(token.value)

        self.raise_error()
