import sys
sys.path.append("..")

from profq_data.data.queue import Queue
import random

def test():
    for _ in range(100):
        queue = Queue()

        assert queue.is_empty()

        random_item1 = random.randint(-100, 100)

        queue.enqueue(random_item1)

        assert not queue.is_empty()

        assert queue.head.data == random_item1
        assert queue.peek() == random_item1
        assert queue.tail.data == random_item1

        random_item2 = random.randint(-100, 100)

        queue.enqueue(random_item2)

        assert not queue.is_empty()

        assert queue.head.data == random_item1
        assert queue.peek() == random_item1
        assert queue.tail.data == random_item2

        assert queue.dequeue() == random_item1
        assert queue.dequeue() == random_item2
        assert queue.is_empty()

    