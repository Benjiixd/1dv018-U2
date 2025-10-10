from assignment1 import LinkedList
from assignment2 import Deque
from assignment3 import BST
from assignment4 import HashTable
from assignment5 import Veichle
import random
import string

def main() -> None:
    assignment1test()
    assignment2test()
    assignment3test()
    assignment4test()
    assignment5test()

# ______ test code for assignment 1  _______
def assignment1test():
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

# ______ test code for assignment 2  _______
def assignment2test():
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

# ______ test code for assignment 3  _______  
def assignment3test():
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

# ______ test code for assignment 4  _______
def assignment4test():
    print("\n___Assignment 4 Test (HashTable)___")
    ht = HashTable(8)
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

# ______ test code for assignment 5  _______
def assignment5test():
    print("\n___Assignment 5 Test (HashTable with veichles)___")
    
    ht2 = HashTable(8)
    #0
    print(f"Number of collisions: {ht2.collision_count()} of {ht2._n} objects (capacity={ht2.capacity})")
    temp = None
    testVeichle = Veichle("911", "porsche", 0, "abc123")
    ht2.put(testVeichle.regnr, testVeichle)
    # create 20 cars
    for _ in range(20):
        temp = createRandomCar()
        ht2.put(temp.regnr, temp)
    ht2.display()

    # see if we can find the porsche
    print("find the porche (abc123):", ht2.get("abc123"))
    # remove it and make sure we cant find it
    ht2.remove("abc123")
    try:
        print("find the porche (abc123):", ht2.get("abc123"))
    except KeyError as e:
        print("couldnt find the porche after deletion")
    # 20 cars
    print(f"Number of collisions: {ht2.collision_count()} of {ht2._n} objects (capacity={ht2.capacity})")
    # create 30 more (50)
    for _ in range(30):
        temp = createRandomCar()
        ht2.put(temp.regnr, temp)
    print(f"Number of collisions: {ht2.collision_count()} of {ht2._n} objects (capacity={ht2.capacity})")

    # create 50 more (100)
    for _ in range(50):
        temp = createRandomCar()
        ht2.put(temp.regnr, temp)
    print(f"Number of collisions: {ht2.collision_count()} of {ht2._n} objects (capacity={ht2.capacity})")
    #200
    for _ in range(100):
        temp = createRandomCar()
        ht2.put(temp.regnr, temp)
    print(f"Number of collisions: {ht2.collision_count()} of {ht2._n} objects (capacity={ht2.capacity})")
    #500
    for _ in range(300):
        temp = createRandomCar()
        ht2.put(temp.regnr, temp)
    print(f"Number of collisions: {ht2.collision_count()} of {ht2._n} objects (capacity={ht2.capacity})")
    #1000
    for _ in range(500):
        temp = createRandomCar()
        ht2.put(temp.regnr, temp)
    print(f"Number of collisions: {ht2.collision_count()} of {ht2._n} objects (capacity={ht2.capacity})")

    for cap in [8, 16, 32, 64]:
        ht3 = HashTable(capacity=cap)
        for _ in range(200):
            car = createRandomCar()
            ht3.put(car.regnr, car)
        print(f"Capacity={cap}: {ht3.collision_count()} collisions of {ht3._n} objects")


# code to create random car objects
def createRandomCar():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    digits = ''.join(random.choices(string.digits, k=3))
    brands = ["Volvo", "Saab", "Tesla", "BMW", "Audi", "Toyota"]
    models = ["V60", "9-3", "Model 3", "X5", "A4", "Corolla"]

    reg = letters+digits
    brand = random.choice(brands)
    model = random.choice(models)
    mileage = random.randint(5000, 200000)
    v = Veichle(model, brand, mileage, reg)
    return v

if __name__ == "__main__":
    main()
