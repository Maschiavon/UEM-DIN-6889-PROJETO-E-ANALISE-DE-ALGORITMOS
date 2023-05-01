from dataclasses import dataclass
from typing import Union, List

@dataclass
class Link:
    primeiro: int
    resto: 'Lista'

    def __repr__(self):
        return f'Link({self.primeiro}, {self.resto})'

Lista = Union[None, Link]
# Uma Lista é um dos valores:
# - None
# - Link(int, Lista)

# Cria uma nova lista com os elementos
# de lst e v no final
def insere_fim(v: int, lst: Lista) -> Lista:
    if lst is None:
        return Link(v, None)
    else:
        return Link(lst.primeiro, insere_fim(v, lst.resto))

assert insere_fim(3, None) == Link(3, None)
assert insere_fim(4, Link(2, Link(1, None))) == Link(2, Link(1, Link(4, None)))

# Cria uma nova lista com os elementos
# de lst de tras para frente.
def inverte(lst: Lista) -> Lista:
    if lst is None:
        return None
    else:
        return insere_fim(lst.primeiro, inverte(lst.resto))

assert inverte(None) == None
assert inverte(Link(5, Link(2, Link(7, None)))) == Link(7, Link(2, Link(5, None)))

# Cria uma nova lista com os elementos
# de lst de tras para frente.
def inverte_it(lst: Lista) -> Lista:
    # Invariante:
    # inv contem os elementos em ordem
    # invertida que vieram antes de cur.
    inv = None
    p = lst
    while p != None:
        inv = Link(p.primeiro, inv)
        p = p.resto
    return inv


assert inverte_it(None) == None
assert inverte_it(Link(5, Link(2, Link(7, None)))) == Link(7, Link(2, Link(5, None)))
