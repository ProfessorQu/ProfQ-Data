import sys
sys.path.append("..")

from profq_data.data.heap import Heap
import random

def test():
    heap = Heap()

    # ===== Test Add =====
    heap.add(10)
    heap.add(15)
    heap.add(20)
    heap.add(17)
    
    assert heap.items == [10, 15, 20, 17]
    assert heap.peek() == 10

    # ===== Test Poll =====
    assert heap.poll() == 10
    assert heap.peek() == 15
    assert heap.items == [15, 17, 20]

    # ===== Test Add =====
    heap.add(10)
    assert heap.items == [10, 15, 20, 17]

    # ===== Test Add =====
    heap.add(8)
    assert heap.items == [8, 10, 20, 17, 15]
