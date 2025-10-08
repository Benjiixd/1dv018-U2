def main() -> None:
    from assignment1 import LinkedList
    from assignment2 import Deque

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
    #dq2.removeFirst()  # should raise an exception
    
    



if __name__ == "__main__":
    main()
