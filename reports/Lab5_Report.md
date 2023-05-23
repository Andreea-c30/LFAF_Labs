# Topic: Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata

### Author: Andreea Chiper, FAF-212, Variant 7

------------------------------------------------------------------------

## Theory

&ensp;&ensp;&ensp;In computer science, a parser is a program that is often part of a compiler. It takes in sequential source program instructions as input. It examines the structure of a text or input data in accordance with grammar or syntax norms. It's popular in the fields of technology, programming languages, and natural language analysis.
The resulting data structure, known as an abstract syntax tree (AST), allows the program to be analyzed and processed in later phases of compilation or interpretation.


&ensp;&ensp;&ensp;Parsing occurs during the compilation's analysis stage.
Parsing is the process of taking code from the preprocessor, breaking it down into smaller pieces, and analyzing it so that other software can understand it. The parser performs this by constructing a data structure from the pieces of input [1].

&ensp;&ensp;&ensp;The parser is made up of three parts, each of which deals with a distinct stage of the parsing process. The three stages are as follows:

- The first stage is a lexical analysis, also known as a scanner, takes code from the preprocessor and breaks it down into smaller chunks. It organizes the input code into lexeme sequences, each of which corresponds to a token.

- Syntactic analysis - this stage of parsing examines the input's syntactical structure using a data structure known as a parse tree or derivation tree.

- Semantic analysis is the third stage,it checks the parse tree against a symbol table to see if it is semantically consistent. 

&ensp;&ensp;&ensp;Overall, parsers are not only restricted to programming languages. They're used as well in natural language processing activities to evaluate and learn the grammatical structure of human languages, allowing chatbots, voice assistants, and machine translation tools to understand and react to user input.

  
## Objectives:

1. Get familiar with parsing, what it is and how it can be programmed [2].
2. Get familiar with the concept of AST [3].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.



## Implementation description

&ensp;&ensp;&ensp;In this laboratory work, it was implemented a parser in python language which uses the lexer in order to recieve the tokens that were be analysed. 

&ensp;&ensp;&ensp;Different data classes for the nodes were established in order to define a structure that would represent the nodes for AST. Each data class in the AST represents a certain type of node and provides a string representation of that node.

&ensp;&ensp;&ensp;The classes which were implemented in order to represent the nodes of the AST are: 

- NumberNode - represents a number in the AST.
- SubtractNode - represents a subtraction operation in the AST. 
- MultiplyNode - represents a multiplication operation in the AST. 
- DivideNode - represents a division operation in the AST. 
- PlusNode - represents a unary plus operation in the AST. 
- MinusNode - represents a unary minus operation in the AST. 
- EqualNode - represents an assignment operation in the AST.
- StringNode - represents a string literal in the AST. 
- KeywordNode - represents a keyword in the AST. 
- IdentifierNode - represents an identifier, variable or function name in the AST. 

&ensp;&ensp;&ensp;As can be seen, it is provided an example of implementation of the class that represents the node:

```
class NumberNode:
    value: any

    def __repr__(self):
        return f"Number: {self.value}"
```
&ensp;&ensp;&ensp;Each data class has an overridden __repr__ function that returns the node's string representation. The string representation provides the node type and its characteristics in a structured manner, making the AST structure easier to understand.

&ensp;&ensp;&ensp;During the parsing process, these data classes are used to generate the AST, where each token is mapped to the associated node type in the AST.

 &ensp;&ensp;&ensp;The parser includes methods to handle different grammar rules and construct an abstract syntax tree based on the input tokens.

&ensp;&ensp;&ensp;The initializer of the Parser class takes a list of tokens and creates an iterator to loop through them. To raise exceptions with relevant error messages and token details, use the raise_error function.

```
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.get_token()
```
&ensp;&ensp;&ensp;The "get_token" method tries to get the next token from the token iterator and sets it to the parser instance's current_token variable. If no more tokens are available, the current_token attribute is set to None.

```
    def get_token(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
```

&ensp;&ensp;&ensp;The "parse" method is responsible for beginning the parsing process and returning the outcome.It begins by determining whether the current_token is none. If no additional tokens are available, it instantly returns none. Then the parse_expression method is called to parse the input string and return the result.

