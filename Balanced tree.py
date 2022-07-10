import sys

class Node:
    MIN_VALUE = -sys.maxsize-1
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 0

    # A function to insert a new node with the given key value to BST
    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if root.value < node.value:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)

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


    def isBalanced(self, root):
        if (root == None):
            return True

        height_diff = self.TreeHeight(root.left) - self.TreeHeight(root.right)
        if abs(height_diff) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    # Checking the height of each subtree as we recurse down from the root.
    # On each node, we recursively get the heights of the left and right subtrees through the checkHeight
    # method. If the subtree is balanced, then checkHeight will return the actual height of the subtree. If the
    # subtree is not balanced, then c h ec kHeight will return an error code. We will immediately break and
    # return an error code from the current call.

    def checkHeight(self, root):
        if root==None:
            return -1
        leftHeight=checkHeight(root.left)
        if leftHeight==MIN_VALUE:
            return int(MIN_VALUE) #pass error

        rightHeight=checkHeight(root.right)
        if (rightHeight == Integer.MIN_VALUE):
            return int(MIN_VALUE)  #pass error

        height_diff=abs(rightHeight-leftHeight)
        if height_diff>1:
            return int(MIN_VALUE)   #pass error

        else:
            return max(leftHeight,rightHeight)+1

    def isBalanced2(self, root):
        return checkHeight(root) != int(MIN_VALUE)

tree = Node(9)
tree.insert(tree,Node(5))
tree.insert(tree,Node(2))
#tree.insert(tree,Node(4))
tree.insert(tree,Node(11))
tree.insert(tree,Node(12))
tree.insert(tree,Node(14))
tree.PrintTree()

print(tree.isBalanced2(tree))

print(tree.TreeHeight(tree))
