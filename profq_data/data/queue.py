class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.node = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None
    
    def peek(self) -> int:
        return self.head.data
    
    def add(self, data: int):
        node = Node(data)
        if self.tail is not None:
            self.tail.next = node
        
        self.tail = node

        if self.head is None:
            self.head = node
    
    def remove(self):
        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        return data