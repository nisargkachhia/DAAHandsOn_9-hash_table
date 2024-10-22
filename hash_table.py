class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class HashTable:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash_function(self, key):
        # Multiplication and division hash method
        A = 0.6180339887  # constant (fractional part of sqrt(5)-1/2)
        return int(self.capacity * ((key * A) % 1))

    def resize(self, new_capacity):
        old_table = self.table
        self.capacity = new_capacity
        self.size = 0
        self.table = [None] * self.capacity
        for chain in old_table:
            if chain:
                current = chain.head
                while current:
                    self.insert(current.key, current.value)
                    current = current.next

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            from doubly_linked_list import DoublyLinkedList
            self.table[index] = DoublyLinkedList()
        chain = self.table[index]
        node = chain.find(key)
        if node:
            node.value = value
        else:
            chain.insert(key, value)
            self.size += 1

        if self.size == self.capacity:
            self.resize(self.capacity * 2)

    def find(self, key):
        index = self.hash_function(key)
        chain = self.table[index]
        if chain is None:
            return None
        node = chain.find(key)
        return node.value if node else None

    def delete(self, key):
        index = self.hash_function(key)
        chain = self.table[index]
        if chain is None:
            return False
        removed = chain.delete(key)
        if removed:
            self.size -= 1

        if self.size > 0 and self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)

        return removed