# -*- coding: utf-8 -*-

from . import abstract
import typing as t

__all__ = [
    "DLQ",
    "DLQItem",
]

VT = t.TypeVar("VT")

class DLQ(abstract.AbstractDLQ):
    
    def __init__(self, initializer: t.Optional[t.Iterable[VT]] = None) -> None:
        super().__init__()
        self.head: t.Optional[DLQItem] = None
        if initializer is not None:
            prev_dlq_item: t.Optional[DLQItem] = None
            for value in initializer:
                item = DLQItem(value)
                if prev_dlq_item is None:
                    self.head = item
                else:
                    prev_dlq_item.next_item = item
                    item.previous_item = prev_dlq_item
                prev_dlq_item = item

    def first(self):
        current = self.head
        return current

    def last(self):
        curr: t.Optional[DLQItem] = self.head
        prev: t.Optional[DLQItem] = None
        while curr is not None:
            prev = curr
            curr = curr.next_item
        return prev

    def append(self, value):
        if self.head is None:
            node = DLQItem(value)
            node.previous_item = None
            self.head = node
        else:
            node = DLQItem(value)
            curr = self.head
            while curr.next_item is not None:
                curr = curr.next_item
            curr.next_item = node
            node.previous_item = curr
            node.next_item = None

    def appendleft(self, value):
        if self.head is None:
            node = DLQItem(value)
            node.previous_item = None
            self.head = node
        else:
            node = DLQItem(value)
            self.head.previous_item = node
            node.next_item = self.head
            self.head = node
            node.previous_item = None

    def pop(self):
            if self.head is None:
                raise KeyError
            curr = self.head
            while curr.next_item is not None:
                curr = curr.next_item
            last = curr
            new_last = curr.previous_item
            new_last.next_item = None
            last.previous_item = None
            return last.value

    def popleft(self):
        if self.head is None:
                raise KeyError
        curr = self.head
        first = curr
        new_first = curr.next_item
        new_first.previous_item = None
        first.next_item = None
        self.head = new_first
        return first.value

    def __eq__(self, new_list):
        return list(self) == list(new_list)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next_item

class DLQItem(abstract.AbstractDLQItem):
    def __init__(self, value: VT):
        self._value = value
        self.next_item = None
        self.previous_item = None

    @property
    def value(self):
        return self._value

    def next(self):
        return self.next_item

    def previous(self):
        return self.previous_item
        