"""a persistent linked list"""
from __future__ import annotations
from typing import Iterable, Any, final
from .ipersistent import IPersistent


@final
class ListNode:
    """This node class will be used with the persistent linked list.
    Added in version: 0.1.0
    """

    def __init__(self, value: Any, nextNode: ListNode = None) -> None:
        self.value = value
        self.next = nextNode

    def __eq__(self, node):
        return self.value == node.value


class Plist(IPersistent):
    """Persistent linked list with O(1) concatenation.

    Added in version: 0.1.0
    """

    def __init__(self, iterable: Iterable) -> None:
        self.head: ListNode = None
        self.tail: ListNode = None
        self.length: int = 0

        self._construct(iterable)

    def _construct(self, iterable: Iterable) -> None:
        """Construct linked list from iterable.
        
        Added in version: 0.1.0
        """

        # TODO refactor. ugly
        current = None
        for element in iterable:
            self.length += 1
            if not self.head:
                self.head = ListNode(element)
                current = self.head
            else:
                current.next = ListNode(element)

                current = current.next
        self.tail = current
    
    def _copy_self(self):

        """Added in version: 0.1.0"""
        pass
        

    def cons(self, value):
        """Added in version: 0.1.0"""
        new_plist = Plist([value])
        new_plist.head.next = self.head
        new_plist.tail = self.tail
        new_plist.length = self.length + 1

        return new_plist

    def conj(self, value):
        """Added in version: 0.1.0"""
        return self.cons(value)  # Conj and cons is same for link list

    def concat(self, value):
        """Added in version: 0.1.0"""
        # make new list, copy self's head new list
        new_plist = Plist([self.head.value])
        # sets self tail to point to new tail
        self.tail.next = ListNode(value)
        # Set the value of the new list's tail
        new_plist.tail = self.tail.next
        new_plist.length = self.length + 1
        return new_plist

    # def insert(self,index, value):
    #     new_plist=self.head
    #     new_plist.tail=self.tail

    

    def __iter__(self):
        """Added in version: 0.1.0"""
        current = self.head
        while current is not self.tail:
            yield current.value
            current = current.next
        yield current.value  # Tail's value

    def __repr__(self):
        """Added in version: 0.1.0"""
        # iteration yields the value of the Node
        # not the node object
        return f"Plist{[i for i in self]}"

    def __len__(self):
        """Added in version: 0.1.0"""
        return self.length
