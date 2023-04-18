# Topic: Chomsky Normal Form

### Course: Formal Languages & Finite Automata

### Author: Andreea Chiper, FAF-212, Variant 7

------------------------------------------------------------------------

## Theory

&ensp;&ensp;&ensp;Chomsky normal form is a type of context-free grammar that is used in formal language. It is a method of converting a CFG into a more narrowed and canonical form that can then be analyzed and processed using algorithms.

&ensp;&ensp;&ensp;A context-free grammar is made up of a series of production rules that define how non-terminal symbols can be replaced by sequences of terminal and non-terminal symbols. 

&ensp;&ensp;&ensp;Chomsky Normal Form is a grammar where every production is either of the form A → BC or A → c, where A, B, C are arbitrary variables and c an arbitrary symbol [1].

&ensp;&ensp;&ensp;All production rules have a combination of exactly two non-terminal symbols or one non-terminal symbol followed by one terminal symbol on the right side; a terminal symbol isn't allowed on the left side of a production rule. Furthermore, CNF allows for the production of an empty string using simply the start symbol [2].

&ensp;&ensp;&ensp;Usually, converting a context-free grammar into Chomsky normal form takes the following steps:
1. Eliminate ε-productions by introducing new production rules.
2. Eliminate unit productions by replacing them with equivalent productions.
3. Eliminate inaccessible symbols, usually there are the non-terminal sybols that cannot be found in the right side of the productions, but exist in the left side.
4. Eliminate the non-productive symbols.
5. Obtain the Chomsky normal form.

&ensp;&ensp;&ensp;In combination, these steps convert the original context-free grammar into CNF, a more constrained and standardized version.
  
## Objectives:

1.  Learn about Chomsky Normal Form (CNF) [3].
2.  Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
    1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
    2. The implemented functionality needs executed and tested.
    3. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
    4. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.



## Implementation description

&ensp;&ensp;&ensp;The program for converting a grammar into Chomsky normal form was written in Python and includes a class called Chomsky, which was tested using unit tests.

&ensp;&ensp;&ensp;The steps for converting into CNF were defined as the following methods:

1. The method remove_epsilon_prod() - removing epsilon productions from the specified grammar. 

&ensp;&ensp;&ensp;It finds non-terminal symbols (nt) in the grammar that have epsilon, represented by ('') as one of its productions and generates new ones to take their place. 

```
epsilons = [nt for nt in grammar if '' in grammar[nt]]
```

&ensp;&ensp;&ensp;It is generated every possible combination of productions without epsilon for each non-terminal with epsilon and added to the new productions for each non-terminal with epsilon.

```
new_prod = prod.replace(eps, '')
                        if new_prod != '':
                            new_productions[nt].add(new_prod)
            if epsilons:
                new_productions[nt] |= set(grammar[nt]) - {''}
```

&ensp;&ensp;&ensp;Finally, it is removed the grammar's original epsilon production and returned the updated grammar.

```
 grammar = {nt: list(prods) for nt, prods in new_productions.items() if prods}
 
```
2. The method eliminate_unit_prod()- eliminating unit productions from the given grammar. 

&ensp;&ensp;&ensp;Are identified non-terminal symbols that have exactly one production, which is also a non-terminal symbol, and replaced the unit production with the productions of the non-terminal symbol it produced. This process is repeated until there are no more unit productions in the grammar. The method returns the updated grammar.

```
units = [(nt, prod) for nt in grammar for prod in grammar[nt] if len(prod) == 1 and prod.isupper()]
        while units:
            nt, prod = units.pop()
            new_prods = grammar[prod].copy()
            grammar[nt].remove(prod)
            grammar[nt].extend(new_prods)
            for new_prod in new_prods:
                if len(new_prod) == 1 and new_prod.isupper():
                    units.append((nt, new_prod))
```
3. The method remove_inaccessible() - removing inaccessible symbols from the given grammar. 

&ensp;&ensp;&ensp;Identifies non-terminal symbols that are not reachable from the start symbol 'S' and removes them from the grammar. It also removes productions that contain non-terminal symbols that are not reachable from 'S'. 

&ensp;&ensp;&ensp;Starting from the start symbol 'S', adding reachable symbols to the accessible set. 

```
        while queue:
            symbol = queue.pop(0)
            if symbol not in accessible:
                accessible.add(symbol)
                for production in grammar.get(symbol, []):
                    for s in production:
                        if s.isupper():
                            queue.append(s)
```

&ensp;&ensp;&ensp;Updating the grammar by removing inaccessible productions for each non-terminal symbol in the grammar. Iterating through the accessible symbols and for each non-terminal symbol, it is created a list of updated productions by filtering inaccessible symbols. If there are any updated productions, they are added to the new grammar with the non-terminal symbol as the key. 

```
        for nt in sorted(accessible):
            new_productions = []
            for prod in grammar.get(nt, []):
                if all(s in accessible or not s.isupper() for s in prod):
                    new_productions.append(prod)
            if new_productions:
                new_grammar[nt] = sorted(new_productions)
```

