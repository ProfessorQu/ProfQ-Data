class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def is_empty(self):
        return self.top is None
    
    def peek(self):
        return self.top.data
    
    def push(self, data: int):
        node = Node(data)

        node.next = self.top
        self.top = node
    
    def pop(self):
        data = self.top.data
        self.top = self.top.next

        return data