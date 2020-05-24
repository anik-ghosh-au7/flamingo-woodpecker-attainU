class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.add_node(self.root, data)

    def add_node(self, node, data):
        if node.data < data:
            self.add_right(node, data)
        else:
            self.add_left(node, data)

    def add_right(self, node, data):
        if node.right is None:
            node.right = Node(data)
        else:
            self.add_node(node.right, data)

    def add_left(self, node, data):
        if node.left is None:
            node.left = Node(data)
        else:
            self.add_node(node.left, data)


def levelOrder_traversal(root):  # root --> left --> right
    queue = [root]
    while queue:
        temp_node = queue.pop(0)
        print(temp_node.data, end=" ")
        if temp_node.left:
            queue.append(temp_node.left)
        if temp_node.right:
            queue.append(temp_node.right)


tree = BinaryTree()
tree.add(3)
tree.add(5)
tree.add(1)
tree.add(7)
tree.add(2)
tree.add(4)
tree.add(6)

print('level order traversal of tree : ')
levelOrder_traversal(tree.root)  # 3 1 5 2 4 7 6

# tree structure

#               3
#             /   \
#            1     5
#             \   /  \
#              2 4    7
#                    /
#                   6
