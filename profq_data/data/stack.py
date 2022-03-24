from profq_data.helpers.node import Node

class Stack:
    """An implementation of the Stack data structure
    """
    def __init__(self) -> None:
        """The init function
        """
        self.top = None
    
    def is_empty(self) -> bool:
        """Returns if the stack is empty

        Returns:
            bool: is the stack empty
        """
        return self.top is None
    
    def peek(self) -> int:
        """Peek the top value of the stack

        Returns:
            int: the value of top
        """
        return self.top.data
    
    def push(self, data: int):
        """Push a new value onto the stack

        Args:
            data (int): the data to push
        """
        node = Node(data)

        node.next = self.top
        self.top = node
    
    def pop(self) -> int:
        """Pop top from the stack

        Returns:
            int: the value of top
        """
        data = self.top.data
        self.top = self.top.next

        return data