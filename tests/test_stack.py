import sys
sys.path.append("..")

from profq_data.data.stack import Stack
import random

def test():
    for _ in range(100):
        stack = Stack()
        assert stack.is_empty()

        # ===== Test Push =====
        random_item1 = random.randint(-100, 100)

        stack.push(random_item1)

        assert not stack.is_empty()

        assert stack.top.data == random_item1
        assert stack.peek() == random_item1

        # ===== Test Push =====
        random_item2 = random.randint(-100, 100)

        stack.push(random_item2)

        assert not stack.is_empty()

        assert stack.top.data == random_item2
        assert stack.peek() == random_item2

        # ===== Test Pop =====
        assert stack.pop() == random_item2
        assert stack.pop() == random_item1
        assert stack.is_empty()

    