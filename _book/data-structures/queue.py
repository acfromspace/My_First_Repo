"""
@author: acfromspace
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def showcase(self):
        return self.items


queue = Queue()
print(queue.is_empty())
queue.enqueue('hello')
queue.enqueue('dog')
queue.enqueue(3)
print(queue.dequeue())
print(queue.showcase())
