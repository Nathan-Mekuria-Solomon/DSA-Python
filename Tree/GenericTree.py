class GenericNode(object):
    def __init__(self, data = None):
        self.data = data
        self.firstChild = None
        self.nextSibling = None
        
"""Problem 38 - implementation of generic tree:
    adding and nth child  and print path from root to leaves"""
    
import string
class GenericTree(object):
    def __init__(self, parent, data = None):
        self.data = data
        self.parent = parent
        self.childList = []
        
        if parent == None:
            self.birthOrder =  0
        else:
            self.birthOrder = len(parent.childList)
            parent.childList.append(self)
            
    def nthChild(self, n):
        if n >= len(self.childList):
            raise IndexError
        
        return self.childList[n]
    
    def nChildren(self):
        return self.childList
    
    def fullPath(self):
        parent = self.parent
        kid = self
        result = []
        
        while parent:
            result.insert(0, kid.birthOrder)
            parent, kid = parent.parent, parent
            
        return result
    
    def nodeId(self):
        fullPath = self.fullPath()
        return NodeId(fullPath)
    
class NodeId(object):
    def __init__(self, path):
        self.path = path
        
    def __str__(self):
        L = map(str, self.path)
        return string.join(L, '/')
    
    
def addTree(root):
    if root == None:
        return 0
    
    return root.data + addTree(root.firstChild) + addTree(root.nextSibling) 
    
# Examples:
one = GenericNode(1)
two = GenericNode(2)
three = GenericNode(3)
four = GenericNode(4)
five = GenericNode(5)
six = GenericNode(6)
seven = GenericNode(7)
eight = GenericNode(8)
one.firstChild = two
two.nextSibling = three
three.nextSibling = four
four.firstChild = six
four.nextSibling = five
five.firstChild = eight
six.nextSibling = seven

def maxDepth(p): # tree as a list
    maxdepth = -1
    
    for i in range(len(p)):
        count = -1
        j = i
        while p[j] != -1:
            count += 1
            j = p[j]
            
        if count > maxdepth:
            maxdepth = count
            
    return maxdepth

p = [-1, 0, 1, 6, 6, 0, 0, 2, 7, 8]
print(maxDepth(p))
