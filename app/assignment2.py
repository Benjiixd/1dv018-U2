class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
class DequeIterator:
    def __init__(self, first) -> None:
        self.current = first
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data
    
class Deque:
    def __init__(self) -> None:
        self.first = None
        self.last = None
    
    def isEmpty(self) -> bool:
        return self.first is None
    
    def addFirst(self, data) -> None:
        new_node = Node(data)
        if self.isEmpty():
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node
    
    def addLast(self, data) -> None:
        new_node = Node(data)
        if self.isEmpty():
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
    
    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("deque is empty")
        if self.first == self.last:
            removed = self.first
            self.first = None
            self.last = None
            removed.next = None # to help garbage collection
            removed.prev = None
            return removed
        else:
            removed = self.first
            self.first = self.first.next
            self.first.prev = None
            removed.next = None
            removed.prev = None # to help garbage collection
            return removed
        
    
    def removeLast(self) -> None:
        if self.isEmpty():
            raise IndexError("deque is empty")
        if self.first == self.last:
            removed = self.last
            self.first = None
            self.last = None
            removed.next = None # to help garbage collection
            removed.prev = None
            return removed
        else:
            removed = self.last
            self.last = self.last.prev
            self.last.next = None
            removed.next = None # to help garbage collection
            removed.prev = None
            return removed
    
    def size(self) -> int:
        count = 0
        current = self.first
        while current:
            count += 1
            current = current.next
        return count
    
    def display(self) -> None:
        current = self.first
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("end")
    
    def __iter__(self):
        return DequeIterator(self.first)

    

