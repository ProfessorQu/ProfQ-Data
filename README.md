# ProfQ-Data

## Usage

You can import the module like any other with:

```python
import profq_data
```

Then you have access to all kinds of [data structures](<#data-structures>).

For example, a [queue](#queue):

```python
from profq_sorting import Queue

queue = Queue()

queue.enqueue(1)
queue.enqueue(3)

print(queue.dequeue())
```

```none
Output: 1
```

There are many more data structures which I have implemented, but here is a few that may interest you: `queue`, `stack`, `binary tree` and `linked list`.

## Data Structures

### Binary Tree

```python
from profq_sorting import BinaryTree
```

A binary tree is a data structure in which you can input numbers and it will put them at a certain spot. Every node has a right child and a left child, the idea is that every node that is smaller than the parent, will be on the left and every nod that's bigger, on the right. This implementation has no balancing, so it can be quite ineffecient.

### Hash Table

```python
from profq_sorting import HashTable
```

This data structure uses a hashing function to determine an index in where it should put an item in an array. If the index is the same, however, it will take the node that is already inside the index and add a reference, basically creating a [linked list](#linked-list) in that spot.

### Heap

```python
from profq_sorting import Heap
```

A heap is kind of like a [binary tree](#binary-tree), in that it has a tree-like architecture. It is implemented however with an array. It uses some formulas to see what items are parents and children of each other. Also, it ensures that the minimum element is always on top, and when an item gets added, the tree is always filled left to right.

### Queue

```python
from profq_sorting import Queue
```

Queue is a simple data structure, it's almost identical to an actual queue except it's with data in a computer instead of with people. It works according to FIFO (First In First Out), the acronym says it all really. The items that are added first will exit first, like a queue to see a movie. They don't let the people in the back of the line in first, they let the people on the front in first. The data structure is also very similar to a [linked list](#linked-list).

### Priority Queue

```python
from profq_sorting import PriorityQueue
```

A priority queue is the same as a [queue](#queue), instead it just has a priority, every item has a priority and items with the highest priority are the first to go out. My implementation lets you have control over what the priority is decided by.

### Stack

```python
from profq_sorting import Stack
```

Basically the opposite of a [queue](#queue). It uses the principle LIFO (Last In First Out), and again it says it all. You can imagine a "stack" (see what I did there?) of pancakes. You don't take the bottom one (FIFO), you take the top one (LIFO). This one is also based on the linked list.

### Linked List

```python
from profq_sorting import SinglyLinkedList
```

A the famed linked list, I've talked about it so much because many other data structures use this or the principles of this. It starts with one node, the head, and that node links to another node, that one links to the next and so on and so forth, until you reach the end of the list. This means that, unlike arrays, you can't access every element instantly, you first have to traverse the list. That's a big negative, BUT it can be any length. And maybe Python isn't the greatest programming language to have that in. In other programming languages it can be very easy to make dynamically sized lists.

You may have also noticed the class not being called `LinkedList` but instead `SinglyLinkedList`. That's because there are many other linked lists including one [doubly linked list](#doubly-linked-list) and one [skip list](#skip-list).

### Doubly Linked List

```python
from profq_sorting import DoublyLinkedList
```

A doubly linked list is the same as a singly linked list except that it has another reference, namely the previous node, meaning you can traverse it both ways. This can be extremely helpful for the history of web pages, because you can go forward AND backward, which you can't do with a normal linked list.

### Skip List

```python
from profq_sorting import SkipList
```

A skip list is the same as a linked list except it has one "express lane" or another linked list. When it wants to insert a node, it uses the express lane to find the node that is before a node that is higher that the one you want to insert and then it traverses the normal linked list. Then it flips a coin to decide whether to add this node to the express lane. Deletion is the same, only it also has to delete the node in the express lane.

## Conclusion

I made this package to learn more about data structures and their uses plus now I can say I've published **MULTIPLE** Python packages (just 2, but still). And I like this way of doing it, because I hope it can help someone who is looking for some implementation of data structures and that they can find this.

I used this [playlist](https://www.youtube.com/playlist?list=PLI1t_8YX-Apv-UiRlnZwqqrRT8D1RhriX) from [HackerRank](https://www.youtube.com/c/HackerrankOfficial) a lot, it's really helpful!

[GeeksForGeeks](https://www.youtube.com/c/GeeksforGeeksVideos) also has a lot of videos about data structures (and I mean a LOT).

It has been really fun learning about all these data structures and I highly encourage you to try and implement some for yourself and see where you can use this in your current/future job!
