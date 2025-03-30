import math
import random

class Node:
    def __init__(self, data, level = 0):
        self.data = data
        self.next = [None] * level
        
    def __str__(self):
        return f"Node[{self.data, len(self.next)}]"
    
    __repr__ = __str__  # Didnt understand fully
    
class SkipLink(object):
    def __init__(self, maxLevel = 8):
        self.maxLevel = maxLevel
        n = Node(None, self.maxLevel)
        self.head = n
        self.verbose = False
        
    def randomLevel(self, maxLevel):
        level = random.randint(1, maxLevel - 1)
        return maxLevel -level
    
    def    