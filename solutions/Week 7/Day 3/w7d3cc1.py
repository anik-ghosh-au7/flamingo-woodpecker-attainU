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


def inOrder_traversal(root):  # left --> root --> right
    if root is None:
        return

    inOrder_traversal(root.left)
    print(root.data, end=" ")
    inOrder_traversal(root.right)


def flatten(root):
    if root is None or (root.left is None and root.right is None):
        return

    if root.left is not None:
        flatten(root.left)

        temp_node = root.right
        root.right = root.left
        root.left = None
        curr_node = root.right
        while curr_node.right is not None:
            curr_node = curr_node.right
        curr_node.right = temp_node

    flatten(root.right)


def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


tree = BinaryTree()
tree.add(3)
tree.add(5)
tree.add(1)
tree.add(7)
tree.add(2)
tree.add(4)
tree.add(6)

inOrder_traversal(tree.root)  # 1 2 3 4 5 6 7
print('Height of tree : ', height(tree.root))  # 4

flatten(tree.root)

print('after flattening : ')
inOrder_traversal(tree.root)  # 3 1 2 5 4 7 6
print('Height of tree : ', height(tree.root))  # 7

# tree structure (before flattening)

#               3
#             /   \
#            1     5
#             \   /  \
#              2 4    7
#                    /
#                   6


# tree structure (after flattening)

#               3
#             /   \
#            1     5
#             \   /  \          ======>
#              2 4    7
#                      \
#                       6


#               3
#             /   \
#            1     5
#             \     \
#              2     4          ======>
#                     \
#                      7
#                       \
#                        6


#               3
#                \
#                 1
#                  \
#                   2
#                    \
#                     5         (Final tree after flattening)
#                      \
#                       4
#                        \
#                         7
#                          \
#                           6
