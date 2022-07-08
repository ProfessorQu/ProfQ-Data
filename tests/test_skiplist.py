import sys
sys.path.append("..")

from profq_data.data.skiplist import SkipList

import random
import pytest


def test():
    for _ in range(100):
        skiplist = SkipList()

        random1 = random.randint(-100, 0)
        random2 = random.randint(random1 + 1, 100)
        random3 = random.randint(random2 + 1, 200)

        while random2 == random1:
            random2 = random.randint(random1 + 1, 100)

        while random3 in [random1, random2]:
            random3 = random.randint(random2 + 1, 200)

        assert len(skiplist) == 0

        # ===== Test Insert =====
        skiplist.insert(random1)
        assert skiplist.peek() == random1
        assert len(skiplist) == 1

        assert skiplist.contains(random1)
        assert not skiplist.contains(random2)
        assert not skiplist.contains(random3)

        # ===== Test Push =====
        skiplist.insert(random2)
        assert skiplist.peek() == random1
        assert len(skiplist) == 2

        assert skiplist.contains(random1)
        assert skiplist.contains(random2)
        assert not skiplist.contains(random3)

        # ===== Test Delete With Value =====
        skiplist.delete_with_value(random1)
        assert skiplist.peek() == random2
        assert len(skiplist) == 1

        assert not skiplist.contains(random1)
        assert skiplist.contains(random2)
        assert not skiplist.contains(random3)

        # ===== Test Insert =====
        skiplist.insert(random3)
        assert skiplist.peek() == random2
        assert len(skiplist) == 2

        assert not skiplist.contains(random1)
        assert skiplist.contains(random2)
        assert skiplist.contains(random3)

        # ===== Test Delete With Value =====
        skiplist.delete_with_value(random3)
        assert skiplist.peek() == random2
        assert len(skiplist) == 1

        assert not skiplist.contains(random1)
        assert skiplist.contains(random2)
        assert not skiplist.contains(random3)

        # ===== Test Delete At Index =====
        skiplist.delete_at_index(0)
        with pytest.raises(AttributeError):
            skiplist.peek()
        assert len(skiplist) == 0
