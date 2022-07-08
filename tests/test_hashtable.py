import sys
sys.path.append("..")

from profq_data.data.hashtable import HashTable

import random
import string

def test():
    for _ in range(100):
        table = HashTable()

        key1 = "".join(random.choices(string.ascii_letters, k=random.randint(2, 100)))
        key2 = "".join(random.choices(string.ascii_letters, k=random.randint(2, 100)))
        key3 = "".join(random.choices(string.ascii_letters, k=random.randint(2, 100)))
        key4 = "".join(random.choices(string.ascii_letters, k=random.randint(2, 100)))

        data1 = random.randint(-100, 100)
        data2 = random.randint(-100, 100)
        data3 = random.randint(-100, 100)
        data4 = random.randint(-100, 100)

        table.put(key1, data1)
        assert table.find(key1) == data1
        assert len(table) == 1

        table.put(key2, data2)
        assert table.find(key2) == data2
        assert len(table) == 2

        assert table.remove(key1) == data1
        assert len(table) == 1

        table.put(key3, data3)
        assert table.find(key3) == data3
        assert len(table) == 2

        table.put(key4, data4)
        assert table.find(key4) == data4
        assert len(table) == 3

        assert table.remove(key3) == data3
        assert len(table) == 2

        assert table.remove(key1) is None
        assert len(table) == 2

        assert table.remove(key2) == data2
        assert len(table) == 1

        assert table.remove(key4) == data4
        assert len(table) == 0

        assert table.find(key1) is None
        assert table.find(key2) is None
        assert table.find(key3) is None
        assert table.find(key4) is None

        table.put("a", 1)
        table.put("b", 2)

        assert table.find("a") == 1
        assert table.find("b") == 2
        
        assert table.remove("a") == 1
        assert table.find("a") is None
        assert table.find("b") == 2
        assert table.remove("b") == 2
        assert table.find("b") is None
