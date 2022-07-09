from profq_data.helpers.heap_calculator import HeapCalculator


class Heap:
    """An implementation of a heap
    """
    def __init__(self) -> None:
        """The init function
        """
        # Create a new heap
        self.items = []

        # Create a new heap calculator
        self.calc = HeapCalculator(self)
    
    def __len__(self) -> int:
        """Get the length of the heap

        Returns:
            int: the length of the heap
        """
        return len(self.items)
    
    def __getitem__(self, index: int) -> int:
        """Get an item at a specific index

        Args:
            index (int): the index of the item

        Returns:
            int: the item at the index
        """
        return self.items[index]
    
    def swap(self, index1: int, index2: int) -> None:
        """Swap two items

        Args:
            index1 (int): the index of item 1 to swap
            index2 (int): the index of item 2 to swap
        """
        # Swap the items
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]
    
    def peek(self) -> int:
        """Get the top item of the heap

        Raises:
            IndexError: if the heap is empty

        Returns:
            int: the top item of the heap
        """
        # Raise an error if the heap is empty
        if len(self) == 0:
            raise IndexError("Heap is empty")

        # Return the top item
        return self.items[0]
    
    def poll(self) -> int:
        """Remove the top item of the heap

        Raises:
            IndexError: if the heap is empty

        Returns:
            int: the top item of the heap
        """
        # Raise an error if the heap is empty
        if len(self) == 0:
            raise IndexError("Heap is empty")
        
        # Get the top item
        item = self.items[0]
        # Set the last item to the top item
        self.items[0] = self.items[-1]
        # Remove the last item
        self.items.pop()
        # Heapify down the heap
        self.heapify_down()

        # Return the top item
        return item
    
    def add(self, item: int) -> None:
        """Add an item to the heap

        Args:
            item (int): the item to add
        """
        # Add the item to the end of the heap
        self.items.append(item)
        # Heapify up the heap
        self.heapify_up()
    
    def heapify_up(self) -> None:
        """Heapify up the heap
        """
        index = len(self) - 1

        # As long as there is a parent and the parent is smaller than the child
        while self.calc.has_parent(index) and self.calc.get_parent(index) > self[index]:
            # Swap the parent and child
            self.swap(self.calc.get_parent_index(index), index)
            # Update the index
            index = self.calc.get_parent_index(index)

    def heapify_down(self) -> None:
        """Heapify down the heap
        """
        index = 0

        # As long as there is a left child
        while self.calc.has_left_child(index):
            # Get the left child index
            smaller_child_index = self.calc.get_left_child_index(index)
            # If there is a right child and the right child is smaller than the left child
            if self.calc.has_right_child(index) and self.calc.get_right_child(index) < self[smaller_child_index]:
                smaller_child_index = self.calc.get_right_child_index(index)
            
            # No need to swap if the parent is already smaller than the child
            if self.items[index] < self.items[smaller_child_index]:
                break
            
            # Swap the parent with the smallest child
            self.swap(index, smaller_child_index)
            # Update the index
            index = smaller_child_index

