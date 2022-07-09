import sys
sys.path.append("..")

from profq_data.data.queue import Queue
import random

def test():
    for _ in range(100):
        queue = Queue()

        assert queue.is_empty()

        # ===== Test Enqueue =====
        data1 = random.randint(-100, 100)

        queue.enqueue(data1)

        assert not queue.is_empty()

        assert queue.head.data == data1
        assert queue.peek() == data1
        assert queue.tail.data == data1

        # ===== Test Enqueue =====
        data2 = random.randint(-100, 100)

        queue.enqueue(data2)

        assert not queue.is_empty()

        assert queue.head.data == data1
        assert queue.peek() == data1
        assert queue.tail.data == data2

        # ===== Test Dequeue =====
        assert queue.dequeue() == data1
        assert queue.dequeue() == data2
        assert queue.is_empty()

    