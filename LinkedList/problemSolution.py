"""Problem 1:
    finding nth node from the last"""
    
class Node:
    def __init__(self, element = None):
        self.next = None
        self.data = element
    
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next != None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def nthNode(self, n):
        if n < 0:
            return None
        
        temp = self.head
        count = 0
        while count < n and None != temp:
            temp = temp.next
            count += 1
            
        if count < n or None == temp:
            return None
        
        nth = self.head
        while temp.next != None:
            temp = temp.next
            nth = nth.next
            
        return nth

"""Problem 6:
    check whether a loop is present (circular linkedlink)"""

"""Brute-force approach: depending on the knowledge of size"""

class Node6:
    def __init__(self):
        self.data = None
        self.next = None
        
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return (self.next != None)
    

class LinkedList6(object):
    def __init__(self):
        self.head = None
        self.size = 0
        
    def addElement(self, element):
        newNode = Node()
        newNode.setData(element)
        
        if self.head == None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
            
        self.size += 1
        
    def deleteElement(self):
        if self.head == None:
            print("Deleting empty linkedlist")
            raise IndexError
        
        if self.size == 1:
            self.size -= 1
            newNode = self.head
            self.head = None
            return newNode.getData()
        else:
            newNode = self.head
            self.head = self.head.getNext()
            self.size -= 1
            return newNode.getData()
        
    def connect(self, k):
        newNode = self.head
        for i in range(k):
            newNode= newNode.getNext()
            
        newNode2 = self.head
        while newNode2.getNext() is not None:
            newNode2 = newNode2.getNext()
            
        newNode2.setNext(newNode)
        
    def ssize(self):
        return self.size
        
l = LinkedList6()
l.addElement(1)
l.addElement(2)
l.addElement(3)
l.addElement(4)
l.addElement(5)
l.connect(2)

def isLoop(linkedlist):
    newNode = linkedlist.head
    
    for i in range(linkedlist.ssize() - 1):
        newNode2 = newNode
        for j in range(i , linkedlist.ssize()):
            newNode2 = newNode2.getNext()
            if newNode is newNode2:
                return newNode
        
        newNode = newNode.getNext()
            
    return False

"""FLOYD algorithm for cyclic linkedlist"""
def floyd(linkedlist):
    fastptr = linkedlist.head
    slowptr = linkedlist.head
    
    while fastptr and slowptr:
        if fastptr == None:
            return False
        
        fastptr = fastptr.getNext()
        if fastptr == slowptr:
            return True
        
        if fastptr == None:
            return False
        
        fastptr = fastptr.getNext()
        if fastptr == slowptr:
            return True
        
        slowptr = slowptr.getNext()
        
"""Founding the beginning of the loop"""
def detectCycle(linkedlist):
    if linkedlist.head == None or linkedlist.head.getNext() == None:
        return None
    
    slowptr = linkedlist.head.getNext()
    fastptr = slowptr.getNext()

    while fastptr != slowptr:
        slowptr = slowptr.getNext()
        try:
            fastptr = fastptr.getNext().getNext()
        except AttributeError:
            return None
        
    slowptr = linkedlist.head
    while slowptr != fastptr:
        slowptr = slowptr.getNext()
        fastptr = fastptr.getNext()
        
    loopStart = slowptr
    sizeOfLoop = 1
    while slowptr.getNext() != loopStart:
        slowptr = slowptr.getNext()
        sizeOfLoop += 1
        
    return sizeOfLoop

"""Problem 15:
    Adding a node in sorted list"""
    
class Node15:
    def __init__(self, item = None, next = None):
        self.data = item
        self.next = next
        
    def setData(self, data):
        self.data = data
        
    def setNext(self, next):
        self.next = next
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next != None
    
class LinkedList15(object):
    def __init__(self):
        self.head = None
        self.size = 0
        
    def addFront(self, item):
        newNode = Node15(item)
        if self.head == None:
            self.head = newNode
        else:
            curr = self.head
            previous = None
            stop = False
            
            while curr != None and not stop:
                if curr.getData() > item:
                    stop = True
                else:
                    previous = curr
                    curr = curr.getNext()
                    
            if previous == None:
                newNode.setNext(self.head)
                self.head = newNode
            else:
                newNode.setNext(curr)
                previous.setNext(newNode)
                
        self.size += 1
        
    def display(self):
        curr = self.head
        while curr != None:
            print(curr.getData())
            curr = curr.getNext()
            
    # time complexity O(n), space complexity O(1)
    
    """Reverse the order of the linkedlist in O(n)"""
    
    #iterative version
    def reverseOrder(self):
        last = None
        current = self.head
        
        while current != None:
            nextNode = current.getNext()
            current.setNext(last)
            last = current
            current = nextNode
        
        self.head = last # I forgot to add this part in the first trial
        
    # recursive version
    def reverseRecursive(self, n):
        if None != n:
            right = n.getNext()
        else:
            return
            
        if self.head == n:
            n.setNext(None)
        else:
            n.setNext(self.head)
            self.head = n
            
        self.reverseRecursive(right)
        
    # time complexity O(n), space complexity O(n) --> recursive stack
    
"""Two linkedlist that intersect at some point"""

"""Problem 17: using brute-force algorithm, find the intersecting point of the lists"""

