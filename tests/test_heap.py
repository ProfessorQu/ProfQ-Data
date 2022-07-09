import sys
sys.path.append("..")

from profq_data.data.heap import Heap
import random

def test():
    data1 = 1
    data2 = 2
    data3 = 3
    data4 = 4
    for _ in range(100):
        heap = Heap()

        # ===== Data =====

        # while data2 == data1:
        #     data2 = random.randint(0, 100)
        
        # while data3 in [data1, data2]:
        #     data3 = random.randint(0, 100)
        
        # while data4 in [data1, data2, data3]:
        #     data4 = random.randint(0, 100)
        
    # ===== Test functions =====
    heap.add(10)
    heap.add(15)
    heap.add(20)
    heap.add(17)
    
    assert heap.items == [10, 15, 20, 17]

    assert heap.peek() == 10
    assert heap.poll() == 10

    assert heap.peek() == 15
    
    assert heap.items == [15, 17, 20]

    heap.add(10)

    assert heap.items == [10, 15, 20, 17]

    heap.add(8)

    assert heap.items == [8, 10, 20, 17, 15]
