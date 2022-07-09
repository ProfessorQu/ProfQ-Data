from profq_data.helpers.nodes.binary_tree_node import Node

from typing import Any

class Node(Node):
    """A red black tree node
    """
    def __init__(self, data: int) -> None:
        super().__init__(data)

        self.color = "red"
        self.parent = None
    
    def __str__(self) -> str:
        """Return the string representation of the node
        """
        return f"""{self.data} ({self.color}). Parent: {self.parent.data if self.parent else None}.
        Left: {self.left.data if self.left else None}. Right: {self.right.data if self.right else None}"""

    def insert(self, node: Any, data: int) -> Any:
        """Insert a value in the red black tree

        Args:
            node (Any): the node to start from
            data (int): the value to insert

        Returns:
            Any: the new root
        """
        # Create the node if it's none
        if node is None:
            return Node(data)

        # Check if it should go left
        if data < node.data:
            node.left = self.insert(node.left, data)
        # Or right
        else:
            node.right = self.insert(node.right, data)

        # Return the final node
        return self.fix_insert(node)
    
    def fix_insert(self, node: Any) -> Any:
        """Fix the tree after an insert
        """
        # If the node is the root, set it to black
        if node.parent is None:
            node.color = "black"
            return node

        # If the parent is black, we're done
        if node.parent.color == "black":
            return node

        # If the uncle is red, we need to rotate
        if node.uncle().color == "red":
            node.parent.color = "black"
            node.uncle().color = "black"
            node.grandparent().color = "red"
            return self.fix_insert(node.grandparent())

        # If the parent is red and the uncle is black, we need to rotate
        if node.parent.color == "red" and node.uncle().color == "black":
            if node.is_left_child() and node.parent.is_left_child():
                node.parent.color = "black"
                node.grandparent().color = "red"
                node.rotate_right()
            elif node.is_right_child() and node.parent.is_right_child():
                node.parent.color = "black"
                node.grandparent().color = "red"
                node.rotate_left()
            elif node.is_left_child() and node.parent.is_right_child():
                node.parent.color = "black"
                node.grandparent().color = "red"
                node.rotate_left()
            elif node.is_right_child() and node.parent.is_left_child():
                node.parent.color = "black"
                node.grandparent().color = "red"
                node.rotate_right()

        # Return the final node
        return node
    
    def rotate_left(self, node: Any) -> Any:
        """Rotate the node to the left
        """
        # Get the right child
        right_child = node.right

        # Move the right child to the left child
        node.right = right_child.left

        # If the right child has a left child, set it's parent to the node
        if right_child.left:
            right_child.left.parent = node

        # Set the right child's parent to the node's parent
        right_child.parent = node.parent

        # If the node is the root, set the right child as the root
        if node.parent is None:
            self.root = right_child

        # If the node is a left child, set the right child as the left child
        elif node.is_left_child():
            node.parent.left = right_child

        # If the node is a right child, set the right child as the right child
        elif node.is_right_child():
            node.parent.right = right_child

        # Set the right child's left to the node
        right_child.left = node

        # Set the node's parent to the right child
        node.parent = right_child

        # Return the right child
        return right_child
    
    def rotate_right(self, node: Any) -> Any:
        """Rotate the node to the right
        """
        # Get the left child
        left_child = node.left

        # Move the left child to the right child
        node.left = left_child.right

        # If the left child has a right child, set it's parent to the node
        if left_child.right:
            left_child.right.parent = node

        # Set the left child's parent to the node's parent
        left_child.parent = node.parent

        # If the node is the root, set the left child as the root
        if node.parent is None:
            self.root = left_child

        # If the node is a left child, set the left child as the left child
        elif node.is_left_child():
            node.parent.left = left_child

        # If the node is a right child, set the left child as the right child
        elif node.is_right_child():
            node.parent.right = left_child

        # Set the left child's right to the node
        left_child.right = node

        # Set the node's parent to the left child
        node.parent = left_child

        # Return the left child
        return left_child
    
    def uncle(self) -> Any:
        """Return the uncle of the node
        """
        # If the node has no parent, return None
        if self.parent is None:
            return None

        # If the node is a left child, return the right child of the parent's parent
        if self.is_left_child():
            return self.parent.parent.right

        # If the node is a right child, return the left child of the parent's parent
        if self.is_right_child():
            return self.parent.parent.left
    
    def is_left_child(self) -> bool:
        """Return whether the node is a left child
        """
        return self.parent and self.parent.left == self
    
    def is_right_child(self) -> bool:
        """Return whether the node is a right child
        """
        return self.parent and self.parent.right == self
    
    def grandparent(self) -> Any:
        """Return the grandparent of the node
        """
        return self.parent.parent
    