# https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python
# 16/08/2022 Fergus Haak

# Your task is to return the list with elements from tree sorted by levels,
# which means the root element goes first, then root children (from left to right)
# are second and third, and so on.

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    list_by_levels = []
    if node is None:
        return list_by_levels

    current_node = [node]
    new_node = []
    for node_part in current_node:
        for side in [node_part.right, node_part.left]:
            print(f"side : {side.value}")
            if side.value is not None:
                list_by_levels.append(side.value)
            new_node.append(node_part.right)
            new_node.append(node_part.left)
        current_node = new_node
        new_node = []
        print(f"New node: {current_node}")

    return list_by_levels


print(tree_by_levels(None))
# should equal []
print(
    tree_by_levels(
        Node(
            Node(None,
                 Node(None, None, 4),
                 2),
            Node(
                Node(None, None, 5),
                Node(None, None, 6),
                3),
            1)
        )
    )
# Should equal [1, 2, 3, 4, 5, 6]
