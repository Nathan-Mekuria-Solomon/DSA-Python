"""Problem 1:
    Algorithm for reversing a queue using just queue abstract datatype (ADT)"""
  
"""Dynamic array"""  
class Stack(object):
    def __init__(self, limit = 10):
        self.stk = []
        self.limit = limit
        self.size = 0
        
    def push(self, item):
        if self.size >= self.limit:
            self.resize()
        self.stk.append(item)
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            print("The stack is empty")
            return 0
        
        self.size -= 1
        return self.stk.pop()        
    
    def isEmpty(self):
        return self.stk == []
    
    def resize(self):
        newStk = self.stk
        self.limit = 2 * self.limit
        self.stk = newStk
        
    def top(self):
        return self.stk[self.size - 1]
           
"""Queue:  Linked list implementation"""   

"""Node class"""
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
    
"""Queue class"""
class Queue(object):
    def __init__(self):
        self.front = None
        self.rare = None
        self.size = 0
        
    def enQueue(self, data):
        newNode = Node()
        newNode.setData(data)
        
        if self.front is None:
            self.front = self.rare = newNode
        else:
            self.rare.next = newNode
            self.rare = newNode
            
        self.size += 1
        
        temp = self.front
        lst = []
        
        while temp is not None:
            lst.append(temp.getData())
            temp = temp.next
            
        print("Items after enQueue", lst)
        
    def deQueue(self):
        if self.size <= 0:
            return 0
        
        temp = self.front
        if self.front == self.rare:
            self.front = self.rare = None
        else:
            self.front = temp.next
            
        self.size -= 1
            
        return temp.getData()
    
    def queueFront(self):
        if self.size <= 0:
            print("Empty queue")
            raise IndexError
        
        return self.front.getData()
    
    def queueRare(self):
        if self.size <= 0:
            print("Empty queue")
            raise IndexError
        
        return self.rare.getData()
    
    def ssize(self):
        return self.size
    
    def isEmpty(self):
        return self.size <= 0
    
def reverse(queue):
    stack = Stack()
    while not queue.isEmpty():
        stack.push(queue.deQueue())
    
    queue2 = Queue()
    while not stack.isEmpty():
        temp = stack.pop()
        queue2.enQueue(temp)
        
    temp =  queue2.front
    tempArr = []   

    while temp is not None:
        tempArr.append(temp.getData())
        temp = temp.getNext()
        
    print("The inversed queue as a list: ", tempArr)
    
# time complexity O(n)

"""problem 2:
    Queue implementation using two stacks"""
    
class Queue2(object):
    def __init__(self):
        self.S1 = []
        self.S2 = []
        
    def enQueue(self, item):
        self.S1.append(item)
        
    def deQueue(self):
        if not self.S2: # if s2 is empty
            while self.S1: # s1 not empty
                self.S2.append(self.S1.pop())
        
        return self.S2.pop()
    
# amortized complexity of O(1)

"""Problem 3:
    Stack implementation using two queue"""
    
class Queue3(object):
    def __init__(self):
        self.que = []
        self.size = 0
        
    def isEmpty(self):
        return self.que == []
    
    def enQueue(self, element):
        self.que.append(element)
        self.size += 1
        
        
    def deQueue(self):
        if not self.que:
            print("deQueue empty queue")
            raise IndexError
        
        a = self.que[0]
        self.que.remove(a)   # deletes the first x that it found
        self.size -= 1
        
        return a
    
    def ssize(self):
        return self.size
    
class Stack3(object):
    def __init__(self):
        self.que1 = Queue3()
        self.que2 = Queue3()
        
    def isEmpty(self):
        return (self.que1.isEmpty() and self.que2.isEmpty())
    
    def push(self, element):
        if self.que2.isEmpty():
            self.que1.enQueue(element)
        else:
            self.que2.enQueue(element)
            
    def pop(self):
        if self.isEmpty():
            print("Poping empty stack")
            raise IndexError
        
        if self.que2.isEmpty():
            while not self.que1.isEmpty():
                curr = self.que1.deQueue()
                if self.que1.isEmpty():
                    return curr
                self.que2.enQueue(curr)
                
        else:
            while not self.que2.isEmpty():
                curr = self.que2.deQueue()
                if self.que2.isEmpty():
                    return curr
                self.que1.enQueue(curr)
                
                
"""problem 4:
    maximum number in sliding window of width w"""
    
#doubly ended queue for optimization
class DoublyQueue(object):
    def __init__(self):
        self.que = []
        
    def enQueueFront(self, element):
        self.que = [element] + self.que
        
    def enQueueRare(self, element):
        self.que.append(element)
        
    def deQueueFront(self):
        if not self.que:
            print("deQueue empty queue")
            raise IndexError
        
        a = self.que[0]
        self.que.remove(a)
        return a
    
    def deQueueRare(self):
        if not self.que:
            print("deQueue empty queue")
            raise IndexError
        
        return self.que.pop()
    
