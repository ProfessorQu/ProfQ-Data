from typing import Any

class Node:
    """A class for most data structures
    """
    def __init__(self, data: int) -> None:
        """The init function

        Args:
            data (int): what data to put in the node
        """
        self.data = data
        self.left = None
        self.right = None

    def search(self, node: Any, value: int) -> Any:
        """Search an item in the tree

        Args:
            node (Node): the node to start from
            value (int): the value to search for

        Returns:
            Node: the node with the key value
        """
        if node is None or node.data == value:
            return node

        if node.data < value:
            return self.search(node.right, value)

        return self.search(node.left, value)

    def insert(self, node: Any, value: int) -> Any:
        """Insert a value in the binary tree

        Args:
            node (Node): the node to start from
            value (int): the value to insert

        Returns:
            Node: the new tree
        """
        # Create the node if it's none
        if node is None:
            return Node(value)

        # Check if it should go left
        if value < node.data:
            node.left = self.insert(node.left, value)
        # Or right
        else:
            node.right = self.insert(node.right, value)
        
        # Return the final node
        return node

    def contains(self, node: Any, value: int) -> bool:
        """Tests if the binary tree contains a value

        Args:
            node (Node): the node to start from
            value (int): the value to check for

        Returns:
            bool: whether the value is in the tree
        """
        # If there is no node at the location of contains, return false
        if node is None:
            return False
        # If the current node is the value, return true
        elif value == node.data:
            return True
        # If it's less, traverse the left part of the tree
        elif value < node.data:
            return False if node.left is None else self.contains(node.left, value)
        # If it's greater, traverse the right part of the tree
        else:
            return False if node.right is None else self.contains(node.right, value)

    def delete(self, node: Any, value: int) -> Any:
        """Delete a node with a certain value

        Args:
            node (Node): the node to start from
            value (int): the value to delete

        Returns:
            Node: the new tree
        """
        # Remove the node if it's not there
        if node is None:
            return None
        
        # Traverse the left part of the tree
        if value < node.data:
            node.left = self.delete(node.left, value)
        # Traverse the right part of the tree
        elif value > node.data:
            node.right = self.delete(node.right, value)
        # We found the node to delete
        else:
            # If it has the right child, replace the current node with it
            if node.left is None:
                right_node = node.right
                node = None
                return right_node
            # If it has the left child, replace the current node with it
            elif node.right is None:
                left_node = node.left
                node = None
                return left_node
            
            # Get the minimum node at the right side of the tree
            min_node = self._get_minimum_node(node.right)
            # Set the current node data to the mimumum node data
            node.data = min_node.data
            # Remove the mimumum node
            node.right = self.delete(node.right, min_node.data)
        
        return node
    
    def _get_minimum_node(self, node: Any) -> Any:
        """Get the minimum node of the entire tree

        Args:
            node (Node): the node to start from

        Returns:
            Node: the new tree
        """
        current = node

        while current.left is not None:
            current = current.left
        
        return current

    def inorder(self, node: Any):
        """Go through a binary tree inorder (Left, Root, Right)

        Args:
            node (Node): the node to start from
        """
        if node is not None:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)
    
    def preorder(self, node: Any):
        """Go through a binary tree preorder (Root, Left, Right)

        Args:
            node (Node): the node to start from
        """
        if node is not None:
            self.inorder(node.left)
            self.inorder(node.right)
            print(node.key, end=" ")
    
    def postorder(self, node: Any):
        """Go through a binary tree postorder (Right, Left, Root)

        Args:
            node (Node): the node to start from
        """
        if node is not None:
            print(node.key, end=" ")
            self.inorder(node.left)
            self.inorder(node.right)
