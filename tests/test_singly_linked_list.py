import sys
sys.path.append("..")

from profq_data.data.singly_linked_list import SinglyLinkedList
import random

def test():
    for _ in range(100):
        linked_list = SinglyLinkedList()

        linked_list.append