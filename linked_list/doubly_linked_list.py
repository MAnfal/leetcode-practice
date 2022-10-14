class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        node = Node(value)

        node.previous = self.tail

        self.tail.next = node

        self.tail = self.tail.next

    def to_list(self):
        if self.head is None:
            return []

        _head = self.head
        _list = []

        while _head:
            _list.append(_head.value)
            _head = _head.next

        return _list
