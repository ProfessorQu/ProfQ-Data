from os import link
import sys
sys.path.append("..")

from profq_data.data.hashtable import HashTable

import random
import string

def test():
    for _ in range(100):
        table = HashTable()

        key1 = [random.choice(string.ascii_letters) for _ in range(random.randint(2, 100))]
        key2 = [random.choice(string.ascii_letters) for _ in range(random.randint(2, 100))]

        data1 = random.randint(-100, 100)
        data2 = random.randint(-100, 100)

        table.insert(key1, data1)

        assert table.find(key1) == data1

        table.insert(key2, data2)
        assert table.find(key2) == data2
        
