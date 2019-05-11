class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.base = Node()

    def add_node(self, value):
        if value is None:
            return

        # p is a pointer set as the base of the list
        # Then we bring pointer to the last node of the list
        p = self.base
        while p.next_node is not None:
            p = p.next_node

        # This sets the next node of the last node as a new node
        # The new node is now the last in the list
        p.next_node = Node(value)

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

    def count_nodes(self):
        count = 0

        p = self.base.next_node
        while p is not None:
            count += 1
            p = p.next_node

        return count
