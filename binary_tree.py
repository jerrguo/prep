
class Node():
    """
    A single node within a Tree
    """

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BinaryTree():
    """
    Tree object of Nodes
    """


    def __init__(self):
        self.root = None


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
        if self.root == None:
            self.root = Node(val)
            return
        else:
            self._add(self.root, val)


    def remove(self, val):
        raise NotImplementedError('BinaryTree: Remove not implemented.')


    def _inorder(self, node):
        if node == None:
            return []

        return self._inorder(node.left) + [node] + self._inorder(node.right)


    def inorder_traversal(self):
        return self._inorder(self.root)


    def BFS(self, start):
        """
        Breadth First Search implementation
        """
        pass
