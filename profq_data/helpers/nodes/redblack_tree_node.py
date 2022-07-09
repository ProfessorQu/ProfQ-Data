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
        if node is None:
            return Node(data)

        # Check if it should go left
        if data < node.data:
            node.left = self.insert(node.left, data)
        # Or right
        else:
            node.right = self.insert(node.right, data)

        # Fixup the insertion
        return self.fixup(node)
    
    def fixup(self, node: Any) -> Any:
        """Fix the red black tree

        Args:
            node (Any): the node to fix

        Returns:
            Any: the new root
        """
        # Check if the node is red
        if node.color == "red":
            # Check if the node is the root
            if node.parent is None:
                node.color = "black"
            # Check if the parent is red
            elif node.parent.color == "red":
                # Check if the uncle is red
                if node.uncle().color == "red":
                    # Change the colors
                    node.parent.color = "black"
                    node.uncle().color = "black"
                    node.grandparent().color = "red"
                    # Fixup the tree
                    return self.fixup(node.grandparent())
                # Check if the node is a right child
                elif node.is_right_child():
                    # Rotate left
                    node.parent.rotate_left()
                    # Fixup the tree
                    return self.fixup(node.parent)
                # Check if the node is a left child
                elif node.is_left_child():
                    # Rotate right
                    node.parent.rotate_right()
                    # Fixup the tree
                    return self.fixup(node.parent)
            # Check if the node is a right child
            elif node.is_right_child():
                # Rotate left
                node.parent.rotate_left()
                # Fixup the tree
                return self.fixup(node.parent)
            # Check if the node is a left child
            elif node.is_left_child():
                # Rotate right
                node.parent.rotate_right()
                # Fixup the tree
                return self.fixup(node.parent)
        # Return the root
        return node
    
    def rotate_left(self) -> None:
        """Rotate the tree left
        """
        # Check if the node is the root
        if self.parent is None:
            self.color = "black"
        # Check if the node is a right child
        elif self.is_right_child():
            # Rotate left
            self.parent.rotate_left()
            # Fixup the tree
            self.parent.fixup(self.parent)
        # Check if the node is a left child
        elif self.is_left_child():
            # Rotate right
            self.parent.rotate_right()
            # Fixup the tree
            self.parent.fixup(self.parent)
        
    def rotate_right(self) -> None:
        """Rotate the tree right
        """
        # Check if the node is the root
        if self.parent is None:
            self.color = "black"
        # Check if the node is a left child
        elif self.is_left_child():
            # Rotate right
            self.parent.rotate_right()
            # Fixup the tree
            self.parent.fixup(self.parent)
        # Check if the node is a right child
        elif self.is_right_child():
            # Rotate left
            self.parent.rotate_left()
            # Fixup the tree
            self.parent.fixup(self.parent)
    
    