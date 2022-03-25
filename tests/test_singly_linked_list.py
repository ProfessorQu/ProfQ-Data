import sys
sys.path.append("..")

from profq_data.data.singly_linked_list import SinglyLinkedList

import random
import pytest

def test():
    for _ in range(100):
        linked_list = SinglyLinkedList()

        random1 = random.randint(-100, 100)
        random2 = random.randint(-100, 100)
        random3 = random.randint(-100, 100)

        assert len(linked_list) == 0

        linked_list.push(random1)
        assert linked_list.peek() == random1
        assert len(linked_list) == 1

        linked_list.push(random2)
        assert linked_list.peek() == random2
        assert len(linked_list) == 2

        linked_list.delete_with_value(random1)
        assert linked_list.peek() == random2
        assert len(linked_list) == 1

        linked_list.push(random3)
        assert linked_list.peek() == random3
        assert len(linked_list) == 2

        linked_list.delete_with_value(random3)
        assert linked_list.peek() == random2
        assert len(linked_list) == 1

        linked_list.delete_at_index(0)
        with pytest.raises(AttributeError):
            linked_list.peek()
        assert len(linked_list) == 0

test()
