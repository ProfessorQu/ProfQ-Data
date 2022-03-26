from os import link
import sys
from typing_extensions import dataclass_transform
sys.path.append("..")

from profq_data.data.hashtable import HashTable

import random
import string

def test():
    for _ in range(100):
        table = HashTable()

        key1 = [random.choice(string.ascii_letters) for _ in range(random.randint(2, 100))]
        key2 = [random.choice(string.ascii_letters) for _ in range(random.randint(2, 100))]
        key3 = [random.choice(string.ascii_letters) for _ in range(random.randint(2, 100))]
        key4 = [random.choice(string.ascii_letters) for _ in range(random.randint(2, 100))]

        data1 = random.randint(-100, 100)
        data2 = random.randint(-100, 100)
        data3 = random.randint(-100, 100)
        data4 = random.randint(-100, 100)

        table.insert(key1, data1)
        assert table.find(key1) == data1
        assert len(table) == 1

        table.insert(key2, data2)
        assert table.find(key2) == data2
        assert len(table) == 2

        assert table.remove(key1) == data1
        assert len(table) == 1

        table.insert(key3, data3)
        assert table.find(key3) == data3
        assert len(table) == 2

        table.insert(key4, data4)
        assert table.find(key4) == data4
        assert len(table) == 3

        assert table.remove(key3) == data3
        assert len(table) == 2
        
        assert table.remove(key1)
        assert len(table) == 2
        
