from profq_data.helpers.nodes.hashtable_node import Node
from profq_data.data.singly_linked_list import SinglyLinkedList

INITIAL_CAPACITY = 100

class HashTable:
    """An implementation of the Hash Table data structure
    """
    def __init__(self) -> None:
        """The init function
        """
        self.capacity = INITIAL_CAPACITY
        self._size = 0
        self.buckets = [None] * self.capacity
    
    def __len__(self) -> int:
        """Return the length of the hash table

        Returns:
            int: length of the table
        """
        return self._size
    
    def hash(self, key: str) -> int:
        """Hash the key for an index

        Args:
            key (str): the key to hash

        Returns:
            int: the index
        """
        hashsum = 0

        # For each character in the key
        for idx, char in enumerate(key):
            # Add (index + length of key) ^ (current char code)
            hashsum += (idx + len(key)) ** ord(char)
            # Modules to keep hashsum in range [0, self.capacity - 1]
            hashsum %= self.capacity
        
        return hashsum
    
    def insert(self, key: str, data: int):
        """Insert an item at key

        Args:
            key (str): the key of the item
            data (int): the value of the item
        """
        # Increase size
        self._size += 1
        # Calculate index
        index = self.hash(key)
        # Get the node in the list if there is one
        node = self.buckets[index]

        # No collision, just add the node at the index
        if node is None:
            self.buckets[index] = Node(key, data)
            return
        
        # Collision, go to the end of the linked list and add it
        current = node
        while current.next is not None:
            current = current.next
        
        current.next = Node(key, data)
    
    def find(self, key: str) -> int:
        """Find an item according to a key

        Args:
            key (str): the key to find the item to

        Returns:
            int: the data at the key
        """
        node = self._get_node_by_key(key)

        # Now node is the requested data or None
        return None if node is None else node.data
    
    def remove(self, key: str):
        """Remove an item in the hash table and return the data

        Args:
            key (str): the key for the data to remove

        Returns:
            int: the data of the key
        """
        # Get node by index
        node = self._get_node_by_key(key)
        if node is None:
            return None
        
        # Get the index
        index = self.hash(key)
        # Get the node in the list if there is one
        current = self.buckets[index]
        
        # If the node to remove is the first node
        if current.key == key:
            self.buckets[index] = current.next
            # Decrease size
            self._size -= 1

            return current.data
        
        # Traverse the linked list
        while current.next is not None:
            # If we have found the node
            if current.next.key == key:
                # Remove the node
                value = current.next.data
                current.next = current.next.next
                # Decrease size
                self._size -= 1

                return value
            
            current = current.next
        
        return None
        # Get node by index
        # index = self.hash(key)
        # current = self.buckets[index]

        # if current.key == key:
        #     self._size -= 1
        #     return current.data

        # # Loop over the list to find the item with the data
        # while current.next is not None:
        #     # If next data is equal to data
        #     # Reroute the next to the next next
        #     # "Skip" the next node
        #     if current.next.key == key:
        #         current.next = current.next.next
        #         self._size -= 1

        #         return current.data
                
        #     current = current.next
    
    def _get_node_by_key(self, key: str) -> Node:
        """Get a node by a certain key

        Args:
            key (str): the key to find the node to

        Returns:
            Node: the node with the key
        """
        # Get node by index
        index = self.hash(key)
        result = self.buckets[index]

        # Traverse linked list
        while result is not None and result.key != key:
            result = result.next

        # Return node
        return result
    
    def print_items(self):
        """Print all items in the hash table
        """
        for idx, node in enumerate(self.buckets):
            if node is None:
                print(f"{idx}: None")
                continue
            
            print(f"{idx}: {node.key}")
            current = node
            while current.next is not None:
                current = current.next
                print(f"{current.key}")
        
        print()