
class InorderIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        value = node.data
        self._push_left(node.right)
        return value

class PreorderIterator:
    def __init__(self, root):
        self.stack = []
        if root:
            self.stack.append(root)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        value = node.data
        if node.right:
            self.stack.append(node.right)
        if node.left:
            self.stack.append(node.left)
        return value

class PostorderIterator:
    def __init__(self, root):
        self.stack1 = []
        self.stack2 = []
        if root:
            self.stack1.append(root)
            while self.stack1:
                node = self.stack1.pop()
                self.stack2.append(node)
                if node.left:
                    self.stack1.append(node.left)
                if node.right:
                    self.stack1.append(node.right)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.stack2:
            raise StopIteration
        node = self.stack2.pop()
        return node.data


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
        self._n = 0 # to keep track of number of nodes faster
    
    def size(self) -> int:
        return self._n

    def isEmpty(self) -> bool:
        return self.root is None
    
    def add(self, data) -> None:
        new_node = Node(data)
        if self.isEmpty():
            self.root = new_node
            self._n += 1
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    self._n += 1
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    self._n += 1
                    return
                current = current.right
            else:
                # data already exists, do not add duplicates
                return
            
    def get_successor(self, node):
        cur = node.right
        while cur.left is not None:
            cur = cur.left
        return cur
    
    def remove_rec(self, node, data):
        if node is None:
            return None, False

        if data < node.data:
            node.left, removed = self.remove_rec(node.left, data)
            return node, removed
        elif data > node.data:
            node.right, removed = self.remove_rec(node.right, data)
            return node, removed
        else:
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True
            
            succ = self.get_successor(node)
            node.data = succ.data
            node.right, _ = self.remove_rec(node.right, succ.data)
            return node, True
            
    def remove(self, data) -> None:
        self.root, removed = self.remove_rec(self.root, data)
        if removed:
            self._n -= 1
        else:
            raise KeyError("value not found")
        
    def size(self):
        return self._n
    
    def _height(self, node):
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height, right_height)
    
    def height (self):
        return self._height(self.root)

    def contains (self, data) -> bool:
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
        return False
    
    def __iter__(self):
        return InorderIterator(self.root)
    
    def inorder(self):
        return InorderIterator(self.root)
    
    def preorder(self):
        return PreorderIterator(self.root)
    
    def postorder(self):
        return PostorderIterator(self.root)
    

            
    def __str__(self):
        lines = []
        def _print(node, level=0):
            if node is not None:
                _print(node.right, level + 1)
                lines.append("    " * level + f"{node.data}")
                _print(node.left, level + 1)
        _print(self.root)
        return "\n".join(lines)  
               
    def removeKLargest(self, k):
        if k <= 0 or k > self.size():
            raise ValueError("k is out of bounds")
        if self.isEmpty():
            raise IndexError("Tree is empty")
        if k is None:
            raise ValueError("k cannot be None")
        values = list(self)
        self.remove(values[-k])
