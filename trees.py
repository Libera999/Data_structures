class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 0

    # A function to insert a new node with the given key value to BST
    def Insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                Insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                Insert(root.left, node)

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value),
        if self.right:
            self.right.PrintTree()

    def TreeHeight(self, node):
        if node is None:
            return -1

        else:

            # depth of each subtree
            lDepth = self.TreeHeight(node.left)
            rDepth = self.TreeHeight(node.right)

            # Use the larger one
            if (lDepth > rDepth):
                return lDepth + 1
            else:
                return rDepth + 1



root = Node(9)
Insert(root, Node(5))
Insert(root, Node(2))
Insert(root, Node(4))
Insert(root, Node(11))
root.PrintTree()
print(root.TreeHeight(root))