class LinkedNodes(object):
    def __init__(self):
        self.head = None
        self.size = None
        
    def addFront(self, node):
        if self.head == None:
            self.head = node
        else:
            node.setNext(self.head)
            self.head = node
            
    def display(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.setNext()
            
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

linkedlist1 = LinkedNodes()
linkedlist1.addFront(node1)
linkedlist1.addFront(node2)
linkedlist1.addFront(node3)
linkedlist1.addFront(node4)
linkedlist1.addFront(node5)

linkedlist2 = LinkedNodes()
linkedlist2.addFront(node1)
linkedlist2.addFront(node2)
linkedlist2.addFront(node6)
linkedlist2.addFront(node7)

def linkedPoint(linkedlist1, linkedlist2):
    currNode1 = linkedlist1.head
    currNode2 = linkedlist2.head
    while currNode1:
        while currNode2:
            if currNode1 == currNode2:
                return currNode1.getData()
            
            currNode2 = currNode2.getNext()
        
        currNode2 = linkedlist2.head
        currNode1 = currNode1.getNext()
        
# time complexity O(m*n), space complexity O(1)

"""using two stacks to find the linking point"""
def mergePointUsingStack(lst1, lst2):
    stk1 = Stack()
    stk2 = Stack()
    
    curr = lst1.head
    while curr:
        stk1.push(curr)
        curr = curr.getNext()
        
    curr = lst2.head
    while curr:
        stk2.push(curr)
        curr = curr.getNext()
    
    intersection = None
    while stk1.top() == stk2.top():
        intersection = stk1.pop()
        stk2.pop()
        
    if intersection == None:
        return None
    return intersection.getData()

class Stack(object):
    def __init__(self):
        self.lst = []
        
    def push(self, element):
        self.lst.append(element)
        
    def pop(self):
        return self.lst.pop()
    
    def top(self):
        return self.lst[len(self.lst) - 1]
    
# time complextiry O(n + m)  and space complexity O(n + m) --> stack
        
def intersectionByDifference(list1, list2):
    curr1 = list1.head
    curr2 = list2.head
    size1, size2 = 0, 0
    
    while curr1:
        size1 += 1
        curr1 = curr1.getNext()
        
    while curr2:
        size2 += 1
        curr2 = curr2.getNext()
        
    curr1, curr2 = list1.head, list2.head
    
    if size1 > size2:
        for i in range(size1 - size2):
            curr1 = curr1.getNext()
    elif size2 > size1:
        for i in range(size2 - size1):
            curr2 = curr2.getNext()
            
    while curr1 != curr2:
        curr1 = curr1.getNext()
        curr2 = curr2.getNext()
        
    if curr1 == None:
        return None
    return curr1.getData()

# time complextity O(max(m, n)) and space complexity O(1)

"""Middle of the linkedlist with one scanning"""
def middle(linkedlist):
    fastptr = linkedlist.head
    slowptr = linkedlist.head
    
    while fastptr != None:
        fastptr = fastptr.getNext()
        if fastptr == None:
            return slowptr.getData()
        
        fastptr = fastptr.getNext()
        slowptr = slowptr.getNext()
        
    return slowptr.getData()

# time complextity O(n), space complexity O(1)

"""Printing a linkedlist from the back"""
class NodeB:
    def __init__(self):
        self.data = None
        self.next = None
        
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return (self.next != None)
    
class LinkedListB(object):
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add(self, data):
        newNode = NodeB()
        newNode.setData(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
            
        self.size += 1
        
    def sortedMerge(self, lst1, lst2):
        temp = NodeB()
        pointer = temp
        
        while lst1 != None and lst2 != None:
            if lst1.getData() > lst2.getData():
                pointer.setNext(lst2)
                lst2 = lst2.getNext()
            else:
                pointer.setNext(lst1)
                lst1 = lst1.getNext()
                
            pointer = pointer.getNext()
            
        if lst1 == None:
            pointer.setNext(lst2)
        else:
            pointer.setNext(lst1)
            
        return temp.getNext()
    
    
        
def reversePrint(lst):
    head = lst
    if head == None:
        return 
    
    tail = head.getNext()
    reversePrint(tail)
    print(head.getData())
        
"""Effecient way for determining the parity of the size of a linked list"""
def parity(lst):
    curr = lst.head
    while curr and curr.getNext():
        curr = curr.getNext().getNext()
        if not curr:
            return "even"
        
    return "odd"

# time complexity O(n/2) = O(n), space complexity of O(1)
    
"""Merging two merged linkedlist in the third sorted linkedlist"""

"""Reverse in paris"""
def reverseInParis(lst):
    temp = lst.head
    while temp != None and temp.getNext() != None:
        swap(temp, temp.getNext())
        temp = temp.getNext().getNext()

def swap(a, b):
    tmp = a.getData()
    a.setData(b.getData())
    b.setData(tmp)
    
"""Spliting circular linkedlist into two"""
#using floyd algorithm

def splitList(circularList):
    slowptr = circularList.head
    fastptr = circularList.head
    
    while fastptr != None and fastptr.getNext() != None: #finding the middle of the list
        slowptr = slowptr.getNext()
        fastptr = fastptr.getNext().getNext()
        
    if fastptr == None: #odd number of nodes
        secondHead = slowptr
    else:
        secondHead = slowptr.getNext()
        
    return circularList.head.getData(), secondHead.getData()


