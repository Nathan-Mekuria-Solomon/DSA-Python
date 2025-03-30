# simple array implementation of stack
class Stack(object):
    # constructor
    def __init__(self, limit = 10):
        self.limit = limit
        self.stk = []
    
    # isEmpty
    def isEmpty(self):
        return len(self.stk) <= 0
    
    # push
    def push(self, value):
        if len(self.stk) >= self.limit:
            print("Stack Overflow")
        else:
            self.stk.append(value)
    
    # pop
    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return 0
        self.stk.pop()
    
    # peek
    def peek(self):
        if self.isEmpty():
            print("Empty stack")
            return 0
        return self.stk[-1]
    
    # size
    def size(self):
        return len(self.stk)
    
"""Linked List implementation of stack"""
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
    
class Stack2(object):
    #constructor
    def __init__(self, data = None):
        self.head = None
        for data in data:
            self.push(data)
    
    # push
    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp 
    
    # pop
    def pop(self):
        if self.head == None:
            raise IndexError
        temp = self.head
        self.head = self.head.next
        return temp.getData()
    
    # peek
    def peek(self):
        if self.head == None:
            print("Empty stack")
            return 0
        return self.head.getData()
    
    

