# Topic: Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

### Course: Formal Languages & Finite Automata

### Author: Andreea Chiper, FAF-212, Variant 7

------------------------------------------------------------------------

## Theory

   A finite automata is a mechanism that is able to recognize patterns. Also known as finite state machine, consists of states, transition that go from one state to another based on the input symbol.
Finite automata can be classified in 2 types:
Deterministic(DFA) - for one input character, the transition goes to one state only. A transition function is defined on every state for every input symbol. Also in DFA null transition is not allowed, it cannot change state without any input character.
Nondeterministic(NFA) - similar to the DFA, it has some different rules, it is allowed to transmit to any number of states for a particular input. It is allowed to do a null move (empty string), which means it can go forward without reading symbols.


## Objectives:

1.  Understand what an automaton is and what it can be used for.

2.  Continuing the work in the same repository and the same project, the following need to be added: 

a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

a. Implement conversion of a finite automaton to a regular grammar.

b. Determine whether your FA is deterministic or non-deterministic.

c. Implement some functionality that would convert an NDFA to a DFA.

d. Represent the finite automaton graphically (Optional, and can be considered as a bonus point):

- You can use external libraries, tools or APIs to generate the figures/diagrams.

- Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.



## Implementation description
First of all, from the previous laboratory work grammar, it was implemented a function that classifies it based on Chomsky hierarchy. The "classify_chomsky" method determines the type of grammar represented as input by a set of production rules. It was determined which category enters using the rules for each type in particular. 
It determines whether the grammar is a regular grammar first, then whether it is a context-free grammar, and finally whether it is a context-sensitive grammar. The grammar is considered unrestricted if none of these conditions are met.

The function is invoked in the Main program through a grammar object.
```
print("Classification of grammar based on Chomsky hierarchy:")
chomsky_class = gr.classify_chomsky()
print(chomsky_class)
```
Concerning the finite automata tasks, sets have been utilized to represent the alphabet and states, while distionaries were used to represent the transitions defined as delta.

```
 #defining the finite automaton
Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b'}
F = {'q3'}
delta = {('q0', 'a'): {'q1'},
('q1', 'b'): {'q2'},
('q2', 'b'): {'q3', 'q2'},
('q3', 'a'): {'q1'},
('q1', 'a'): {'q1'}}
q0 = 'q0'
```
 Using the "fa_to_rg" function the finite automaton is converted into a grammar. This is done by creating production rules for each transition in the automaton, as well as a production rule for each accepted state that allows for the generation of the empty string. Lastly, it generates a production rule that defines the grammar's first symbol.
 The function converts a finite automata into a grammar. It performs the following:
 
-Defines the start symbol.

-Defines non-terminal values.

-Adds production rules for each transition.

-Adds production rules for each final state.

-Defines the initial production rule.

-Returns the production rules as a string.

Function "is_deterministic" determines if a finite automaton is deterministic (DFA) or nondeterministic (NFA). It accepts the transition function delta as input and looks for states with multiple transitions defined for the same input symbol. 
If such states exist, the automaton is declared an NFA, and the function prints the result and returns 0. If no such states exist, the automaton is called a DFA, and the function returns an output which specifies the type DFA.

```
for state in delta:
  inputs = set(symbol for symbol, _ in delta[state])
  if len(inputs) < len(delta[state]):
    print("NFA- nondeterministic")
    return 0
print("DFA- deterministic")
```

In order to convert the NFA to DFA it was implemented the method "nfa_to_dfa()", which takes in the parameters: Q, Sigma, delta, q0 and F to return the equivalent DFA. It uses the "epsilon_closure()" function to compute the epsilon closure of each state and then computes the transitions and final states of the DFA using these epsilon closures.

The function creates an empty dictionary and set for the new DFA transitions and states. 

Then it computes the epsilon closure of the initial state and adds it as the first state in the new DFA states set. It processes each unmarked state, computes the transitions for each symbol, and adds the resulting set of states to the new DFA states set and transition to the dictionary if they are not already present. 

It computes the final states of the new DFA by checking if any of the states contain at least one of the final states from the input NFA. In the end, it converts the sets of states to lists and returns a new DFA components.

Last but not least, in order to represent the automaton graphically it was used the NetworkX library.
The function adds the nodes to the graph, with final nodes having the doublecircle shape. Then, it adds the edges to the graph using the delta dictionary. The initial state is set to bold, and the node and edge labels are set. The function then calculates the layout of the graph using the spring layout algorithm in NetworkX, and uses the nx.draw_networkx_* functions to draw the graph. To display the graph it was used the plt.show() function from the matplotlib library.

## Conclusions / Screenshots / Results
Working on this laboratory work, I implemented the Chomsky classification functionality for my grammar. This functionality provides a useful tool for classifying grammars according to their complexity and structure. Additionally, I implemented the conversion of finite automata to grammar and the determination of automata types. 
Converting the NFA to DFA was harder then I expected, but I managed to finish it through a lot of research and analysis.  Overall, this laboratory was a great learning experience and has provided valuable skills that can be applied to future projects in pbl or in my personal development.

The results I have obtained during this lab can be observed in the figures below
<div align="center">
  
![classification](https://user-images.githubusercontent.com/84787381/223276285-fa793134-9d97-4058-a570-29d532309aed.png)

Figure 1. Classification of the grammar</div>

<div align="center">

![Fa_to_gr](https://user-images.githubusercontent.com/84787381/223276541-fe77d417-c1b7-4588-9dad-63543db4095c.png)

Figure 2. Conversion FA to Grammar</div>
  
<div align="center">
  
![DFAorNFA](https://user-images.githubusercontent.com/84787381/223276609-ea8328f0-602e-47c5-be2d-f4c516e8f668.png)

Figure 3. Type of Finite automata</div>

  <div align="center">
    
![nfa_To_dfa](https://user-images.githubusercontent.com/84787381/223276651-00b1197b-a9ac-4035-9a7b-b9cce8a958b0.png)

Figure 4. Conversion NFA to DFA</div>

 <div align="center">
  
![graph](https://user-images.githubusercontent.com/84787381/223277700-208757fd-2a3d-4055-9f2a-f3d0d0d2da59.png)

Figure 5. Graph of the finite automaton</div>


## References
-   Chomsky Hierarchy in Theory of Computation [online source]: https://www.geeksforgeeks.org/chomsky-hierarchy-in-theory-of-computation/
-   Formal language theory [online source]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3367686/
-   Conversion from NFA to DFA [online source]: [https://youtu.be/ZZi5DJINwJ0](https://www.javatpoint.com/automata-conversion-from-nfa-to-dfa)
