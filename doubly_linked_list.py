from hash_table import DoublyLinkedListNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key, value):
        new_node = DoublyLinkedListNode(key, value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def delete(self, key):
        node = self.find(key)
        if node is None:
            return False
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        return True
