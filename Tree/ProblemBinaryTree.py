class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None
        
def insertNode(root, data):
    if root == None:
        root = Node(data)
    else:
        if data > root.data:
            if root.right == None:
                root.right = Node(data)
            else:
                insertNode(root.right, data)
        else:
            if data < root.data:
                if root.left == None:
                    root.left = Node(data)
                else:
                    insertNode(root.left, data)

root = Node(8) 
insertNode(root, 5)              
insertNode(root, 15)              
insertNode(root, 4)              
insertNode(root, 7)              
insertNode(root, 3)              
insertNode(root, 6)              
insertNode(root, 13)              
insertNode(root, 17)              
insertNode(root, 12)              
insertNode(root, 14)              
insertNode(root, 16)              
insertNode(root, 18)              
insertNode(root, 19)  

def inorder(root):
    if root == None:
        return None
    
    inorder(root.left)
    print(root.data, end = "->")
    inorder(root.right)
                
                
                
"""Finding the least common ancestor of two nodes"""
def findCommonAncestor(root, a, b): # a and b-> nodes in question
    while(root):
        if (a > root.data and b < root.data) or (a < root.data and b > root.data):
            return root
        elif a > root.data:
            root = root.right
        else:
            root = root.left
            

"""Shortest path-way from one node to another"""
def shortestPath(root, a, b):  # pathway from a to b
    current = root
    commAnc = findCommonAncestor(current, a, b)
        
    childParent(commAnc, a)
    parentChild(commAnc, b)
    
def childParent(root, a):
    stack = []
    while root:
        stack.append(root)
        if root.data == a:
            break
        elif root.data > a:
            root = root.left
        else:
            root = root.right
            
    while stack:
        print(stack.pop().data, end = "->")
        
def parentChild(root, a):
    while root:
        if root.data == a:
            break
        elif root.data > a:
            root = root.left
            if root.data == a:
                print(root.data)
            else:
                print(root.data, end = "->")
        else:
            root = root.right
            if root.data == a:
                print(root.data)
            else:
                print(root.data, end = "->")
             
"""Problem: checking whether the tree is BinarySearchTree or not"""
"""greedy algorithm and kind of short cut because I know some properties"""
def isBinary(root):
    if not root:
        return True
    
    if isLess(root.left, root.data) and isGreat(root.right, root.data) and isBinary(root.left) and isBinary(root.right):
        return True
    else:
        return False
    
def isLess(root, value):
    if root == None:
        return True
    
    if value > root.data and isLess(root.left, value) and isLess(root.right, value):
        return True
    else:
        return False
    
def isGreat(root, value):
    if root == None:
        return True
    
    if root.data > value and isGreat(root.left, value) and isGreat(root.right, value):
        return True
    else:
        return False

six = Node(6)
two = Node(2)
one = Node(1)
nine = Node(9)
eight = Node(8)

six.left = two
six.right = eight
two.left = one
two.right = nine

# alternative approach
import sys
def BinaryUtil(root, min, max):
    if root == None:
        return True
    
    if root.data > min and root.data < max and BinaryUtil(root.left, min, root.data) and BinaryUtil(root.right, root.data, max):
        return True
    else:
        return False
    
def BinaryEfficient(root):
    return BinaryUtil(root, -sys.maxsize, sys.maxsize)



def BSTtoDLL(head): # bug on the leaves
    """main function to converst an ordered binary search tree to doubly linkedlist"""
    if not head or not head.next:
        return head
    
    curr = head
    middle = findMid(head)
    
    while curr.next != middle:
        curr = curr.next
        
    curr.next = None
    q = middle.next
    middle.next = None
    q.prev = None
    
    middle.prev = findMid(head)
    middle.next = findMid(q)
    return middle

def findMid(head):
    if not head or not head.next:
        return head
    
    slowptr = head
    fastptr = head
    
    while fastptr:
        fastptr = fastptr.next
        
        if fastptr == None:
            break
        
        slowptr = slowptr.next
        fastptr = fastptr.next            
        
    return slowptr

class DLLNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node = DLLNode(data)
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next != None and curr.data < data:
                curr = curr.next
                
            if curr.next == None:
                curr.next = node
                node.prev = curr
            elif curr == self.head:
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:
                node.next = curr
                node.prev = curr.prev
                curr.prev.next = node
                curr.prev = node
                
example = DoublyLinkedList()
example.insert(2)
example.insert(7)
example.insert(9)
example.insert(4)
example.insert(1)
example.insert(3)

root = BSTtoDLL(example.head)

# print(root.prev.prev.next.data)   

def listToBST(lst, left, right):
    if left > right:
        return None
    
    newNode = Node()
    if left == right:
        newNode.data = lst[left]
        newNode.left = None
        newNode.right = None
    else:
        mid = left + (right - left) // 2
        newNode.data = lst[mid]
        newNode.left = listToBST(lst, left, mid - 1)
        newNode.right = listToBST(lst, mid + 1, right)
        
    return newNode
        
def singlyLLtoBST(head):
    if head == None or head.next == None:
        return head
    
    middle = findMid(head)
    p = head
    while p.next != middle:
        p = p.next
        
    p.next = None
    q = middle.next 
    
    middle.prev = singlyLLtoBST(head)
    middle.next = singlyLLtoBST(q)
    
    return middle

class SingleLL(object):
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            prev = None
            
            while current != None and data > current.data:
                prev = current
                current = current.next
                
            if prev == None:
                newNode.next = self.head
                self.head = newNode
            else:
                newNode.next = prev.next
                prev.next = newNode
                

s = SingleLL()
s.insert(2)
s.insert(4)
s.insert(5)
s.insert(7)
s.insert(3)
s.insert(1)



def singleBST(head):
    if head == None or head.next == None:
        return head
    
    middle = findMid(head)
    p = head
    
    while p.next != middle:
        p = p.next
        
    q = middle.next 
    p.next = None
    middle.next = None
    
    middle.left = singleBST(head)
    middle.right = singleBST(q)
    
    return middle

