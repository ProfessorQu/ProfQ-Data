from profq_data.helpers.linked_list import LinkedList
from profq_data.helpers.nodes.linked_list_node import Node

class SinglyLinkedList(LinkedList):
    """An implementation of a singly linked list
    """
    def push(self, data: int):
        """Prepend the data to the start of the array

        Args:
            data (int): the data to prepend
        """
        new_head = Node(data)

        # Point the new head to the previous head
        new_head.next = self.head
        
        # Set the new head
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

        # Loop over the array until the end
        current = self.head
        while current.next is not None:
            current = current.next

        # Add the new node
        current.next = Node(data)
        
        self._size += 1
        