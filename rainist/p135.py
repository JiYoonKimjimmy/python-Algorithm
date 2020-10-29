from collections import deque
import copy

min_node = 0
dq = deque()
copy_dq = []


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def init_tree():
    node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1), None)))
    print_tree(node)


def print_tree(node):
    if node is None:
        return

    global min_node
    global copy_dq
    if min_node == 0:
        min_node = node.data
    else:
        if min_node > node.data:
            min_node = node.data
            copy_dq = copy.deepcopy(dq)

    dq.append(node.data)

    print_tree(node.left)
    print_tree(node.right)
    dq.pop()


init_tree()
print(sum(copy_dq) + min_node)