def slidingMax(A, w): # array A and int w as an input
    queue = DoublyQueue()
    for i in range(w):
        queue.enQueueRare(A[i])
    
    print(queue.que, fSlidingMax(queue))
    
    for j in range(w, len(A)):
        queue.deQueueFront()
        queue.enQueueRare(A[j])
        print(queue.que, fSlidingMax(queue))
        
def fSlidingMax(queue):
    return max(queue.que)


"""Problem 5:
    Reversing the order of the queue in O(n)"""
    
def reverseQueue(queue):
    stack = Stack5()
    while queue.que != []:
        stack.push(queue.deQueue())
        
    curr = stack.pop()
    while stack.ssize() > 0:     # I wrote is as "not stack.ssize()" and it didnt work
        queue.enQueue(curr)
        
        if stack.ssize() == 1:
            break
        
        curr = stack.pop()
               
    return curr, queue.que

class Stack5(object):
    def __init__(self):
        self.stk = []
        
    def push(self, item):
        self.stk.append(item)
        
    def pop(self):
        if self.stk == []:
            print("poping empty stack")
            raise IndexError
        
        return self.stk.pop()
    
    def ssize(self):
        return len(self.stk)
    
    def isEmpty(self):
        return self.stk == []
    
"""Problem 6:
    What is the best data structure to print queue in reverse order?"""
    
# Answer: Stack

"""Problem 7:
    Doubly-linked queue (head-tail linked list)"""
    
class HeadTailLinkedList(object):
    def __init__(self):
        self.arr = []
        
    def addFront(self, element):
        self.arr.append(element)
        
    def addRare(self, element): # insert method
        self.arr.insert(0, element)
        
    def removeFront(self):
        if self.arr == []:
            print("poping empty queue")
            raise IndexError
        
        return self.arr.pop()
    
    def removeRare(self):
        if self.arr == []:
            print("poping empty array")
            raise IndexError
        
        return self.arr.pop(0)
    
    def isEmpty(self):
        return self.arr == []
    
    
"""Problem 9:
    Are successive integer of a stack are consecutive?"""
    
# Queue3() and Stack5()
import math

def checkConsecutive(stk):
    queue = Queue3()
    isConsecutive = True
    
    while not stk.isEmpty():
        queue.enQueue(stk.pop())
        
    while not queue.isEmpty():
        stk.push(queue.deQueue())
        
    while not stk.isEmpty():
        a = stk.pop()
        queue.enQueue(a)
        if not stk.isEmpty():
            b = stk.pop()
            queue.enQueue(b)
            if (abs(a - b) != 1):
                isConsecutive = False
                break
            
    while not queue.isEmpty():
        stk.push(queue.deQueue())
        
    if isConsecutive:
        print("It is consecutive")
    else:
        print("it is not")
        
    return isConsecutive

# time complexity O(n), space complexity O(n)

"""Problem 10:
    Interleveling a given queue""" 
    
def interlevelingEven(queue):
    stack = Stack5()
    halfsize = queue.ssize() // 2
    
    for i in range(halfsize):
        stack.push(queue.deQueue())
        
    while not stack.isEmpty():
        queue.enQueue(stack.pop())
        
    for i in range(halfsize):
        queue.enQueue(queue.deQueue())
    
    for i in range(halfsize):
        stack.push(queue.deQueue())
        
    while not stack.isEmpty():
        queue.enQueue(stack.pop())
        queue.enQueue(queue.deQueue())
        
    print(queue.que)
        
"""Problem 11:
    input: queue, and k. output: reverse the first k elements, preserving the rest of the elements' order"""
    
def reverseK(queue, k):
    stack = Stack5()
    if queue is None or k > queue.ssize():  # for got to check the constaint
        return
    
    for i in range(k):
        stack.push(queue.deQueue())
        
    while not stack.isEmpty():
        queue.enQueue(stack.pop())
    
    for i in range(queue.ssize() - k):
        queue.enQueue(queue.deQueue())
        
    return queue.que

# time complexity O(n), space complexity O(n)

"""Problem 13:
    palindrome check using doubly linked queue"""
    
class Doubly(object):
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return self.queue == []
    
    def enQueueFront(self, element):
        self.queue.insert(0, element)
        
    def enQueueRare(self, element):
        self.queue.append(element)
        
    def deQueueFront(self):
        if self.isEmpty():
            print("Dequeue empty queue")
            raise IndexError
        
        return self.queue.pop(0)
    
    def deQueueRare(self):
        if self.isEmpty():
            print("Dequeue empty queue")
            raise IndexError
        
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
def palindrome(string):
    temp = Doubly()
    for letter in string:
        temp.enQueueRare(letter)
        
    isPalindrome = True
    
    while temp.size() > 1 and isPalindrome:
        a = temp.deQueueFront()
        b = temp.deQueueRare()
        if b != a:
            isPalindrome = False
                
    return isPalindrome

# time complexity O(n), space complexity O(n)
