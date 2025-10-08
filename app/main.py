def main() -> None:
    from assignment1 import LinkedList

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


if __name__ == "__main__":
    main()
