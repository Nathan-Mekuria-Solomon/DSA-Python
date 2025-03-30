"""Simple circular array implimentation of QUEUE"""
class Queue(object):
    def __init__(self, limit = 5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rare = None
        self.size = 0
        
    def isEmpty(self):
        return self.size <= 0
    
    def enQueue(self, item):
        if self.size >= self.limit:
            print("Queue overflow.")
            return 
        else:
            self.que.append(item)
        
        if self.front == None:
            self.front = self.rare = 0
        else:
            self.rare = self.size
            
        self.size += 1
        print("Queue after enQueue", self.que)
        
    def deQueue(self):
        if self.size <= 0:
            print("Queue underflow")
            return 0
        else:
            temp = self.que.pop(0)   # poping index 0
            self.size -= 1
            if self.size == 0:
                self.front = self.rare = None
            else:
                self.rare = self.size - 1
            
            return temp
        
    def queueRare(self):
        if self.rare is None:
            print("The queue is empty")
            raise IndexError
        return self.que[self.rare]
    
    def queueFront(self):
        if self.size == 0:
            print("The queue is empty")
            raise IndexError
        return self.que[0]
    
    def ssize(self):
        return self.size
    
    

"""Dynamic circular array representation of QUEUE"""

class Queue2(object):
    def __init__(self, limit = 2):
        self.que = []
        self.limit = limit
        self.front = None
        self.rare = None
        self.size = 0
        
    def enQueue(self, item):
        if self .size >= self.limit:
            self.resize()
        
        self.que.append(item)
        self.size += 1
            
        if self.front is None:
            self.front = self.rare = 0
        else:
            self.rare = self.size - 1
        print("Queue after append", self.que)
        
    def deQueue(self):
        if self.size <= 0:
            print("Queue underflow")
            return 0
        
        self.que.pop(0)
        self.size -= 1
        if self.size == 0:
            self.front = self.rare = None
        else:
            self.rare = self.size - 1
        
    def queueFront(self):
        if self.front is None:
            print("Empty Queue")
            raise IndexError
        
        return self.que[self.front]
    
    def queueRare(self):
        if self.rare is None:
            print("Empty Queue")
            raise IndexError
        
        return self.que[self.rare]
    
    def ssize(self):
        return self.size
    
    def resize(self):
        newque = list(self.que)
        self.limit = 2 * self.limit
        self.que =  newque
        print("The array has been resized to: ", self.limit)
        

"""Linked list implementation of QUEUE"""
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
        
class Queue3(object):
    def __init__(self):
        self.rare = None
        self.front = None
        self.size = 0
        
    def enQueue(self, item):
        newNode = Node()
        newNode.setData(item)
        newNode.setNext(None)
        if self.size <= 0:
            self.front = self.rare = newNode
        else:
            self.rare.setNext(newNode)
            self.rare = newNode
            
        self.size += 1
        
        temp = self.front
        temp2 = []
        for i in range(self.size):
            temp2.append(temp.getData())
            temp = temp.next
            
        print("Elements as a list after append", temp2)
        
    def deQueue(self):
        if self.size <= 0:
            print("Empty queue")
            return 0
        
        temp = self.front
        while temp.next != self.rare:
            temp = temp.next
            
        temp.setNext(None)
        self.rare = temp
        
        self.size -= 1
        
        temp = self.front
        temp2 = []
        while temp != None:
            temp2.append(temp.getData())
            temp = temp.next
            
        print("Elements as a list after append", temp2)
            
    def queueFront(self):
        if self.size == 0:
            print("Empty Queue")
            raise IndexError
        
        return self.front.getData()
        
    def queueRare(self):
        if self.rare is None:
            print("Empty Queue")
            raise IndexError
        
        return self.rare.getData()
    
    def ssize(self):
        return self.size
    
