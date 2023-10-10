from collections import deque
from heapq import heappop, heappush, heapify
from typing import Optional


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.heap = list()
        self.data = dict()

    def get(self, key: int) -> int:
        if key in self.data:
            value_list = self.data[key]
            value_list[0] += 1
            heapify(self.heap)
            return value_list[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.heap) == self.capacity:
            old_key = heappop(self.heap)[1]
            self.data.pop(old_key)

        value_list = [0, value]
        self.data[key] = value_list
        heappush(self.heap, value_list)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.heap = list()
        self.data = dict()

    def get(self, key: int) -> int:
        if key in self.data:
            value_list = self.data[key]
            value_list[0] += 1
            heapify(self.heap)
            return value_list[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.heap) == self.capacity:
            old_key = heappop(self.heap)[1]
            self.data.pop(old_key)

        value_list = [0, value]
        self.data[key] = value_list
        heappush(self.heap, value_list)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length = 0

    def is_empty(self):
        if not self.head and not self.tail:
            return True
        return False

    def insert_head(self, node: Node):
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head.previous = node
            node.next = self.head
            self.head = node
            self.head.previous = None
        self.length += 1

    def insert_tail(self, node: Node):
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.tail.next = None
        self.length += 1

    def delete_node(self, node: Node):
        if node == self.head and node == self.tail:
            self.tail = None
            self.head = None
        elif node == self.head:
            new_head = node.next
            new_head.previous = None
            self.head = new_head
        elif node == self.tail:
            new_tail = node.previous
            new_tail.next = None
            self.tail = new_tail
        else:
            next = node.next
            previous = node.previous
            previous.next = next
            next.previous = previous

        self.length -= 1

    def pop_tail(self) -> Node:
        if self.tail == self.head:
            node = self.tail
            self.tail = None
            self.head = None
        else:
            node = self.tail
            if node:
                self.tail = node.previous
            if self.tail:
                self.tail.next = None
        self.length -= 1
        return node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list_ = DoubleLinkedList()
        self.data = dict()

    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key][1]
            self.list_.delete_node(node)
            self.list_.insert_head(node)
            return self.data[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key not in self.data:
            if self.list_.length == self.capacity:
                node = self.list_.pop_tail()
                if node:
                    self.data.pop(node.value)
            node = Node(key)
            self.data[key] = [value, node]
            self.list_.insert_head(node)
        else:
            node = self.data[key][1]
            self.data[key][0] = value
            self.list_.delete_node(node)
            self.list_.insert_head(node)


if __name__ == '__main__':
    l = LRUCache(2)
    # l.put(1, 1)
    # l.put(2, 2)
    # print(l.get(1))
    # l.put(3, 3)
    # print(l.get(2))
    # l.put(4, 4)
    # print(l.get(1))
    # print(l.get(3))
    # print(l.get(4))

    # l.put(1, 0)
    # l.put(2, 2)
    # print(l.get(1))
    # l.put(3, 3)
    # print(l.get(2))

    l = LRUCache(1)
    print(l.get(6))
    print(l.get(8))
    l.put(12, 1)
    print(l.get(2))
    l.put(15, 11)
    l.put(5, 2)
    l.put(1, 15)
    l.put(4, 2)
    print(l.get(5))
    l.put(15, 15)
