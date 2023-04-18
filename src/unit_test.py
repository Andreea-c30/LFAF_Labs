import unittest
from Chomsky import Chomsky


class TestChomskyNormalForm(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
