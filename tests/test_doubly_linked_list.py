from os import link
import sys
sys.path.append("..")

from profq_data.data.doubly_linked_list import DoublyLinkedList

import random
import pytest

def test():
    for _ in range(100):
        linked_list = DoublyLinkedList()

        random1 = random.randint(-100, 100)
        random2 = random.randint(-100, 100)
        random3 = random.randint(-100, 100)

        while random2 == random1:
            random2 = random.randint(-100, 100)

        while random3 in [random1, random2]:
            random3 = random.randint(-100, 100)

        assert len(linked_list) == 0

        # ===== Test Push =====
        linked_list.push(random1)
        assert linked_list.peek() == random1
        assert len(linked_list) == 1

        assert linked_list.contains(random1)
        assert not linked_list.contains(random2)
        assert not linked_list.contains(random3)

        # ===== Test Push =====
        linked_list.push(random2)
        assert linked_list.peek() == random2
        assert len(linked_list) == 2

        assert linked_list.contains(random1)
        assert linked_list.contains(random2)
        assert not linked_list.contains(random3)

        # ===== Test Delete With Value =====
        linked_list.delete_with_value(random1)
        assert linked_list.peek() == random2
        assert len(linked_list) == 1

        assert not linked_list.contains(random1)
        assert linked_list.contains(random2)
        assert not linked_list.contains(random3)

        # ===== Test Push =====
        linked_list.push(random3)
        assert linked_list.peek() == random3
        assert len(linked_list) == 2

        assert not linked_list.contains(random1)
        assert linked_list.contains(random2)
        assert linked_list.contains(random3)

        # ===== Test Delete With Value =====
        linked_list.delete_with_value(random3)
        assert linked_list.peek() == random2
        assert len(linked_list) == 1

        assert not linked_list.contains(random1)
        assert linked_list.contains(random2)
        assert not linked_list.contains(random3)

        # ===== Test Delete At Index =====
        linked_list.delete_at_index(0)
        with pytest.raises(AttributeError):
            linked_list.peek()
        assert len(linked_list) == 0
