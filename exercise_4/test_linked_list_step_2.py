from linked_list_step_2 import LinkedList, Node


def count_nodes(l):
    n_nodes = 0
    p = l.base
    while p.next_node is not None:
        p = p.next_node
        n_nodes += 1
    return n_nodes


def test_init_list():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)
    assert hasattr(ll, 'base')
    assert isinstance(ll.base, Node)
    assert ll.base.value is None
    assert ll.base.next_node is None


def test_add_node_none():
    ll = LinkedList()
    ll.add_node(3)

    nodes_before = count_nodes(ll)
    ll.add_node(None)
    nodes_after = count_nodes(ll)
    assert nodes_before == nodes_after

    first_node = ll.base.next_node
    assert first_node.value == 3
    assert first_node.next_node is None


def test_add_node_first():
    ll = LinkedList()
    ll.add_node(3)

    assert ll.base.next_node is not None
    assert ll.base.next_node.value == 3


def test_add_node_second():
    ll = LinkedList()
    ll.add_node(3)
    ll.add_node('hello')

    first_node = ll.base.next_node
    second_node = first_node.next_node

    assert first_node.value == 3
    assert first_node.next_node is not None
    assert second_node.value == 'hello'
    assert second_node.next_node is None


def test_remove_node_last():
    ll = LinkedList()
    ll.add_node(3)
    ll.add_node('hello')
    ll.add_node(4)
    ll.add_node(5)
    ll.add_node(6)
    # list: 3 'hello' 4 5 6

    nodes_before = count_nodes(ll)
    ll.remove_node(6)
    nodes_after = count_nodes(ll)
    assert nodes_after == nodes_before - 1

    last = ll.base
    while last.next_node is not None:
        last = last.next_node
    assert last.value == 5


def test_remove_node_middle():
    ll = LinkedList()
    ll.add_node(3)
    ll.add_node('hello')
    ll.add_node(4)
    ll.add_node(5)
    # list: 3 'hello' 4 5

    nodes_before = count_nodes(ll)
    ll.remove_node(4)
    nodes_after = count_nodes(ll)
    assert nodes_after == nodes_before - 1

    p = ll.base.next_node
    assert p.value == 3
    p = p.next_node
    assert p.value == 'hello'
    p = p.next_node
    assert p.value == 5
    assert p.next_node is None


def test_remove_node_first():
    ll = LinkedList()
    ll.add_node(3)
    ll.add_node('hello')
    ll.add_node(5)
    # list: 3 'hello' 5

    nodes_before = count_nodes(ll)
    ll.remove_node(3)
    nodes_after = count_nodes(ll)
    assert nodes_after == nodes_before - 1

    p = ll.base.next_node
    assert p.value == 'hello'
    p = p.next_node
    assert p.value == 5
    assert p.next_node is None


def test_remove_node_none():
    ll = LinkedList()
    ll.add_node(3)
    ll.add_node('hello')
    ll.add_node(5)
    # list: 3 'hello' 5

    nodes_before = count_nodes(ll)
    ll.remove_node(None)
    nodes_after = count_nodes(ll)

    assert nodes_before == nodes_after


def test_remove_node_inexisting():
    ll = LinkedList()
    ll.add_node(3)
    ll.add_node('hello')
    ll.add_node(5)
    # list: 3 'hello' 5

    nodes_before = count_nodes(ll)
    ll.remove_node(4)
    nodes_after = count_nodes(ll)
    assert nodes_before == nodes_after


def test_remove_node_duplicate():
    ll = LinkedList()
    ll.add_node(3)
    ll.add_node('hello')
    ll.add_node(5)
    ll.add_node(5)
    # list: 3 'hello' 5 5

    nodes_before = count_nodes(ll)
    ll.remove_node(5)
    nodes_after = count_nodes(ll)
    assert nodes_after == nodes_before - 1


def test_count_nodes():
    ll = LinkedList()
    ll.add_node('hello')
    ll.add_node(5)
    assert ll.count_nodes() == 2


def test_count_nodes_empty():
    ll = LinkedList()
    assert ll.count_nodes() == 0
