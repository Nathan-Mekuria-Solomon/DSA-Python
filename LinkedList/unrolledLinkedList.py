class Node:
    def __init__(self):
        self.next = None
        self.data = None

class LinkedBlock:
    def __init__(self):
        self.head = None
        self.next = None
        self.nodeCount = 0
        
blockSize = 2
blockHead = None

# create an empty block
def newLinkedBlock():
    newBlock = LinkedBlock()
    newBlock.head = None
    newBlock.next = None
    newBlock.nodeCount = 0
    return newBlock

# create a node
def newNode(value):
    temp = Node()
    temp.next = None
    temp.data = value
    return temp

def searchElement(blockHead, k):
    #search for the block
    p = blockHead
    j = (k + blockSize - 1) // blockSize
    
    j -= 1
    while(j):
        p = p.next
        j -= 1
        
    fLinkedBlock = p
    
    # search for Node
    k = k % blockSize
    q = p.head
    
    if k == 0:
        k = blockSize
    
    k = p.nodeCount + 1- k # inside the linkedblock the list is reversed
    
    while k > 0:
        q = q.next
        k -= 1
        
    fNode = q
    
    return fLinkedBlock, fNode

# start shift operation from block *p
def shift(A):
    B = A
    global blockHead
    
    #if need shift, if the last, create another bolck if not shift to the next block
    while(A.nodeCount > blockSize):
        if A.next == None:
            # create the next linked block
            A.next = newLinkedBlock()                       
            B = A.next                # assign it as next A
            temp = A.head.next          # temp variable for the last element
            A.head.next = A.head.next.next    # remove from a
            B.head = temp              # head to temp
            temp.next = temp
            A.nodeCount -= 1            # adjust the counts
            B.nodeCount += 1
        else:
            B = A.next
            temp = A.head.next
            A.head.next = temp.next
            temp.next = B.head.next
            B.head.next = temp
            B.head = temp
            A.nodeCount -= 1
            B.nodeCount += 1
            A = B #make adjustment
           
def addElement(k, x):
    global blockHead
    r = newLinkedBlock()
    p = Node()
    
    if blockHead == None: #first block first node
        blockHead = newLinkedBlock()
        blockHead.head = newNode(x)
        blockHead.head.next = blockHead.head # mistake was made here
        blockHead.nodeCount += 1
    
    elif k == 0: #first element
        p = blockHead.head
        q = p.next
        p.next = newNode(x)
        p.next.next = q
        blockHead.head = p.next
        blockHead.nodeCount += 1
        shift(blockHead)
        
    else:
        r, p = searchElement(blockHead, k)
        q = p
        while q.next != p: #find prev of p
            q = q.next
        
        q.next = newNode(x)
        q.next.next = p
        r.nodeCount += 1
        shift(r)
    
    return blockHead # check the example

def searchElements(blockHead, k):
    r, p = searchElement(blockHead, k)
    return p.data

blockHead = addElement(0, 11)    
blockHead = addElement(0, 21)    
blockHead = addElement(1, 19)    
blockHead = addElement(1, 23)    
blockHead = addElement(2, 16)    
blockHead = addElement(2, 35)    
print(searchElements(blockHead, 6))    