&ensp;&ensp;&ensp;Finally, it is returned the updated grammar as the new_grammar dictionary

4. The method remove_nonproductive() - removes non-productive symbols from the grammar. 

&ensp;&ensp;&ensp;It is indentified the productive symbols and is added it to a set in order to eliminate further the nonproductive symbols

```
productive = set()
        for nt, prods in grammar.items():
            for prod in prods:
                if all(s in productive or s.islower() for s in prod):
                    productive.add(nt)
```
&ensp;&ensp;&ensp;Are found non-terminal symbols that do not generate any terminal symbol and are removed from the grammar. 

```
new_grammar = {}
        for nt, prods in grammar.items():
            if nt in productive:
                new_prods = [prod for prod in prods if all(s in productive or s.islower() for s in prod)]
                if new_prods:
                    new_grammar[nt] = new_prods
```
5. The method apply_rules() - are applied all the above rules to the given grammar in the following order: remove_epsilon_prod, eliminate_unit_prod, remove_inaccessible, and remove_nonproductive. Returning the updated grammar.
```
    def apply_rules(self, grammar):
        grammar = self.remove_epsilon_prod(grammar)
        grammar = self.eliminate_unit_prod(grammar)
        grammar = self.remove_inaccessible(grammar)
        grammar = self.remove_nonproductive(grammar)

        return grammar
```

6. The method chomsky_normal_form() - converting the grammar into Chomsky Normal Form by applying the rules in the apply_rules method. 

&ensp;&ensp;&ensp;Then, creating new non-terminal symbols for each terminal symbol in the grammar and adds new productions for them, as well as some additional productions required for CNF.

&ensp;&ensp;&ensp;Selecting the terminal symbols by iterating over the grammar's productions and adding new productions for each terminal symbol in the format Xn -> t, where n is an incrementing index and t is a terminal symbol.

```
index = 0
        for t in terminals:
            new_nt = f"X{index}"
            new_grammar[new_nt] = [t]
            index += 1
```
&ensp;&ensp;&ensp;Iterating through new_grammar and its productions, are generated new productions for each non-terminal symbol in the grammar. If there is only one lowercase symbol in the production, it is substituted it with the matching non-terminal symbol from new_grammar. Then adding the corresponding new productions to match the rules of the CNF.

```
 productions = []
        for nt, prods in new_grammar.items():
            for prod in prods:
                if len(prod) == 1 and prod.islower():
                   productions.append(f"{nt} -> {prod}")
                elif len(prod) > 1:
                    new_prod = ""
                    for symbol in prod:
                        if symbol.islower():
                            new_prod += next(nt for nt, t in new_grammar.items() if t == [symbol])
                        else:
                            new_prod += symbol
                    productions.append(f"{nt} -> {new_prod}")
```

&ensp;&ensp;&ensp;Last but not least, unit tests were built in order to execute and test the program. The test cases verify the accuracy of the Chomsky class's apply_rules() and chomsky_normal_form() methods.

&ensp;&ensp;&ensp;The first two test cases, test_rules_nr1() and test_rules_nr2(), determine whether the apply_rules() method applies the grammatical transformation rules successfully. 

```
    def test_rules_nr1(self):
        grammar = {'S': ['bA', 'B'],
                   'A': ['a', 'aS', 'bAaAb'],
                   'B': ['AC', 'bS', 'aAa'],
                   'C': ['', 'AB'],
                   'E': ['BA']
                   }
        result =  {'S': ['AC', 'a', 'aAa', 'aS', 'bA', 'bAaAb', 'bS'],
                   'A': ['a', 'aS', 'bAaAb'],
                   'B': ['AC', 'a', 'aAa', 'aS', 'bAaAb', 'bS'],
                   'C': ['AB']
                   }
        ch = Chomsky()
        self.assertEqual(ch.apply_rules(grammar), result)

    def test_rules_nr2(self):
        grammar = {'S': ['aB', 'AC'],
                  'A': ['a', 'ASC', 'BC', 'aD'],
                  'B': ['b', 'bS'],
                  'C': ['', 'BA'],
                  'E': ['aB'],
                  'D': ['abC']
                  }
        result =  {'S': ['AC', 'AS', 'ASC', 'BC', 'a', 'aB', 'aD', 'b', 'bS'],
                   'A': ['AS', 'ASC', 'BC', 'a', 'aD', 'b', 'bS'],
                   'B': ['b', 'bS'],
                   'C': ['BA'],
                   'D': ['ab', 'abC']
                   }
        ch = Chomsky()
        self.assertEqual(ch.apply_rules(grammar), result)
```

&ensp;&ensp;&ensp;The third test case, test_conversion(), determines whether the chomsky_normal_form() method converts the grammar appropriately to Chomsky normal form.

