from dataclasses import dataclass


@dataclass
class NumberNode:
    value: any

    def __repr__(self):
        return f"Number: {self.value}"


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"Addition: (\n    {self.node_a},\n    {self.node_b}\n)"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"Subtraction: (\n    {self.node_a},\n    {self.node_b}\n)"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"Multiplycation: (\n    {self.node_a},\n    {self.node_b}\n)"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"Dividsion: (\n    {self.node_a},\n    {self.node_b}\n)"


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"Plus: (\n    {self.node}\n)"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"Minus: (\n    {self.node}\n)"


@dataclass
class EqualNode:
    node: any

    def __repr__(self):
        return f"Equal: (\n    {self.node}\n)"


@dataclass
class StringNode:
    node: any

    def __repr__(self):
        return f"String: (\n    {self.node}\n)"


@dataclass
class KeywordNode:
    node: any

    def __repr__(self):
        return f"Keyword:(\n    {self.node}\n)"


@dataclass
class IdentifierNode:
    node: any

    def __repr__(self):
        return f"Identifier: (\n    {self.node}\n)"

