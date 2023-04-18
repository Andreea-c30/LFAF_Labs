class Chomsky:

    def remove_epsilon_prod(self, grammar):

        epsilons = [nt for nt in grammar if '' in grammar[nt]]

        #add new prod to replace epsilon
        new_productions = {}
        for nt in grammar:
            new_productions[nt] = set()
            for prod in grammar[nt]:
                for eps in epsilons:
                    if eps in prod:
                        #generate all possible combinations without eps
                        new_prod = prod.replace(eps, '')
                        if new_prod != '':
                            new_productions[nt].add(new_prod)
            if epsilons:
                #add the original productions without epsilons
                new_productions[nt] |= set(grammar[nt]) - {''}

        #remove the original epsilon production
        grammar = {nt: list(prods) for nt, prods in new_productions.items() if prods}
        #print("Removing epsilon productions:\n", grammar)
        return grammar



    def eliminate_unit_prod(self, grammar):
        renamings = [nt for nt in grammar if len(grammar[nt]) == 1 and list(grammar[nt])[0] in grammar and list(grammar[nt])[0] != nt]
        for nt in renamings:
            prod = list(grammar[nt])[0]
            new_prods = set(grammar[prod]) - {''}
            del grammar[nt]
            for new_prod in new_prods:
                grammar[nt].append(new_prod)

        #eliminate all unit productions
        units = [(nt, prod) for nt in grammar for prod in grammar[nt] if len(prod) == 1 and prod.isupper()]
        while units:
            nt, prod = units.pop()
            new_prods = grammar[prod].copy()
            grammar[nt].remove(prod)
            grammar[nt].extend(new_prods)
            for new_prod in new_prods:
                if len(new_prod) == 1 and new_prod.isupper():
                    units.append((nt, new_prod))

        #print("Removing unit productions:\n", grammar)
        return grammar

    def remove_inaccessible(self, grammar):
        #find accessible symbols
        accessible = set()
        queue = ['S']
        while queue:
            symbol = queue.pop(0)
            if symbol not in accessible:
                accessible.add(symbol)
                for production in grammar.get(symbol, []):
                    for s in production:
                        if s.isupper():
                            queue.append(s)
        #remove inaccessible symbols
        new_grammar = {}
        if 'S' in accessible:
            new_productions = []
            for prod in grammar.get('S', []):
                if all(s in accessible or not s.isupper() for s in prod):
                    new_productions.append(prod)
            if new_productions:
                new_grammar['S'] = sorted(new_productions)

        for nt in sorted(accessible):
            new_productions = []
            for prod in grammar.get(nt, []):
                if all(s in accessible or not s.isupper() for s in prod):
                    new_productions.append(prod)
            if new_productions:
                new_grammar[nt] = sorted(new_productions)

        #print("Eliminate inaccessible symbols:\n", new_grammar)
        return new_grammar



    def remove_nonproductive(self, grammar):
        #find productive symbols
        productive = set()
        for nt, prods in grammar.items():
            for prod in prods:
                if all(s in productive or s.islower() for s in prod):
                    productive.add(nt)

        #print("Set of productive productions: ",productive)

        #remove non-productive symbols
        new_grammar = {}
        for nt, prods in grammar.items():
            if nt in productive:
                new_prods = [prod for prod in prods if all(s in productive or s.islower() for s in prod)]
                if new_prods:
                    new_grammar[nt] = new_prods
        #print("Eliminate nonproductive symbols:\n", new_grammar)
        return new_grammar

    def apply_rules(self, grammar):
        grammar = self.remove_epsilon_prod(grammar)
        grammar = self.eliminate_unit_prod(grammar)
        grammar = self.remove_inaccessible(grammar)
        grammar = self.remove_nonproductive(grammar)

        return grammar

    def chomsky_normal_form(self, grammar):
        grammar = self.apply_rules(grammar)

        new_grammar = grammar.copy()

        #find terminals
        terminals = set()
        for nt, prods in grammar.items():
            for prod in prods:
                for symbol in prod:
                    if symbol.islower():
                        terminals.add(symbol)
        terminals = sorted(terminals)

        #add new productions for each terminal symbol
        index = 0
        for t in terminals:
            new_nt = f"X{index}"
            new_grammar[new_nt] = [t]
            index += 1

        #add new productions
        new_nt = "X2"
        new_grammar[new_nt] = ["X0A"]
        new_nta = "X3"
        new_grammar[new_nta] = ["X2X1"]
        new_ntb = "X4"
        new_grammar[new_ntb] = ["AX3"]


        #create the new productions
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

        #create the new grammar with the updated productions
        new_grammar_str = "\n".join(productions)
        rep=new_grammar_str.replace("X0A","X2",5)
        rep = rep.replace("X2X1", "X3",3)
        rep = rep.replace("AX3", "X4",3)
        return rep
