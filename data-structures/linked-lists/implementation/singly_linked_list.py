"""A small, reusable singly linked list implementation for learning."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    next: Optional["Node[T]"] = None


class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def is_empty(self) -> bool:
        return self.head is None

    def prepend(self, value: T) -> None:
        node = Node(value, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1

    def append(self, value: T) -> None:
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def find(self, value: T) -> Optional[Node[T]]:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete_first(self, value: T) -> bool:
        previous: Optional[Node[T]] = None
        current = self.head
        while current is not None and current.value != value:
            previous, current = current, current.next
        if current is None:
            return False
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        if self.tail is current:
            self.tail = previous
        self._size -= 1
        return True

    def reverse(self) -> None:
        previous: Optional[Node[T]] = None
        current = self.head
        self.tail = self.head
        while current is not None:
            following = current.next
            current.next = previous
            previous, current = current, following
        self.head = previous


if __name__ == "__main__":
    items = SinglyLinkedList[int]()
    for number in (10, 20, 30):
        items.append(number)
    items.prepend(5)
    print(list(items))          # [5, 10, 20, 30]
    items.reverse()
    print(list(items))          # [30, 20, 10, 5]
    items.delete_first(20)
    print(list(items))          # [30, 10, 5]
