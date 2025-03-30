class TreeNode(object):
    def __init__(self):
        self.data = None # current node
        self.left = None # left node
        self.right = None # right node
        
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setLeft(self, left):
        self.left = left
        
    def getLeft(self):
        return self.left
    
    def setRight(self, right):
        self.right = right
        
    def getRight(self):
        return self.right
    
def preorderRecursion(root, result):
    if not root:
        return 
    
    result.append(root.getData())
    preorderRecursion(root.getLeft(), result)
    preorderRecursion(root.getRight(), result)
    
    return result

def preorderIterative(root, result):
    if not root:
        return
    
    stack = []
    stack.append(root)
    
    while stack:
        node = stack.pop()
        result.append(node.getData())
        if node.getRight(): stack.append(node.getRight())
        if node.getLeft(): stack.append(node.getLeft())
        
    return result

def inorderRecursive(root, result):
    if not root:
        return 
    
    inorderRecursive(root.getLeft(), result)
    result.append(root.getData())
    inorderRecursive(root.getRight(), result)
    
    return result

def inorderIterative(root, result):
    if not root:
        return 
    
    stack = []
    node = root
    stack.append(root)
    while stack:
        if node:
            stack.append(node)
            node = node.getLeft()
        else:
            node = stack.pop()
            result.append(node.getData())
            node = node.getRight()
                
    return result

def postorderRecursive(root, result):
    if not root:
        return 
    
    postorderRecursive(root.getLeft(), result)
    postorderRecursive(root.getRight(), result)
    result.append(root.getData())
    
    return result
            
def postorderIterative(root, result):
    if not root:
        return
    
    visited = []
    stack = []
    node = root
    
    while stack or node:
        if node:
            stack.append(node)
            node = node.getLeft()
        else:
            node = stack.pop()
            if node.getRight() and not node.getRight() in visited:
                stack.append(node)
                node = node.getRight()
            else:
                visited.append(node)
                result.append(node.getData())
                node = None
                
    return result    
            
class Queue(object):
    def __init__(self):
        self.queue = []
        
    def enQueue(self, data):
        self.queue.append(data)
        
    def deQueue(self):
        if self.queue == []:
            raise IndexError
        
        temp = self.queue[0]
        self.queue.remove(temp)
        return temp
    
    def empty(self):
        return self.queue == []

         
def levelorder(root):
    if not root:
        return
    
    result = []
    queue = Queue()
    node = root
    queue.enQueue(node)
    
    while not queue.empty():
        node = queue.deQueue()
        result.append(node.getData())
        if node.getLeft():
            queue.enQueue(node.getLeft())
        if node.getRight():
            queue.enQueue(node.getRight())
            
    return result

# Example
one = TreeNode()
two = TreeNode()
three = TreeNode()
four = TreeNode()
five = TreeNode()
six = TreeNode()
seven = TreeNode()

one.setData(1)
two.setData(2)
three.setData(3)
four.setData(4)
five.setData(5)
six.setData(6)
seven.setData(7)

one.setLeft(two)
one.setRight(three)
two.setLeft(four)
two.setRight(five)
three.setLeft(six)
three.setRight(seven)


def isometric(root1, root2):
    if not root1 and not root2:
        return 1
    
    if (not root1 and root2) or (not root2 and root1):
        return 0
    
    return (isometric(root1.left, root2.left)) and (isometric(root1.right, root2.right))

# time complexity O(n) and space complexity --> for stack O(n)

def quasiIsometric(root1, root2):
    if not root1 and not root2:
        return 1
    
    if (not root1 and root2) or (root1 and not root2):
        return 0
    
    return quasiIsometric(root1.right, root2.right) or quasiIsometric(root1.left, root2.left) or \
            quasiIsometric(root1.right, root2.left) or quasiIsometric(root1.left, root2.right)
            
# power of recursion

"""problem 47 - k-ary in preorder traversal"""
import queue

class karyNode:
    def __init__(self, data = None):
        self.data = data
        self.children = []
        
def karyTree(lst, k): #list and k as an argument
    n = len(lst)
    if len == 0:
        return None
    
    index = 0
    root = karyNode(lst[0])
    
    Q = queue.Queue()
    Q.put(root)
    if not Q:
        return None
    
    while not Q.empty():
        temp = Q.get()
        for i in range(k):
            index += 1
            if index < n:
                temp.children.insert(i, karyNode(lst[index]))
                Q.put(temp.children[i])
                
    return root
    
def preorder(kroot):
    if not kroot:
        return
    
    q = queue.Queue()
    q.put(kroot)
    while not q.empty():
        temp = q.get()
        print(temp.data)
        for child in temp.children:
            q.put(child)
            
            
            
