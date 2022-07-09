import sys
sys.path.append("..")

from profq_data.data.redblack_tree import RedBlackTree

import random


def test():
    for _ in range(100):
        pass
        # tree = RedBlackTree()

        # # ===== Data =====
        # data1 = random.randint(0, 100)
        # data2 = random.randint(0, 100)
        # data3 = random.randint(0, 100)
        # data4 = random.randint(0, 100)

        # while data2 == data1:
        #     data2 = random.randint(0, 100)
            
        # while data3 in [data1, data2]:
        #     data3 = random.randint(0, 100)

        # while data4 in [data1, data2, data3]:
        #     data4 = random.randint(0, 100)

        # # ===== Insert data1 =====
        # tree.insert(data1)
        # assert tree.contains(data1)
        # assert not tree.contains(data2)
        # assert not tree.contains(data3)
        # assert not tree.contains(data4)

        # assert tree.search(data1).data == data1
        # assert tree.search(data2) is None
        # assert tree.search(data3) is None
        # assert tree.search(data4) is None

        # assert tree.height == 1

        # # ===== Insert data2 =====
        # tree.insert(data2)
        # assert tree.contains(data1)
        # assert tree.contains(data2)
        # assert not tree.contains(data3)
        # assert not tree.contains(data4)

        # assert tree.search(data1).data == data1
        # assert tree.search(data2).data == data2
        # assert tree.search(data3) is None
        # assert tree.search(data4) is None

        # assert tree.height == 2
        
        # # ===== Delete data1 =====
        # tree.delete(data1)
        # assert not tree.contains(data1)
        # assert tree.contains(data2)
        # assert not tree.contains(data3)
        # assert not tree.contains(data4)

        # assert tree.search(data1) is None
        # assert tree.search(data2).data == data2
        # assert tree.search(data3) is None
        # assert tree.search(data4) is None

        # assert tree.height == 1

        # # ===== Insert data3 =====
        # tree.insert(data3)
        # assert not tree.contains(data1)
        # assert tree.contains(data2)
        # assert tree.contains(data3)
        # assert not tree.contains(data4)
        
        # assert tree.search(data1) is None
        # assert tree.search(data2).data == data2
        # assert tree.search(data3).data == data3
        # assert tree.search(data4) is None

        # assert tree.height == 2
        # print("Test insert data3 passed")

        # # ===== Insert data1 =====
        # tree.insert(data1)
        # assert tree.contains(data1)
        # assert tree.contains(data2)
        # assert tree.contains(data3)
        # assert not tree.contains(data4)
        
        # assert tree.search(data1).data == data1
        # assert tree.search(data2).data == data2
        # assert tree.search(data3).data == data3
        # assert tree.search(data4) is None

        # print(f"{data1 = }, {data2 = }, {data3 = }")

        # assert tree.height == 2
        # print("Test insert data1 passed")
        
        # # ===== Insert data4 =====
        # tree.insert(data4)
        # assert tree.contains(data1)
        # assert tree.contains(data2)
        # assert tree.contains(data3)
        # assert tree.contains(data4)
        
        # assert tree.search(data1).data == data1
        # assert tree.search(data2).data == data2
        # assert tree.search(data3).data == data3
        # assert tree.search(data4).data == data4

        # assert tree.height == 3
        # print("Test insert data4 passed")
