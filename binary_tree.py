
class Node():
    """
    A single node within a Tree
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
        if self.left == None:
            return -1

        node = self.left
        while node.right != None:
            node = node.right
        return node


    def right_successor(self):
        if self.right == None:
            return -1

        node = self.right
        while node.left != None:
            node = node.left
        return node


    def successor(self):
        if self.left_successor():
            return self.left_successor()
        if self.right_successor():
            return self.right_successor()

        return None



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
            if node.left == None:
                temp = node.right
                node = None
                print(val, 'LEFT is NONE')
                return temp
            elif node.right == None:
                temp = node.left
                node = None
                print(val, 'RIGHT is NONE')
                return temp

            temp = node.right_successor()
            print(val, temp)
            node.data = temp.data
            node.right = self._remove(val, node.right)

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
        return self._traverse(self.root, mode="inorder")


    def preorder_traversal(self):
        return self._traverse(self.root, mode="preorder")


    def postorder_traversal(self):
        return self._traverse(self.root, mode="postorder")


if __name__ == '__main__':
    """
    For Testing...
    """
    tree = BinaryTree()
    tree.add(2)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(2.5)
    tree.add(3.5)
    tree.add(2.75)
    print(tree.inorder_traversal())
    tree.remove(4)
    tree.remove(5)
    tree.remove(2)
    tree.remove(66)
    tree.remove(2)
    tree.remove(2.75)
    print(tree.inorder_traversal())
