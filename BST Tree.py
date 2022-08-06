# defining BST tree class
# introducing recursive methods: Insert, Search, PrintTree, TreeHeight

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 0

    # A function to insert a new node with the given key value to BST
    def Insert(self, root, k):

        if root is None:  # if tree is empty
            return Node(k)
        else:
            if root.value == k:
                return root
            elif root.value < k:
                root.right = self.Insert(root.right, k)
            else:
                root.left = self.Insert(root.left, k)
        return root

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

    def Search(self, root, value):

        if (root == None):
            return False

        if (root.value == value):
            return True

        if (value < root.value):
            return self.Search(root.left, value)

        elif (value > root.value):
            return self.Search(root.right, value)

        return False


r = Node(9)
r.Insert(r, 5)
r.Insert(r, 2)
r.Insert(r, 27)
r.Insert(r, 11)

r.PrintTree()
print("Tree height:", r.TreeHeight(r))

key = input("Search for value: ")
print(f'Is there a node with value = {key} ? ', r.Search(r, int(key)))
