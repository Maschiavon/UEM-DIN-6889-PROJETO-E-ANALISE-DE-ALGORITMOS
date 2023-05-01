# 10. Defina um novo tipo chamado Lista1, que é como Lista, mas que não pode ser vazia, isto é, tem que
# ter pelo menos um elemento.
from dataclasses import dataclass
from typing import Union

@dataclass
class Link:
    primeiro: int
    resto: 'Lista'

    def _repr_(self):
        return f'Link({self.primeiro},{self.resto})'

@dataclass
class Link1:
    primeiro: int
    resto: 'Lista1'

    def _repr_(self):
        return f'Link({self.primeiro},{self.resto})'

# Uma Lista é um dos valores:
# - None
# - Link(int, Lista)
Lista = Union[None, Link]
#Exemplos
x: Lista = None
y: Lista = Link(10, None)
z: Lista = Link(20, Link(4,None))

# Uma Lista1 é um dos valores:
# - int
# - Link(int, Lista1)
Lista1 = Union[int, Link1]
x1: Lista1 = 1
y1: Lista1 = Link1(20, 3)
z1: Lista1 = Link1(40, Link1(50,6))