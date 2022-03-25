class Node:
    """A class for most data structures
    """
    def __init__(self, key: str, data: int) -> None:
        """The init function

        Args:
            data (int): what data to put in the node
        """
        self.key = key
        self.data = data
        self.next = None
