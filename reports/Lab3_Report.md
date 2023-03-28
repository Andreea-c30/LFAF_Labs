# Topic: Lexer & Scanner

### Course: Formal Languages & Finite Automata

### Author: Andreea Chiper, FAF-212

------------------------------------------------------------------------

## Theory

  &ensp;&ensp;&ensp; A lexer, also known as a scanner converts each syntactical element in the input into a token using regular expressions. Tokens are the smallest pieces of a programming language that can be processed further by the compiler or interpreter.
  
  &ensp;&ensp;&ensp; A lexer receives an input character and separates it into tokens according to rules given , providing a token display as output, it can be used by a parser to understand the structure of the program.
  
  &ensp;&ensp;&ensp; This process of processing the input stream character by character and organizing them into meaningful chunks or lexemes such as identifiers, keywords, operators, literals, and punctuation. Each lexeme is given a token type and a value that can be used to build a parse tree.
  
  &ensp;&ensp;&ensp; Overall, a lexer is a critical component of a compiler or interpreter that performs lexical analysis on source code and outputs a sequence of tokens. This procedure is required for parsing and interpreting a programming language and is an essential step in the compilation process.


  
## Objectives:

1.  Understand what lexical analysis [1] is.
2.  Get familiar with the inner workings of a lexer/scanner/tokenizer.
3.  Implement a sample lexer and show how it works.


## Implementation description

&ensp;&ensp;&ensp; The lexer was implemented in python language, it can tokenize a given input code into a sequence of tokens. The lexer is defined as a class called Lexer, which contains several methods for tokenizing different types of lexemes.

&ensp;&ensp;&ensp; The "lex_num" method is used to tokenize integer literals. It loops through the input characters until it finds a non-digit character, at which point it produces a tuple containing the token type 'INT' the integer value and the length of the lexeme which is used further.

```
    def lex_num(self,line):
        num = ""
        for c in line:
            if not c.isdigit():
                break
            num += c
        return 'INT', int(num), len(num)
```
&ensp;&ensp;&ensp; In order to tokenize string literals enclosed in quotes the method "lex_str" was implemented. It finds the delimiter character and then loops through the input characters until it finds the closing delimiter. It returns a tuple containing the token type 'STRING' the string value and the length of the lexeme plus two for the quotes.

```
 def lex_str(self,line):
        delimiter = line[0]
        string = ""
        for c in line[1:]:
            if c == delimiter:
                break
            string += c
        return 'STRING', string, len(string) + 2
```

&ensp;&ensp;&ensp; Tokenize identifiers using the "lex_id" method, which can be keywords or user defined names. It loops through the input characters until it hits a nonalphanumeric or underscore character, at which point it determines if the lexeme is a keyword or an identifier. 

&ensp;&ensp;&ensp; It returns a tuple with the token type 'KEYWORD' or 'ID,' the identifier name and length.

```
def lex_id(self,line):
        keys = ['main','cin','cout', 'while', 'if', 'else', 
        'elif','for','do', 'return', 'int','bool','float']
        id = ""
        for c in line:
            if not (c.isdigit() or c.isalpha() or c == "_"):
                break
            id += c
        if id in keys:
            return 'KEYWORD', id, len(id)
        else:
            return 'ID', id, len(id)
```
&ensp;&ensp;&ensp; The lex_symb method is used to tokenize symbols such as: parentheses, braces, operators, and punctuation marks. 

&ensp;&ensp;&ensp; It uses a dictionary to map each symbol type to a list of symbols and then checks whether the input character matches any of the symbols. It returns a tuple containing the symbol type and the symbol itself.

```
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
```    

&ensp;&ensp;&ensp; The main entry point for the lexer is the "lex()" method, which takes an input string and tokenizes it into a sequence of tokens. It iterates through the input characters using a loop, calling the proper method for each lexeme. 

&ensp;&ensp;&ensp; The resulting token is then appended to a list of tokens, and the index is updated to skip the consumed characters.

&ensp;&ensp;&ensp; If it's a digit, it calls the lex_num method which returns a token of type INT.

```
if lexeme.isdigit():
    typ, tok, consumed = self.lex_num(line[lexeme_count:])
```

&ensp;&ensp;&ensp; If it's a quotation mark, it calls the lex_str method which returns a token of type STRING. 
```
 elif lexeme in ('"', "'"):
    typ, tok, consumed = self.lex_str(line[lexeme_count:])
```
 &ensp;&ensp;&ensp; If it's an alphabetic character or underscore, it calls the lex_id method which returns either a token of type KEYWORD or ID.
 ```
elif lexeme.isalpha() or lexeme == "_":
    typ, tok, consumed = self.lex_id(line[lexeme_count:])
 ```

&ensp;&ensp;&ensp;  If it's a symbol, it calls the lex_symb method which returns a token of type: {},(),[],+,-,*,/%,',',;,=,&,|,<>.

 ```
elif lexeme in ('{', '}', '(', ')', '[', ']',
    '+','-','*','/','%',',',';','=','&','|','<','>'):
    typ, tok = self.lex_symb(line[lexeme_count:])
 ```

&ensp;&ensp;&ensp; If the character is none of the above, it skips through to the next one. The consumed variable records how many characters were used to generate the current token and this value is used to improve the lexeme_count variable to the next character in the input string.

