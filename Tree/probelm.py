# recursively getting the maximum value time complexity O(n)

class TreeNode(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        
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
    
    
max = float("-infinity")
def getMax(root):
    global max
    if not root:
        return
    
    if root.getData() > max:
        max = root.getData()
        
    getMax(root.getLeft())
    getMax(root.getRight())
    
    return max
    
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

"""Return the number of nodes in the tree"""
def numOfNodes(root):
    if not root:
        return 0
    
    return numOfNodes(root.left) + numOfNodes(root.right) + 1

# without recursion
import queue

def levelorderCounting(root):
    if not root:
        return 0
    
    q = queue.Queue()
    q.put(root)
    count = 0
    
    while not q.empty():
        node = q.get()
        count += 1
        
        if node.getLeft():
            q.put(node.left)
        if node.getRight():
            q.put(node.getRight())
            
    return count

# reverse lever order traverse using recursion
def reverseLevelorder(root):
    if not root:
        return
    
    que = queue.Queue()
    stack = []
    que.put(root)
    node = None
    
    while not que.empty():
        node = que.get()
        if node.getLeft():
            que.put(node.getLeft())
        if node.getRight():
            que.put(node.getRight)
            
        stack.append(root)
        
    while not stack:
        print(stack.pop().getData())
        
"""Problem 48:
    finding preorder successor without using threading"""
    
P = None
    
def preorderWithout(root):
    stack = []
    global P
    
    if root:
        P = root
        
    if P.left != None:
        stack.append(P)
        P = P.left
    else:
        while(P.right == None):
            P = stack[0]
            stack.remove(P)
            P = P.right
            
    return P.data

def inorderWithout(root):
    stack = []
    if root:
        P = root
        
    if P.right == None:
        P = stack.pop()
    else:
        P = P.right
        while P.left:
            stack.append(P)
            P = P.left
            
    return P.data

# poping an empty stack has been a problem

opertatorPrecedence = {
    '(':0,
    ')':0,
    '+':1,
    '-':1,
    '*':2,
    '/':2,
}

def prefix(infix):
    stack = []
    prefixExp = []
    
    for val in infix:
        if val not in opertatorPrecedence:
            prefixExp.append(val)
        else:
            if len(stack) == 0:
                stack.append(val)
            elif val == '(':
                stack.append(val)
            elif val == ')':
                while stack[-1] != '(':
                    prefixExp.append(stack.pop())
                stack.pop()
            elif opertatorPrecedence[val] <= opertatorPrecedence[stack[-1]]:
                while len(stack) != 0:
                    if stack[-1] == '(':
                        break
                    prefixExp.append(stack.pop())
                stack.append(val)
                
            else:
                stack.append(val)
                
    while stack != []:
        prefixExp.append(stack.pop())
        
    return prefixExp


class Node:
    def __init__(self, data = None):
        self.data = data
        self.right = None
        self.left = None

class ExpressionTree(object):
    def __init__(self, root):
        self.root = root
        
    def inorder(self):  # why do we need the helper function
        self.inorderHelper(self.root)
        
    def inorderHelper(self, node):
        if node:
            self.inorderHelper(node.left)
            print(node.data, end = "")
            self.inorderHelper(node.right)
            
    def preorder(self):
        self.preorderHelper(self.root)
        
    def preorderHelper(self, node):
        if node:
            print(node.data, end = "")
            self.preorderHelper(node.left)
            self.preorderHelper(node.right)
            
    def postorder(self):
        self.postorderHelper(self.root)
        
    def postorderHelper(self, node):
        if node:
            self.postorderHelper(node.left)
            self.postorderHelper(node.right)
            print(node.data, end = "")
            
def expressionTree(infix):
    preFix = prefix(infix)
    stack = []
    
    for char in preFix:
        if char in opertatorPrecedence:
            node = Node(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
        else:
            node = Node(char)
            stack.append(node)
            
    return ExpressionTree(stack.pop())
print("Inorder: ")
expressionTree('(5+3)*6').inorder()
print()
print("preorder")
expressionTree('(5+3)*6').preorder()
print()
print("postorder")
expressionTree('(5+3)*6').postorder()
        