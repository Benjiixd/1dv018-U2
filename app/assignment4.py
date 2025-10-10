from assignment1 import LinkedList

class HashTable:
    def __init__(self, capacity=8) -> None:
        self.capacity = capacity
        self.table = [LinkedList() for _ in range(capacity)]
        self._n = 0
    
    def _hash(self, key) -> int:
        hv = 0
        for char in str(type(key)) + str(key):
            hv = (hv * 31 + ord(char)) % self.capacity
        return hv
    
    def put(self, key, value) -> None:
        idx = self._hash(key)
        bucket = self.table[idx]
        current = bucket.head
        while current:
            if current.data[0] == key:
                current.data = (key, value)
                return
            current = current.next
        bucket.append((key, value))
        self._n += 1

    def get(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        current = bucket.head
        while current:
            if current.data[0] == key:
                return current.data[1]
            current = current.next
        raise KeyError(f"Key {key} not found")
    
    def remove(self, key) -> None:
        idx = self._hash(key)
        bucket = self.table[idx]
        current = bucket.head
        while current:
            if current.data[0] == key:
                bucket.remove(current.data)
                self._n -= 1
                return
            current = current.next
        raise KeyError(f"Key {key} not found")
    
    def display(self) -> None:
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: ", end="")
            bucket.display()

    def collision_count(self):
        collisions = 0
        for bucket in self.table:
            current = bucket.head
            if current and current.next:
                while current.next:
                    collisions += 1
                    current = current.next
        return collisions
