from enum import Enum
from dataclasses import dataclass



class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    BRACES = 7
    EQUAL = 8
    SEMICOLON = 9
    STRING = 10
    KEYWORD = 11
    ID = 12


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        if self.value is not None:
            return f"{self.type.name}:{self.value}"
        else:
            return self.type.name