&ensp;&ensp;&ensp; The if ```__name__ == '__main__'```: block defines a simple input code, which consists of a function that finds the largest of three numbers, and calls the lex method of the Lexer class to tokenize the code into a sequence of tokens.

 ```
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
 ```

## Conclusions / Screenshots / Results
&ensp;&ensp;&ensp; In conclusion, the lexer implementation in Python, takes a source code as input and breaks it down into a sequence of tokens. The program implements a class called Lexer, which contains several methods for tokenizing different types of lexemes such as integers, strings, identifiers and symbols.

&ensp;&ensp;&ensp; The Lexer class uses a loop to iterate through each character in the input code and calls the appropriate tokenization method for each lexeme. The resulting token is then appended to a list of tokens, and the index is updated to skip the consumed characters.

&ensp;&ensp;&ensp; The output is a sequence of tokens generated by the lexical for the given C++ code. Each token is a pair of a token type and a token value.

&ensp;&ensp;&ensp; In this case, the input code defines a program that reads three numbers from the user and prints the largest one. The output shows that the lexical analyzer has correctly identified the keywords ('int', 'main', 'cout', 'cin', 'if', 'else', 'return'), identifiers ('n1', 'n2', 'n3'), symbols ('{', '}', '(', ')', '[',']', '+', '-', '*', '/', '%', ',', ';', '=', '&', '|', '<', '>'), and string literals ('Enter three numbers:', 'Largest number:'), and has correctly classified them into their respective token types.

```
Token ('KEYWORD', 'int')
Token ('KEYWORD', 'main')
Token ('PARENTHESES ', '(')
Token ('PARENTHESES ', ')')
Token ('BRACES ', '{')
Token ('ID', 'double')
Token ('ID', 'n1')
Token ('COMMA ', ',')
Token ('ID', 'n2')
Token ('COMMA ', ',')
Token ('ID', 'n3')
Token ('SEMICOLON ', ';')
Token ('KEYWORD', 'cout')
Token ('COMPARATOR ', '<')
Token ('COMPARATOR ', '<')
Token ('STRING', 'Enter three numbers: ')
Token ('SEMICOLON ', ';')
Token ('KEYWORD', 'cin')
Token ('COMPARATOR ', '>')
Token ('COMPARATOR ', '>')
Token ('ID', 'n1')
Token ('COMPARATOR ', '>')
Token ('COMPARATOR ', '>')
Token ('ID', 'n2')
Token ('COMPARATOR ', '>')
Token ('COMPARATOR ', '>')
Token ('ID', 'n3')
Token ('SEMICOLON ', ';')
Token ('KEYWORD', 'if')
Token ('PARENTHESES ', '(')
Token ('ID', 'n1')
Token ('COMPARATOR ', '>')
Token ('EQUAL ', '=')
Token ('ID', 'n2')
Token ('AND ', '&')
Token ('AND ', '&')
Token ('ID', 'n1')
Token ('COMPARATOR ', '>')
Token ('EQUAL ', '=')
Token ('ID', 'n3')
Token ('PARENTHESES ', ')')
Token ('KEYWORD', 'cout')
Token ('COMPARATOR ', '<')
Token ('COMPARATOR ', '<')
Token ('STRING', 'Largest number: ')
Token ('COMPARATOR ', '<')
Token ('COMPARATOR ', '<')
Token ('ID', 'n1')
Token ('SEMICOLON ', ';')
Token ('KEYWORD', 'else')
Token ('KEYWORD', 'if')
Token ('PARENTHESES ', '(')
Token ('ID', 'n2')
Token ('COMPARATOR ', '>')
Token ('EQUAL ', '=')
Token ('ID', 'n1')
Token ('AND ', '&')
Token ('AND ', '&')
Token ('ID', 'n2')
Token ('COMPARATOR ', '>')
Token ('EQUAL ', '=')
Token ('ID', 'n3')
Token ('PARENTHESES ', ')')
Token ('KEYWORD', 'cout')
Token ('COMPARATOR ', '<')
Token ('COMPARATOR ', '<')
Token ('STRING', 'Largest number: ')
Token ('COMPARATOR ', '<')
Token ('COMPARATOR ', '<')
Token ('ID', 'n2')
Token ('SEMICOLON ', ';')
Token ('KEYWORD', 'else')
Token ('KEYWORD', 'cout')
Token ('COMPARATOR ', '<')
Token ('COMPARATOR ', '<')
Token ('STRING', 'Largest number: ')
Token ('COMPARATOR ', '<')
Token ('COMPARATOR ', '<')
Token ('ID', 'n3')
Token ('SEMICOLON ', ';')
Token ('KEYWORD', 'return')
Token ('INT', 0)
Token ('SEMICOLON ', ';')
Token ('BRACES ', '}')
```
&ensp;&ensp;&ensp; The generated sequence of tokens can be used by the next step of the compiler, which is the parser, to construct an abstract syntax tree that represents the structure of the program.

## References
[1] [A sample of a lexer implementation](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/LangImpl01.html)

[2] [An Overview of Lexing and Parsing](http://savage.net.au/Ron/html/graphviz2.marpa/Lexing.and.Parsing.Overview.html)

[3] [Building a lexer in python](https://medium.com/@pythonmembers.club/building-a-lexer-in-python-a-tutorial-3b6de161fe84)

[4] [Taming The Lexer](https://www.typefox.io/blog/taming-the-lexer)


