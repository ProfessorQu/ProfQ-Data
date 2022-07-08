from profq_data.helpers.linked_list import LinkedList
from profq_data.helpers.nodes.linked_list_node import Node
from profq_data.helpers.skiplist_linked_list import SkipList_LinkedList

import random

class SkipList(LinkedList):
    """An implementation of a skip list
    """
    def __init__(self) -> None:
        super().__init__()

        self.layer2 = SkipList_LinkedList()

    def insert(self, data: int):
        """Inserts data at the right place in the list

        Args:
            data (int): the data to insert
        """
        
        # If the list is empty
        if self.head is None:
            self.head = Node(data)
            self.layer2.head = Node(data)
            self.layer2.head.layer_below = self.head
            self._size += 1
            return

        # Traverse the layer2 list to find the right place to insert
        current2 = self.layer2.head
        while current2.next is not None and current2.next.data <= data:
            current2 = current2.next

        # Traverse the list to find the right place to insert
        current = current2.layer_below
        while current.next is not None and current.next.data <= data:
            current = current.next
        
        # Create a new node
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

        # See if the new node should be added to the layer2 list
        if random.random() < 0.5:
            new_node2 = Node(data)
            new_node2.next = current2.next
            current2.next = new_node2
            new_node2.layer_below = new_node

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
            self._size -= 1
            return

        # Loop over the list to find the item with the data
        current = self.head
        for _ in range(index):
            current = current.next
        
        # Reroute the next to the next next
        # "Skip" the next node
        current.next = current.next.next
        
        self._size -= 1

    def print_items(self):
        """Prints the items in the list
        """
        self.layer2.print_items()
        super().print_items()