&ensp;&ensp;&ensp;The method verifies for any remaining tokens after parsing the expression. If there are any remaining tokens, indicating an incomplete or unexpected input, the raise_error method is used to throw an exception.
```
 def parse(self):
        if self.current_token == None:
            return None

        result = self.parse_expression()

        if self.current_token != None:
            self.raise_error()

        return result
```

&ensp;&ensp;&ensp;Method "parse_expression" is in charge of parsing an expression and providing the result.
It performs addition and subtraction operations by calling the "parse_term" method, which also performs multiplication and division. 

```
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
```

&ensp;&ensp;&ensp;The "parse_term" method then calls the "parse_factor" method, which handles factors such as parentheses, numbers, unary operators, strings, keywords, and identifiers.

&ensp;&ensp;&ensp;The factor method checks the current token and handles various scenarios appropriately, moving to the next token as needed. If the token does not match any of the expected kinds, the raise_error method is invoked to report incorrect syntax.

&ensp;&ensp;&ensp;The raise_error method handles exceptions when error occurs during parsing, with an optional error message.
```
    def raise_error(self, message="Invalid syntax"):
        if self.current_token:
            token_type = self.current_token.type
            token_value = self.current_token.value
            raise Exception(f"{message} (Token: {token_type}, Value: {token_value})")
        else:
            raise Exception(message)
```

## Conclusions / Screenshots / Results

&ensp;&ensp;&ensp;Considering the expression as the input for the parser:

```
input: (5 + 3) * 2 - 7 / 4
```
&ensp;&ensp;&ensp;The lexer identified and generated tokens for each component of the expression.
The generated tokens are as follows:
```
LPAREN
NUMBER:5.0
PLUS
NUMBER:3.0
RPAREN
MULTIPLY
NUMBER:2.0
MINUS
NUMBER:7.0
DIVIDE
NUMBER:4.0
```
&ensp;&ensp;&ensp;It has been successfully processed by the parser. The AST generated by the parser reflects the structure of the expression. It consists of various nodes representing different operations and operands. The structure of the AST is as follows:
```
Subtraction: (
    Multiplycation: (
    Addition: (
    Number: 5.0,
    Number: 3.0
),
    Number: 2.0
),
    Dividsion: (
    Number: 7.0,
    Number: 4.0
)
)
```
&ensp;&ensp;&ensp;Another example that has been processed by the lexer and parser:
```
input: a+b/(d*c)
```
&ensp;&ensp;&ensp;The generated tokens by the lexer for this expression:
```
ID:a
PLUS
ID:b
DIVIDE
LPAREN
ID:d
MULTIPLY
ID:c
RPAREN
```
&ensp;&ensp;&ensp;As as result it was generated the AST of the expresion based on the previous output. The structure of the AST for the second expresion:
```
Addition: (
    Identifier: (
    a
),
    Dividsion: (
    Identifier: (
    b
),
    Multiplycation: (
    Identifier: (
    d
),
    Identifier: (
    c
)
)
)
)
```

&ensp;&ensp;&ensp;This AST provides a structured representation of the input expression, preserving the order of operations and grouping of operands. It can be further processed and interpreted to evaluate the expression and obtain the desired result.
 
&ensp;&ensp;&ensp;Finally, the successful conclusion of this laboratory work has given me the opportunity to create a parser that makes appropriate use of the tokens generated by the lexer. The parser creates an AST that describes the syntactic structure of the input text by processing the tokens. This AST is an intermediate representation that can be used to interpret and execute syntax in a functional programming language.

&ensp;&ensp;&ensp;I gained grat experience in building the necessary data structures for an AST and designing a small parser program as a result of my laboratory work. I learnt how to create and use multiple classes to represent different nodes in the AST, such as numbers, operators, strings, keywords, and identifiers. 


## References
[1] [Parser](https://www.javatpoint.com/parser)

[2] [Parsing Wiki](https://en.wikipedia.org/wiki/Parsing)

[3] [Abstract Syntax Tree Wiki](https://en.wikipedia.org/wiki/Abstract_syntax_tree)

