# -*- coding: utf-8 -*-

from . import abstract
import typing as t

__all__ = [
    "DLQ",
    "DLQItem",
]

VT = t.TypeVar("VT")

class DLQ(abstract.AbstractDLQ):
    def __init__(self, value = None):
        #abstract.AbstractDLQ.__init__(self, value)
        '''i = isinstance(value, list)
        if i is True:
            for n in value:
                self.head = DLQItem(n)
                #print(self.head.value)
                self.head = self.head.next'''
                #print("x")
            #print(i)
        #else:
        self.head = DLQItem(value)
    def first(self):
        '''if self.previous is not None:
            self.value = self.previous'''
        #self.next.value = 2
        current = self.head
        print("first is:",current.value)
        return current
    def last(self):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        print("Last item is ",curr.value)
        return curr
    def append(self, value):
        #node = DLQItem(value)
        #node.next = None
        if self.head is None:
            node = DLQItem(value)
            node.previous = None
            self.head = node
            #return
        else:
            node = DLQItem(value)
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            node.previous = curr
            node.next = None
            #return
    def appendleft(self, value):
        if self.head is None:
            node = DLQItem(value)
            node.previous = None
            self.head = node
        else:
            node = DLQItem(value)
            self.head.previous = node
            node.next = self.head
            self.head = node
            node.previous = None
    def pop(self):
            #try:
            if self.head is None:
                print("Error1")
                raise Error("KeyError on emptiness")
            else:
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                last = curr # last element in a list
                new_last = curr.previous
                print("new last value", new_last.next.value)
                new_last.next = None
                last.previous = None
                self.head.previous = new_last
                return last
            #except Exception as ex:
            #    print("Error")
    def popleft(self):
        if self.head is None:
                print("Error1")
                raise Error("KeyError on emptiness")
        else:
            curr = self.head
            first = curr # first element in a list
            new_first = curr.next
            new_first.previous = None
            first.next = None
            #self.head.next = new_first
            self.head = new_first
            print("New first value:", new_first.value)
            return first
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next
    def print_list(self):
        curr = self.head
        print("List:")
        while curr is not None:
            print(curr.value)
            curr = curr.next

class DLQItem(abstract.AbstractDLQItem):
    def __init__(self, value: VT):
        self._value = value
        self.next = None
        self.previous = None
    @property
    def value(self):
        return self._value
    def next(self):
        return self.next
    def previous(self):
        return self.previous
        
dllist = DLQ(1)
dllist.append(2)
dllist.first()
dllist.last()
dllist.appendleft(0)
#dllist.first()
dllist.append(3)
dllist.last()
dllist.print_list()
dllist.pop()
dllist.print_list()
dllist.popleft()
dllist.print_list()