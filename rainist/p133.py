sorted_nodes = []


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def init_tree():
    node = Node(10, Node(5), Node(30, Node(22, None, None), Node(35, None, None)))

    sort_tree(node)


def sort_tree(node):
    if node is None:
        return

    sort_tree(node.left)
    sorted_nodes.append(node.data)
    sort_tree(node.right)


init_tree()
sorted_nodes = sorted(sorted_nodes)
print(sorted_nodes)
index = sorted_nodes.index(22)
print(sorted_nodes[index + 1])


