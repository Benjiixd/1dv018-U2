def main() -> None:
    from assignment1 import LinkedList
    from assignment2 import Deque
    from assignment3 import BST
    from assignment4 import HashTable

    # assignment 1 test
    print("___Assignment 1 Test___")
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.display()
    print("Length:", ll.length())
    ll.remove(20)
    ll.remove(21)
    ll.display()
    print("Length:", ll.length())

    print("___Assignment 2 Test___")
    dq = Deque()
    dq.addFirst(10)
    dq.addLast(20)
    dq.display()
    dq.addFirst(5)
    dq.addLast(25)
    dq.display()
    dq.addFirst(1)
    dq.display()
    print("Size:", dq.size())
    dq.removeFirst()
    dq.display()
    dq.removeLast()
    dq.display()
    print("Size:", dq.size())
    print("Iterating over deque:")
    for value in dq:
        print(value)
    dq2 = Deque()
    print("Is dq2 empty?", dq2.isEmpty())
    try:
        dq2.removeFirst()
    except IndexError as e:
        print("Expected exception on removing empty:", e)    
    
    print("\n___Assignment 3 Test (BST)")
    bst = BST()
    for x in [ 5, 3, 7, 2, 4, 6, 8, 9]:
        bst.add(x)

    print("Initial tree:")
    print(bst)
    print("InorderIterator:", list(bst))
    print("preorder:", list(bst.preorder()))
    print("postorder:", list(bst.postorder()))
    print("Size:", bst.size())
    print("Height:", bst.height())
    print("Contains 4?", bst.contains(4))
    print("Contains 11?", bst.contains(11))

    bst.remove(2)
    print("\nRemoving leaf 2:")
    print("Inorder:", list(bst))
    print("preorder:", list(bst.preorder()))
    print("postorder:", list(bst.postorder()))
    print("Size:", bst.size(), "Height:", bst.height())
    print(bst)

    bst.removeKLargest(2)
    print("\nRemoving leaf 8 (second largest):")
    print("Inorder:", list(bst))
    print("preorder:", list(bst.preorder()))
    print("postorder:", list(bst.postorder()))
    print(bst)

    bst.remove(7)
    print("Removing node 7:")
    print("Inorder:", list(bst))
    print("preorder:", list(bst.preorder()))
    print("postorder:", list(bst.postorder()))
    print("Size:", bst.size(), "Height:", bst.height())
    print(bst)

    bst.remove(5)
    print("\nRemoving node 5:")
    print("Inorder:", list(bst))
    print("preorder:", list(bst.preorder()))
    print("postorder:", list(bst.postorder()))
    print("Size:", bst.size(), "Height:", bst.height())
    print(bst)

    try:
        bst.remove(999)
    except KeyError as e:
        print("Expected exception on remove(999):", e)

    print("\n___Assignment 4 Test (HashTable)___")
    ht = HashTable()
    ht.put("apple", 10)
    ht.put("banana", 20)
    ht.put("orange", 30)
    ht.put("apple1", "one")
    ht.put("banana2", "two")
    ht.put("orange3", "three")
    print("Get apple:", ht.get("apple"))
    print("Get banana:", ht.get("banana"))
    print("Get orange:", ht.get("orange"))
    print("Get apple1:", ht.get("apple1"))
    print("Get banana2:", ht.get("banana2"))
    print("Get orange3:", ht.get("orange3"))
    ht.display()




if __name__ == "__main__":
    main()
