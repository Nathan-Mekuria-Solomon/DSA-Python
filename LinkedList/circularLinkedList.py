"""be careful about the end and beginning... otherwise we might encounter infinte loop"""

class Node:
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
        return self.next != None
    

class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def listLength(self):
        current = self.head
        
        if current == None:
            return 0
        
        count = 1
        current = current.getNext() # one step next before going to the loop
        while current != self.head:
            current = current.getNext()
            count += 1
            
        return count
    
    def printList(self):
        current = self.head
        
        if current == None: return 0
        
        print(current.getData())
        current = current.getNext()
        
        while current != self.head:
            print(current.getData())
            current = current.getNext()
            
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        newNode.setNext(newNode) # node pointing to itself
        
        current = self.head
        if current == None:
            self.head = newNode
        else:
            while current.getNext() != self.head:
                current = current.getNext()
            
            newNode.setNext(self.head)
            current.setNext(newNode)
            self.head = newNode #d/c b/n end and front insertion
            
    def deleteLast(self):
        temp = self.head
        current = self.head
        
        if current == None:
            print("Empty list")
            return
        
        while current.getNext() != self.head:
            temp = current
            current = current.getNext()
            
        temp.setNext(self.head)
        return current.getData()
    
    def deleteFirst(self):
        # first and last element
        # assign last next -> 2nd element
        # head -> second
        current = self.head
        temp = self.head
        
        if current == None:
            print("Empty list")
            return
        
        while current.getNext() != self.head:
            current = current.getNext()
            
        current.setNext(self.head.getNext())
        self.head = current.getNext()
        return temp.getData()
    
a = CircularLinkedList()
a.insertAtBeginning(1)
a.insertAtBeginning(2)
a.insertAtBeginning(3)
a.deleteFirst()

a.printList()