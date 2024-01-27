class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def check_collision(self, index):
        return self.buckets[index] is not None

    def add_to_linked_list(self, index, key, value):
        new_node = HashNode(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.check_collision(index):
            node = self.buckets[index]
            while node:
                if node.key == key:
                    node.value = value  # Update existing key
                    return
                node = node.next
        self.add_to_linked_list(index, key, value)

    def delete(self, key):
        index = self.hash_function(key)
        node = self.buckets[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[index] = node.next
                return
            prev = node
            node = node.next

    def get(self, key):
        index = self.hash_function(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

# Example Usage
htable = HashTable()
htable.insert("name", "John")
htable.insert("age", 25)
htable.insert("city", "New York")

print(htable.get("name"))  # Output: John
print(htable.get("age"))   # Output: 25
print(htable.get("city"))  # Output: New York

htable.delete("name")
print(htable.get("name"))  # Output: None
