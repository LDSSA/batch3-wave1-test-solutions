from step_2 import LinkedList, Node
from step_3 import create_list


def test():
    l = create_list()

    assert isinstance(l, LinkedList)

    assert isinstance(l.base, Node)
    assert l.base.value is None
    assert l.base.next_node is not None

    assert l.count_nodes() == 4

    p = l.base.next_node
    assert p.value == 10
    p = p.next_node
    assert p.value == 3
    p = p.next_node
    assert p.value == 7
    p = p.next_node
    assert p.value == 9
    p = p.next_node
    assert p is None
