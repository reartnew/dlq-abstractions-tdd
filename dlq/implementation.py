# -*- coding: utf-8 -*-

from . import abstract

__all__ = [
    "DLQ",
    "DLQItem",
]


class DLQ(abstract.AbstractDLQ):
    def __init__(self, value = None):
        abstract.AbstractDLQ.__init__(self, value)
        self.value = value
        self.next = None
        self.previous = None
        self.head = None
    def first(self):
        if self.previous is not None:
            self.value = self.previous
        return self.value
    def last(self):
        while self.next is not None:
            self.value = self.next
        return self.value
    def append(self, value):
        node = DLQItem(value)
        node.next = None
        if self.head is None:
            node.previous = None
            self.head = node
            return node
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = node
        node.previous = last
        return node
    def appendleft(self, value):
        node = DLQItem(value)
        node.next = self.head
        if self.head is not None:
            self.head.previous = node
        self.head = node
        return self.head
    def pop(self):
        pass
    def popleft(self):
        pass
    def __iter__(self):
        pass
    def __str__(self):
        print(self.value)

class DLQItem(abstract.AbstractDLQItem):
    @property
    def value(self):
        return self.value
    def next(self):
        return self.next
    def previous(self):
        return self.previous
        