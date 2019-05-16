from linked_list_step_2 import LinkedList, Node
from linked_list_step_4 import update_list


def test():
    l = LinkedList()
    l.add_node(10)
    l.add_node(3)
    l.add_node(7)
    l.add_node(9)

    # List: base -> 10 -> 3 -> 7 -> 9
    l = update_list(l)
    # List: base -> 3 -> 9

    assert isinstance(l, LinkedList)

    assert isinstance(l.base, Node)
    assert l.base.value is None
    assert l.base.next_node is not None

    assert l.count_nodes() == 2

    p = l.base.next_node
    assert p.value == 3
    p = p.next_node
    assert p.value == 9
    p = p.next_node
    assert p is None
