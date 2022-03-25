class LinkedList:
    """A base class for singly and doubly linked lists
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
    
    def contains(self, data: int) -> bool:
        """Tests if the linked list contains data

        Args:
            data (int): the data to find in the list

        Returns:
            bool: if the data is contained in the list
        """
        # If the list is empty
        if self.head is None:
            return

        # If data from head is equal to data, return True
        if self.head.data == data:
            return True

        # Loop over all the items in the linked list
        current = self.head
        while current is not None:
            # Return true if the current's data is equal to the to search data
            if current.data == data:
                return True
            
            current = current.next
        
        # Return false if it doesn't contain
        return False
    
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
    
    def print_items(self):
        """Print the list
        """
        if self.head is None:
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")

            current = current.next
        
        print()