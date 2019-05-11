import pytest
from step_1 import Node


def test_node_with_attributest():
    node = Node(1, 'next')
    assert isinstance(node, Node)
    assert hasattr(node, 'value') and hasattr(node, 'next_node')
    assert node.value == 1
    assert node.next_node == 'next'


def test_defaults():
    node = Node()
    assert isinstance(node, Node)
    assert hasattr(node, 'value') and hasattr(node, 'next_node')
    assert node.value is None
    assert node.next_node is None
