#singly linked list
class Node:
    #constructor
    def __init__(self):
        self.data = None
        self.next = None
    #setData
    def setData(self, data):
        self.data = data
    #get data
    def getData(self):
        return self.data
    #set next
    def setNext(self, next):
        self.next = next
    #get next
    def getNext(self):
        return self.next
    # has next
    def hasNext(self):
        return self.next != None

# uses linked list as an input and returns the number of elements
def listLength(self):
    current = self.head
    count = 0
    
    while current != None:
        count += 1
        current = current.getNext()
        
    return count

# time complexity O(n) -> for transversing throughout the list
#space complexity O(1) -> for creating variable

# inserting at the head (beginning)
def insertAtBeginning(self, data):
    newNode = Node()
    newNode.setData(self, data)
    
    #setNext
    if self.length == 0:
        self.head = newNode
    else:
        newNode.setNext(self.head)
        self.head = newNode
        
    self.length += 1
    
# insert at the end
def insertAtEnd(self, data):
    #create new node
    newNode = Node()
    newNode.setData(self, data)
    
    #find the last node
    current = self.head
    while current.getNext != None:
        current = current.getNext()
        
    #assign new node as next of the last node
    current.setNext(newNode)
    self.length += 1
    
def insertAtPos(self, pos, data):
    if pos > self.length or pos < 0:
        return None   
    
    #check beginning and ending cases    
    if pos == 0:
        insertAtBeginning(data)
    else:
        if pos == self.length:
            insertAtEnd(data)
        else:
            #create a node
            newNode = Node()
            newNode.setData(data)
            current = self.head
            count = 0
            
            # #find node at pos - 1
            while count < (pos - 1):
                count += 1
                current = current.getNext()
                
            #assign newNode next as pos.next and pos.next as newNode    
            newNode.setNext(current.getNext())
            current.setNext(newNode)
            
            #update the length
            self.length += 1
            
#time complexity O(n)
#space complexity O(1) -> creating the variables

#deleting at the beginning
def deleteAtBeginning(self):
    #create temp Node pointing to head
    #move head to next node and dispose temp
    if self.length == 0:
        print("Empty list")
    else:
        self.head = self.head.getNext()
        self.length -= 1
        
#delete at the end
def deleteAtEnd(self):
    if self.length == 0:
        print("Empty list")
    else:
        currentNode = self.head
        prevNode = self.head
        while currentNode.getNext() != None:
            prevNode = currentNode
            currentNode = currentNode.getNext()
        
        prevNode.setNext(None)
        self.length -= 1
        
# delete with a node input
def deleteInMiddleWithNode(self, node):
    #check length
    if self.length == 0:
        raise ValueError("Empty list")
    else:
        current = self.head
        prev = None
        found = False
        
        #find the node
        while not found:
            if current == Node:
                found = True
            elif current == None:
                raise ValueError("Node cannot be found in the list")
            else:
                prev = current
                current = current.getNext()
                
    #prev node next => curr node next
    if prev == None:
        self.head = current.getNext()
    else:
        prev.setNext(current.getNext())
        
    #update the length
    self.length -= 1
    
# delete with data from a linked list
def deleteValue(self, data):
    current = self.head
    prev = self.head
    
    while current.next != None or current.data != data:
        if current.data == data:
            prev.next = current.next
            self.length -= 1
            return
        else:
            prev = current
            current = current.next
    
    print("Value cannot be found in the list")
    
# delete with a position
def deletePos(self, pos):
    #check pos in bound
    if pos > self.length or pos < 0:
        print("Position entered is invalid")
    #curr and pos until we found the position
    else:
        count = 0
        curr = self.head
        prev = self.head
        
        while count < pos or curr.next != None:
            if count == pos:
                prev.next = curr.next
                self.length -= 1
                return
            else:
                prev = curr
                curr = curr.next


# time complexity O(n)
# space complexity O(1) -> creating a temp variable

def clear(self):
    self.head = None

#time complexity O(1)
#space complexity O(1)

class Node2:
    #constructor
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
    #setdata
    def setData(self, data):
        self.data = data
        
    #getdata
    def getData(self):
        return self.data
    
    #setnext
    def setNext(self, next):
        self.next = next
        
    #getnext
    def getNext(self):
        return self.next
    
    #has next
    def hasNext(self):
        return self.next != None
    
    #set prev
    def setPrev(self, prev):
        self.prev = prev
        
    #get prev
    def getPrev(self):
        return self.prev
    
    #has prev
    def hasPrev(self):
        return self.prev != None
    
    # string equivalent of object
    def __str__(self):
        return f'Node[data = {self.data}]'
    
#adding at the beginning
def insertAtBeginning2(self, data):
    newNode = Node2(data, None, None)
    if self.head == None:
        self.head = self.tail = newNode
    else:    
        newNode.next = self.head
        newNode.prev = None
        self.head.prev = newNode
        self.head = newNode
        
#adding at the end
def insetAtEnd(self,data):
    if self.head == None:
        self.head = Node2(data, None, None)
        self.tail = self.head
    else:
        current = self.head
        
        while current.getNext() != None:
            current = current.getNext()
            
        self.current.setNext(data, None, current)
        self.tail = current.getNext()
        
