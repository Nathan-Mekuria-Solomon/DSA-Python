class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
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
    
    def setPrev(self, prev):
        self.prev = prev
    def getPrev(self):
        return self.prev
    def hasPrev(self):
        return self.prev != None
    
    def __str__(self):
        return f'Node[{self.data}]'
    
class DLL:
    """Initializing double linked list"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    """Insertion methods"""
    
    #at the beginning
    def insertAtBeginning(self, data):
        newNode = Node(data, None, None)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.setPrev(None)
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
        self.count += 1
            
    #at the end
    def insertAtEnd(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            self.tail = self.head
        else:
            current = self.head
            
            while(current.getNext() != None):
                current = current.getNext()
                
            current.setNext(Node(data, None, current))
            self.tail = current.getNext()
        self.count += 1
    
    def getNode(self, index):
        if self.head == None:
            return None
        elif index > 0:
            i = 0
            current = self.head
            while (i < index - 1) and (current.getNext() != None):
                current = current.getNext()
                i += 1
                
        return current           

    def insertAtMiddle(self, index, data):
        # create a node
        newNode = Node(data)
        
        # if empty DLL add at beginning
        if self.head == None or index == 0:
            self.insertAtBeginning(data)
            
        # not := getindex
        else:
            temp = self.getNode(index)
            
            # if None or next is none, add at end
            if temp == None or temp.getNext() == None:
                self.insertAtEnd(data)
            else:
                newNode.setPrev(temp)
                newNode.setNext(temp.getNext())
                temp.getNext().setPrev(newNode)
                temp.setNext(newNode)
                self.count += 1

    def deleteAtBeginning(self):
        # temp variable for head
        temp = self.head
        if temp == None:
            return 
        
        # head to next node
        if temp.getNext() == None:
            self.head = None
            self.tail = None
        else:
            self.head = temp.getNext()       
            temp.getNext().setPrev(None)                # cancel the linkage
        
        self.count -= 1   
        
    def deleteAtEndIterative(self):
        current = self.head
        currentPrev = current
         
        if current == None:  return   # if empty
         
        current = current.getNext()
        if current == None:
            self.head = None
            self.tail = None
        else:
            while current.getNext() != None:  #finding last and 2' to last nodes
                currentPrev = current
                current = current.getNext()
    
            currentPrev.setNext(None)
            self.tail = currentPrev
        self.count -= 1
        
    def deleteAtEnd(self):
        current = self.tail
        if self.tail == None: return # empty list
        
        currentPrev = current.getPrev()
        if currentPrev == None: # only one element
            self.head = None
            self.tail = None
            
        currentPrev.setNext(None)
        self.tail = currentPrev  
        
        self.count -= 1   

    def deleteByIndex(self, index):
        temp = self.getNode(index)
        
        if temp:
            temp.getPrev().setNext(temp.getNext())
            if temp.getNext():
                temp.getNext().setPrev(temp.getPrev())
                
            temp.setPrev(None)
            temp.setNext(None)
            temp.setData(None)
            
            self.count -= 1
            
    def deleteByData(self, data):
        temp = self.head
    
        while temp is not None:
            if temp.getData() == data:
                if temp.getPrev() == None:
                    self.head = temp.getNext()
                    temp.getNext().setPrev(None)
                else:
                    temp.getPrev().setNext(temp.getNext())
                    temp.getNext().setPrev(temp.getPrev())
            
            temp = temp.getNext()
            
        self.count -= 1


         
a = DLL()
a.insertAtEnd(1)
a.insertAtEnd(2)
a.insertAtEnd(3)
a.insertAtEnd(4)
a.insertAtMiddle(2, 5)
a.deleteAtEnd()
a.deleteByIndex(2)
a.deleteByData(5)


current = a.head

for i in range(a.count):
    print(current.getData())
    current = current.getNext()