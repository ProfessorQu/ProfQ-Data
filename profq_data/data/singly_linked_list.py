from email import header
from unittest.mock import NonCallableMagicMock
from profq_data.helpers.node import Node

class SinglyLinkedList:
    """An implementation of a singly linked list
    """
    def __init__(self) -> None:
        """The init function
        """
        self.head = None

        self._size = 0
    
    def peek(self) -> int:
        """Peek the head value of the linked lsit

        Returns:
            int: the value of the head
        """
        return self.head.data
    
    def __len__(self) -> int:
        """Gets the size of the linked list

        Returns:
            int: the size of the linked list
        """
        return self._size

    def push(self, data: int):
        """Prepend the data to the start of the array

        Args:
            data (int): the data to prepend
        """
        new_head = Node(data)

        new_head.next = self.head
        self.head = new_head

        self._size += 1

    def append(self, data: int):
        """Append data to the end of the array

        Args:
            data (int): the data to append
        """
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = Node(data)
        
        self._size += 1

    def delete_with_value(self, data: int):
        """Delete a node with a certain value

        Args:
            data (int): the value of the node to be deleted
        """
        # If the list is empty
        if self.head is None:
            return
            

        # If data from head is equal to data, remove data
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return
        
        # Loop over the list to find the item with the data
        current = self.head
        while current.next is not None:
            # If next data is equal to data
            # Reroute the next to the next next
            # "Skip" the next node
            if current.next.data == data:
                current.next = current.next.next
                break
            
            current = current.next
            
        self._size -= 1
    
    def delete_at_index(self, index: int) -> int:
        # If the list is empty
        if self.head is None:
            return
        
        if index < 0 or index > self._size - 1:
            raise IndexError(f"Index {index} not in linked list {self}")

        # If data from head is equal to data, remove data
        if index == 0:
            self.head = self.head.next
            self._size -= 1
            return

        # Loop over the list to find the item with the data
        current = self.head

        for _ in range(index):
            current = current.next

        current.next = current.next.next
        
        self._size -= 1
        