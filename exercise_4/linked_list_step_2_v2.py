from linked_list_step_1 import Node


class LinkedList:
    """
    This is another possible implementation of the LinkedList exercise,
    which is a bit more efficient because doesn't require running through the
    entire list to add new nodes.
    However, it's a bit harder to read!
    """
    def __init__(self):
        self.base = Node()
        self._last_node = None

    def add_node(self, value):
        if value is None:
            return

        # If adding the first node, we need to change base
        if self.base.next_node is None:
            self.base.next_node = Node(value)
            self._last_node = self.base.next_node
            return

        # Otherwise, we already have nodes in the list
        # and self._last_node is the last one
        self._last_node.next_node = Node(value)
        self._last_node = self._last_node.next_node

    def remove_node(self, value):
        if value is None:
            return

        # p starts as the base of the list
        # And moves forward until the next node has value,
        # or until we reach the end of the list
        p = self.base
        while (p.next_node is not None) and (p.next_node.value != value):
            p = p.next_node

        # If we reached the end of the list without finding value, return
        if p.next_node is None:
            return

        # Otherwise, remove the node with value from the list
        p.next_node = p.next_node.next_node

        # If the node we're removing is the last,
        # we need to adjust self._last_node
        if p.next_node is None:
            self._last_node = p

    def count_nodes(self):
        count = 0

        p = self.base.next_node
        while p is not None:
            count += 1
            p = p.next_node

        return count

    def print_list(self):
        s = 'base ->'
        p = self.base.next_node
        while p is not None:
            s += f" {p.value} ->"
            p = p.next_node

        print(s)
