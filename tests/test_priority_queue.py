import sys
sys.path.append("..")

from profq_data.data.priority_queue import PriorityQueue
import random

def test():
    for _ in range(100):
        queue = PriorityQueue()

        assert queue.is_empty()

        # ===== Test Enqueue =====
        data1 = random.randint(-100, 100)
        queue.enqueue(data1, 0)

        assert not queue.is_empty()

        assert queue.peek() == data1

        # ===== Test Enqueue =====
        data2 = random.randint(-100, 100)
        queue.enqueue(data2, 1)

        assert not queue.is_empty()

        assert queue.peek() == data2

        # ===== Test Dequeue =====
        assert queue.dequeue() == data2
        assert queue.dequeue() == data1
        assert queue.is_empty()

    for _ in range(100):
        queue = PriorityQueue(lambda node: node[0] > 0.5, True)

        assert queue.is_empty()

        # ===== Test Enqueue =====
        data1 = random.random()
        queue.enqueue(data1)

        assert not queue.is_empty()

        assert queue.peek() == data1

        # ===== Test Enqueue =====
        data2 = random.random()
        queue.enqueue(data2)

        assert not queue.is_empty()

        if (
            (data1 > 0.5 and data2 > 0.5) or
            (data2 <= 0.5 and data1 > 0.5) or
            (data2 <= 0.5)
        ):
            assert queue.peek() == data1
        else:
            assert queue.peek() == data2

        # ===== Test Dequeue =====
        if data1 > 0.5:
            assert queue.dequeue() == data1
        if data2 > 0.5:
            assert queue.dequeue() == data2

        if data1 > 0.5 and data2 > 0.5:
            assert queue.is_empty()
        if data2 > 0.5 and data1 <= 0.5:
            assert queue.dequeue() == data1
        if data1 > 0.5 and data2 <= 0.5:
            assert queue.dequeue() == data2
        
        if data1 <= 0.5 and data2 <= 0.5:
            assert queue.dequeue() == data1
            assert queue.dequeue() == data2

        assert queue.is_empty()
