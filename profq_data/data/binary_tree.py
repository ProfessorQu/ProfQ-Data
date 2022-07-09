from profq_data.helpers.node_manager import NodeManager
from profq_data.helpers.nodes.binary_tree_node import Node

class BinaryTree:
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
            return self.root

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

    def inorder(self):
        """Go through a binary tree inorder (Left, Root, Right)
        """
        self.root = self.root.inorder(self.root)
    
    def preorder(self):
        """Go through a binary tree preorder (Root, Left, Right)

        Args:
            node (Node): the node to start from
        """
        self.root = self.root.preorder(self.root)
    
    def postorder(self):
        """Go through a binary tree postorder (Right, Left, Root)

        Args:
            node (Node): the node to start from
        """
        self.root = self.root.postorder(self.root)
