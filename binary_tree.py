

class Node():
    """
    A single Node within a Tree
    """


    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


    def __str__(self):
        if self.left == None:
            left_data = None
        else:
            left_data = self.left.data

        if self.right == None:
            right_data = None
        else:
            right_data = self.right.data

        return f'<Node data:{self.data} left:{left_data} right:{right_data}>'


    def __repr__(self):
        if self.left == None:
            left_data = None
        else:
            left_data = self.left.data

        if self.right == None:
            right_data = None
        else:
            right_data = self.right.data

        return f'<Node data:{self.data} left:{left_data} right:{right_data}>'


    def left_successor(self):
        """
        Returns the left successor to the Node
        """
        if self.left == None:
            return -1

        node = self.left
        while node.right != None:
            node = node.right
        return node


    def right_successor(self):
        """
        Returns the right successor to the Node
        """
        if self.right == None:
            return -1

        node = self.right
        while node.left != None:
            node = node.left
        return node


    def successor(self):
        """
        Returns the successor to the Node with left successor having priority
        """
        if self.left_successor():
            return self.left_successor()
        if self.right_successor():
            return self.right_successor()

        return None



class BinaryTree():
    """
    Binary Tree object of Nodes
    """


    def __init__(self):
        self.root = None
        self.count = 0


    def __len__(self):
        return self.count


    def _add(self, node, val):
        """
        Recursive function to add node into Binary Tree
        """
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


    def _remove(self, val, node):
        """
        Recursive function to remove node from Binary Tree
        """
        if node == None:
            return node

        if val < node.data:
            node.left = self._remove(val, node.left)
        elif val > node.data:
            node.right = self._remove(val, node.right)
        else:
            self.count -= 1
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                temp = node.right_successor()
                node.data = temp.data
                # Removing the successor node will decrement `self.count` incorrectly
                self.count += 1
                node.right = self._remove(temp.data, node.right)

        return node



    def remove(self, val):
        """
        Remove a Node with data `val` from the Binary Tree
        """
        self.root = self._remove(val, self.root)


    def _traverse(self, node, mode):
        """
        Traverses the Binary Tree recursively to return traversal order
        """
        if node == None:
            return []

        if mode == "inorder":
            return (
                self._traverse(node.left, mode="inorder") +
                [node.data] +
                self._traverse(node.right, mode="inorder")
            )
        elif mode == "preorder":
            return (
                [node.data] +
                self._traverse(node.left, mode="preorder") +
                self._traverse(node.right, mode="preorder")
            )
        else:
            return (
                self._traverse(node.left, mode="postorder") +
                self._traverse(node.right, mode="postorder") +
                [node.data]
            )


    def inorder_traversal(self):
        """ Performs Inorder Traversal """
        return self._traverse(self.root, mode="inorder")


    def preorder_traversal(self):
        """ Performs Preorder Traversal """
        return self._traverse(self.root, mode="preorder")


    def postorder_traversal(self):
        """ Performs Postorder Traversal """
        return self._traverse(self.root, mode="postorder")


if __name__ == '__main__':
    """
    For Testing...
    """
    # tree = BinaryTree()
    # tree.add(2)
    # tree.add(2)
    # tree.add(3)
    # tree.add(4)
    # tree.add(5)
    # tree.add(2.5)
    # tree.add(3.5)
    # tree.add(2.75)
    # print(len(tree))
    # print(tree.inorder_traversal())
    # tree.remove(4)
    # tree.remove(5)
    # tree.remove(2)
    # tree.remove(66)
    # tree.remove(2)
    # tree.remove(2.75)
    # print(len(tree))
    # print(tree.inorder_traversal())
    # print(tree.postorder_traversal())
