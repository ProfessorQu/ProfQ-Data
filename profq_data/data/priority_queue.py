from profq_data.data.queue import Queue, Node

from typing import Callable

class PriorityQueue(Queue):
    """An implementation of the Priority Queue data structure
    """
    def __init__(self, sort_func: Callable = lambda x: x[1], reverse: bool = True) -> None:
        """The init function
        """
        self.data = []
        self.sort_func = sort_func
        self.reverse = reverse
    
    def enqueue(self, data: int, priority: int = 0):
        """Enqueue an item with data and priority

        Args:
            data (int): the data to add
            priority (int): the priority of the data
        """
        self.data.append((data, priority))
        self.sort()
    
    def dequeue(self):
        """Dequeue the highest priority item
        """
        return self.data.pop(0)[0]
    
    def sort(self):
        """Sort the queue
        """
        self.data.sort(key=self.sort_func, reverse=self.reverse)
    
    def is_empty(self) -> bool:
        return len(self.data) == 0
    
    def peek(self) -> int:
        return self.data[0][0]
