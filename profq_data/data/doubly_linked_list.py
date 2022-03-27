from profq_data.helpers.linked_list import LinkedList
from profq_data.helpers.nodes.linked_list_node import Node

class DoublyLinkedList(LinkedList):
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
        # Point the previous head to the new head
        new_head.prev = self.head
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
        # Set the next's previous
        current.next.prev = current
        
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
            self.head.prev = None
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
                if current.next is not None:
                    current.next.prev = current
                break
            
            current = current.next
            
        self._size -= 1

    def delete_at_index(self, index: int) -> int:
        """Delete an item at index

        Args:
            index (int): the index for the item to delete

        Raises:
            IndexError: when the index is not in the range of the linked list

        Returns:
            int: the value of the node at index
        """
        # If the list is empty
        if self.head is None:
            return
        
        # Test if index is in range of the linked list
        if index < 0 or index > self._size - 1:
            raise IndexError(f"Index {index} not in linked list {self}")

        # If data from head is equal to data, remove data
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            self._size -= 1
            return

        # Loop over the list to find the item with the data
        current = self.head
        for _ in range(index):
            current = current.next
        
        # Reroute the next to the next next
        # "Skip" the next node
        current.next = current.next.next
        current.next.prev = None
        
        self._size -= 1
    