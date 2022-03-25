from profq_data.helpers.nodes.hashtable_node import Node

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
        index = self.hash(key)

        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        return None if node is None else node.data

    