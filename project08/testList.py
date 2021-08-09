"""
File: testList.py
Author: Laurie Jones, Harry Pinkerton, James Lawson
Project: 8

A tester program for list implementations.
"""


#from abstractList import AbstractList
from linkedList import LinkedList
#from arrayList import ArrayList

def testList(listType):
    # Test Abstract List
    print("Create a list with 1-9")
    q = listType()

    print("Length:", len(q))
    print("Empty:", q.isEmpty())
    print("Add 1-10")
    for i in range(10):
        q.add(i + 1)
    print("Lyst:",  q)
    print("Length:", len(q))
    print("Empty:", q.isEmpty())
    theClone = listType(q)
    print("Items in clone (front to rear):",  theClone)
    theClone.clear()
    print("Length of clone after clear:",  len(theClone))
    print("Pop 3 items:", end = " ")
    for count in range(3): print(q.pop(), end = " ")
    print("\nQueue: ", q)
    print("Adding 11 and 12:")
    for item in range(11, 13): q.add(item)
    print("Queue: ", q)    
    print("Popping items (front to rear): ", end="")
    while not q.isEmpty(): print(q.pop(), end=" ")
    print("\nLength:", len(q))
    print("Empty:", q.isEmpty())
    print("Create with 11 items:")
    q = listType(range(1, 12))
    print("Items (front to rear):",  q)
    q = listType(range(1, 11))
    print("Items (front to rear):",  q)
    print("Popping two items: ", q.pop(), q.pop(), q)
    print("Adding five items: ", end = "")
    for count in range(5):
        q.add(count)
    print(q)


    
def testListIterator(listType):
# Create and use a list iterator
    #lyst = ArrayList(range(1,10))
    lyst = LinkedList(range(1,10))
    print("Length:", len(lyst))
    print("Items (first to last): ", lyst)
    listIterator = lyst.listIterator()
    print("Forward traversal: ", end = "")
    listIterator.first()
    while listIterator.hasNext():
        print(listIterator.next(), end = " ")
    print("\nBackward traversal: ", end = "")
    listIterator.last()
    while listIterator.hasPrevious():
        print(listIterator.previous(), end = " ")
    print("\nInserting 10 before 3: ", end = "")
    listIterator.first()
    for count in range(3):
        listIterator.next()
    listIterator.insert(10)
    print(lyst)
    print("Removing 2: ", end = "")
    listIterator.first()
    for count in range(2):
        listIterator.next()
    listIterator.remove()
    print(lyst)
    print("removing all items")
    listIterator.first()
    while listIterator.hasNext():
        listIterator.next()
        listIterator.remove()
    print("Length:", len(lyst))

if __name__ == '__main__':
    testList(LinkedList)
    #testList(ArrayList)
    #testListIterator(LinkedList)
    #testListIterator(ArrayList)
    

