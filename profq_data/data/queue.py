from profq_data.helpers.node import Node

class Queue:
    """An implementation of the Queue data structure
    """
    def __init__(self) -> None:
        """The init function
        """
        self.head = None
        self.tail = None
    
    def is_empty(self) -> bool:
        """Returns if the queue is empty

        Returns:
            bool: is the queue empty
        """
        return self.head is None
    
    def peek(self) -> int:
        """Peek the head value of the queue

        Returns:
            int: the value of the head
        """
        return self.head.data
    
    def enqueue(self, data: int):
        """Add an item to the end of the queue

        Args:
            data (int): the data to add
        """
        node = Node(data)
        if self.tail is not None:
            self.tail.next = node
        
        self.tail = node

        if self.head is None:
            self.head = node
    
    def dequeue(self) -> int:
        """Dequeue the head

        Returns:
            int: the value of the head
        """
        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        return data