```
    def test_conversion(self):

        grammar = {'S': ['bA', 'B'],
                'A': ['a', 'aS', 'bAaAb'],
                'B': ['AC', 'bS', 'aAa'],
                'C': ['', 'AB'],
                'E': ['BA']
                }
        result = "S -> AC\nS -> a\nS -> X2X0\nS -> X0S\nS -> X1A\nS -> X1X4\nS -> X1S\n" \
              "A -> a\nA -> X0S\nA -> X1X4\n" \
              "B -> AC\nB -> a\nB -> X2X0\nB -> X0S\nB -> X1X4\nB -> X1S\n" \
              "C -> AB\n" \
              "X0 -> a\n" \
              "X1 -> b\n" \
              "X2 -> X0A\n" \
              "X3 -> X2X1\n" \
              "X4 -> AX3"
        ch = Chomsky()
        self.assertEqual(ch.chomsky_normal_form(grammar), result)
```

&ensp;&ensp;&ensp;To run the test cases, it is called the unittest.main() function, which has detected and run all of the TestChomskyNormalForm class's test cases. If all of the assertions in the test cases pass without exceptions, it is shown that the Chomsky class implementation is correct. Otherwise, it is indicated that there may be implementation problems that need to be solved.

## Conclusions / Screenshots / Results

&ensp;&ensp;&ensp;In conclusion, the laboratory work required developing and implementing a program that can convert context-free grammars into Chomsky normal form. Unit tests were used to confirm the program's accuracy and functionality. The implemented program converts the grammar into Chomsky normal form using grammar transformation rules and provides a way to obtain the converted grammar as a string representation.

&ensp;&ensp;&ensp;The initial grammar was represented as a dictionary
```
 {'S': ['bA', 'B'], 
 'A': ['a', 'aS', 'bAaAb'], 
 'B': ['AC', 'bS', 'aAa'], 
 'C': ['', 'AB'], 
 'E': ['BA']}
```
&ensp;&ensp;&ensp;After performing multiple grammar operations, such as removing epsilon productions, unit productions, inaccessible symbols, and nonproductive symbols, the resulting grammar at each step is represented below:

&ensp;&ensp;&ensp;Removing epsilon productions:
```
 {'S': ['bA', 'B'], 
 'A': ['a', 'bAaAb', 'aS'], 
 'B': ['A', 'aAa', 'AC', 'bS'], 
 'C': ['AB'], 
 'E': ['BA']}
```
&ensp;&ensp;&ensp;Removing unit productions:
 ```
 {'S': ['bA', 'aAa', 'AC', 'bS', 'a', 'bAaAb', 'aS'], 
 'A': ['a', 'bAaAb', 'aS'], 
 'B': ['aAa', 'AC', 'bS', 'a', 'bAaAb', 'aS'], 
 'C': ['AB'], 
 'E': ['BA']}
```
&ensp;&ensp;&ensp;Eliminate inaccessible symbols:
 ```
 {'S': ['AC', 'a', 'aAa', 'aS', 'bA', 'bAaAb', 'bS'], 
 'A': ['a', 'aS', 'bAaAb'], 
 'B': ['AC', 'a', 'aAa', 'aS', 'bAaAb', 'bS'], 
 'C': ['AB']}
```
&ensp;&ensp;&ensp;Eliminate nonproductive symbols:
```
 {'S': ['AC', 'a', 'aAa', 'aS', 'bA', 'bAaAb', 'bS'], 
 'A': ['a', 'aS', 'bAaAb'], 
 'B': ['AC', 'a', 'aAa', 'aS', 'bAaAb', 'bS'], 
 'C': ['AB']}
```

&ensp;&ensp;&ensp;Lastly in the end it would be obtained the CNF as follows:

```
S -> AC
S -> a
S -> X2X0
S -> X0S
S -> X1A
S -> X1X4
S -> X1S
A -> a
A -> X0S
A -> X1X4
B -> AC
B -> a
B -> X2X0
B -> X0S
B -> X1X4
B -> X1S
C -> AB
X0 -> a
X1 -> b
X2 -> X0A
X3 -> X2X1
X4 -> AX3
```

&ensp;&ensp;&ensp;Unit testing is an important phase in software development since it aids in the identification and correction of bugs in the code. The unit tests given, test_rules_nr1(), test_rules_nr2(), and test_conversion(), cover several scenarios and validate the implemented functions. If all of the test cases pass without issues, it means that the program achieves the expected results. As shown in figure 1, 3 out of 3 tests were passed, therefore the program works without any problems.
 <div align="center">
    
![unit_test_result](https://user-images.githubusercontent.com/84787381/232864451-7c6f5321-ac74-4f32-a963-932d34fd577b.png)

Figure. 1. Test output </div>

&ensp;&ensp;&ensp;Overall, working on this laboratory allowed me to create a program for converting context-free grammars into Chomsky normal form and execute unit testing to check its accuracy. It was a valuable experience in terms of comprehending grammar transformation and unit testing principles in the context of programming and software development.

## References
[1] [Chomsky's Normal Form (CNF)](https://www.javatpoint.com/automata-chomskys-normal-form)

[2] [Chomsky Normal Form](https://www.tutorialspoint.com/automata_theory/chomsky_normal_form.html)

[3] [Chomsky Normal Form Wiki](https://en.wikipedia.org/wiki/Chomsky_normal_form)

