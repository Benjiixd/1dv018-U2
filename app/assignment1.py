# Fördelar med linked list över arraylist:
# Bättre tidskomplexitet för insättning och borttagning av element, O(1) kontra O(n).
# Dynamisk storlek, minnet används mer effektivt beroende på antalet element.
# Nackdelar med linked list över arraylist:
# sämre tidskomplexitet för att hitta element, eftersom den måste ta sig "fram" genom listan.
# Mer minnesanvändning på grund av lagring av pekare.

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.last = None

    def append(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node   
            self.last = new_node        


    def remove(self, key) -> None:
        current = self.head
        prev = None
        while current and current.data != key: # search for the key
            prev = current
            current = current.next
        if current is None: # key not found
            return
        if prev is None: # key is in the first node
            self.head = current.next
            if self.head is None: # list is now empty
                self.last = None
        else: # key is in a node other than the first
            prev.next = current.next
            if current == self.last: # key is in the last node
                self.last = prev
    
    def find(self, key) -> bool:
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def length(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("end")
