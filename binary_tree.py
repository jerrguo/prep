
class Node():
    """
    A single node within a Tree
    """

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def __str__(self):
        return f'<Node data:{{self.data}} left:{{self.left.data}} right:{{self.right.data}}>'


class BinaryTree():
    """
    Tree object of Nodes
    """


    def __init__(self):
        self.root = None
        self.count = 0


    def __len__():
        return self.count


    def _add(self, node, val):
        if val > node.data:
            if node.right == None:
                node.right = Node(val)
            else:
                self._add(node.right, val)
        if val <= node.data:
            if node.left == None:
                node.left = Node(val)
            else:
                self._add(node.left, val)


    def add(self, val):
        """
        Add a new Node with data `val` into the Binary Tree
        """
        if self.root == None:
            self.root = Node(val)
        else:
            self._add(self.root, val)

        self.count += 1


    def remove(self, val):
        """
        Remove a Node with data `val` from the Binary Tree
        """
        pass


    def _traverse(self, node, mode):
        """
        Traverses the Binary Tree recursively to return traversal order
        """
        if node == None:
            return []

        if mode == "inorder":
            return (
                self._traverse(node.left, mode="inorder") +
                [node] +
                self._traverse(node.right, mode="inorder")
            )
        elif mode == "preorder":
            return (
                [node] +
                self._traverse(node.left, mode="preorder") +
                self._traverse(node.right, mode="preorder")
            )
        else:
            return (
                self._traverse(node.left, mode="postorder") +
                self._traverse(node.right, mode="postorder") +
                [node]
            )


    def inorder_traversal(self):
        return self._traverse(self.root, mode="inorder")

    def preorder_traversal(self):
        return self._traverse(self.root, mode="preorder")

    def postorder_traversal(self):
        return self._traverse(self.root, mode="postorder")
