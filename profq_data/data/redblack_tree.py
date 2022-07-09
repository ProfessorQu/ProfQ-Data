from profq_data.helpers.nodes.redblack_tree_node import Node
from profq_data.data.binary_tree import BinaryTree

class RedBlackTree(BinaryTree):
    """An implementation of a binary tree
    """
    def __init__(self) -> None:
        """The init function
        """
        self.root = None
    
    def search(self, value: int) -> Node:
        """Search an item in the tree

        Args:
            value (int): the value to search for
        
        Returns:
            Node: the found node
        """
        return self.root.search(self.root, value)
    
    def insert(self, value: int) -> Node:
        """Insert a value in the binary tree

        Args:
            value (int): the value to insert

        Returns:
            Node: the new tree
        """
        if self.root is None:
            self.root = Node(value)
            self.root.color = "black"
            return

        self.root = self.root.insert(self.root, value)
    
    def contains(self, value: int) -> bool:
        """Tests if the binary tree contains a value

        Args:
            value (int): the value to check for

        Returns:
            bool: whether the value is in the tree
        """
        return self.root.contains(self.root, value)

    def delete(self, value: int):
        self.root = self.root.delete(self.root, value)

    def rotate_left(self):
        """Rotate a node to the left
        """
        self.root = self.root.rotate_left(self.root)
    
    def rotate_right(self):
        """Rotate a node to the right
        """
        self.root = self.root.rotate_right(self.root)

    def inorder(self):
        """Go through a binary tree inorder (Left, Root, Right)
        """
        self.root.inorder(self.root)
        print()
    
    def preorder(self):
        """Go through a binary tree preorder (Root, Left, Right)
        """
        self.root.preorder(self.root)
        print()
    
    def postorder(self):
        """Go through a binary tree postorder (Right, Left, Root)
        """
        self.root.postorder(self.root)
        print()
