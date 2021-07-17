"""a persistent linked list"""
from __future__ import annotations
from typing import Iterable, Any, final
from .ipersistent import IPersistent


@final
class ListNode:
    """This node class to be used with persistent linked list.
    Added in version: 0.1.0
    """

    def __init__(self, value: Any, nextNode: ListNode = None) -> None:
        self.value = value
        self.next = nextNode


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
        """Construct linked list from iterable."""

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

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self):
        return self.length