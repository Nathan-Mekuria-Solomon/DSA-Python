class Heap(object):
    def __init__(self):
        self.heap = []
        self.size = 0
        
    def parentIndex(self, i):
        return (i-1)//2
    
    def leftChildIndex(self, i):
        return 2*i + 1
    
    def rightChildIndex(self, i):
        return 2*i + 2
    
    def leftChild(self, i):
        if i*2 + 1 >= self.size:
            return -1
        return self.heap[2*i + 1]
    
    def rightChild(self, i):
        if i*2 + 2 >= self.size:
            return -1
        return self.heap[2*i + 2]
    
    def searchElement(self, itm):
        if self.size == 0:
            return -1
        i = 0
        while i < self.size:
            if self.heap[i] == itm:
                return i
            i += 1
            
    def getMinimum(self):
        return self.heap[0]
    
    def percolateDown(self, i):
        while 2*i + 1 < self.size:
            minimum = self.minChild(i)
            if self.heap[i] > self.heap[minimum]:
                temp = self.heap[i]
                self.heap[i] = self.heap[minimum]
                self.heap[minimum] = temp
            i = minimum
            
    def minChild(self, i):
        if 2*i + 2 >= self.size:
            return 2*i + 1
        else:
            if self.heap[2*i + 1] < self.heap[2*i + 2]:
                return 2*i + 1
            else:
                return 2*i + 2
            
    def percolateUp(self, i):
        while (i-1)//2 >= 0:
            if self.heap[i] < self.heap[(i-1)//2]:
                temp = self.heap[i]
                self.heap[i] = self.heap[(i-1)//2]
                self.heap[(i-1)//2] = temp
            i = (i-1)//2
    
    def deleteMin(self):
        if self.size == 0:
            return -1
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        
        if self.size != 0:
            self.percolateDown(0)
        
        return temp
    
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.percolateUp(self.size-1)
        
    def printOut(self):
        print(self.heap)
        
def kthMin(h, k):
    hTemp = Heap()
    count = 0
    item = h.getMinimum()
    hTemp.insert(item)
    
    while hTemp.size > 0:
        count += 1
        temp = hTemp.deleteMin()
        
        if count == k:
            return temp
        
        if h.leftChild(h.searchElement(temp)) != -1:
            hTemp.insert(h.leftChild(h.searchElement(temp)))
            
        if h.rightChild(h.searchElement(temp)) != -1:
            hTemp.insert(h.rightChild(h.searchElement(temp)))
                
h = Heap()
h.insert(1)
h.insert(20)
h.insert(5)
h.insert(100)
h.insert(12)
h.insert(18)
h.insert(16)
print(kthMin(h, 5))