class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedLIst:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head

        # Since it is prepend, we don't have to disturb the tail. We can just play with the head.
        temp_head = self.head

        self.head = Node(value)
        self.head.next = temp_head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        self.tail.next = Node(value)

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

    def search(self, search_value):
        if self.head is None:
            return None

        local_head = self.head

        while local_head:
            if local_head.value == search_value:
                return local_head

            local_head = local_head.next

        return None

    def remove(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        local_head = self.head

        while local_head.next:
            if local_head.next == value:
                local_head.next = local_head.next.next
                return

            local_head = local_head.next

    def pop(self, value):
        if self.head is None:
            return None

        return_value = self.head

        self.head = self.head.next

        return return_value

    def insert(self, location, value):
        if self.head is None:
            self.head = Node(value)
            return

        if location == 0:
            self.prepend(value)

        local_head = self.head
        current_position = 0

        while local_head.next:
            if current_position + 1 == location:
                temp_head = local_head.next
                local_head.next = Node(value)
                local_head.next.next = temp_head
                return

        local_head.next = Node(value)