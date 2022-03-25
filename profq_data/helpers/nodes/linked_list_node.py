class Node:
    """A class for most data structures
    """
    def __init__(self, data: int) -> None:
        """The init function

        Args:
            data (int): what data to put in the node
        """
        self.data = data
        self.next = None
        self.prev = None