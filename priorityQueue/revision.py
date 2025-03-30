class MinHeap(object):
    def __init__(self):
        self.heapList = []
        self.size = 0
        
    def parent(self, index):
        if index == 0:
            print('You are accessing the root node')
            raise IndexError
        else:
            return self.heapList[(index-1) // 2]
        
    def parentIndex(self, index):
        if (index-1)//2 < 0:
            return -1
        return (index-1)//2
        
    def leftChild(self, index):
        if self.size <= index*2 +1:
            return -1
        return self.heapList[(index*2)+1]
    
    def rightChild(self, index):
        if self.size <= index*2 +2:
            return -1
        return self.heapList[index*2 +2]
    
    def getMin(self):
        if self.size == 0:
            print("Attempting finding min of empty PQ")
            raise IndexError
        
        return self.heapList[0]
    
    def percolateDown(self, i):
        # iteratively
        while (i * 2 + 1) <= self.size:
            minChildIndex = self.minChild(i)
            if self.heapList[i] > self.heapList[minChildIndex]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[minChildIndex]
                self.heapList[minChildIndex] = temp
            i = minChildIndex
            
    def minChild(self, i):
        if i*2 +2 > self.size:
            return i*2 + 1
        else:
            if self.heapList[i*2 + 1] > self.heapList[i*2 + 2]:
                return i*2 + 2
            else:
                return i*2 + 1
            
    def percolateDown2(self, i): 
        # tried to approach recursively 
        # but seems like there is logical error in the implementation
        # need for a test run to confirm
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left >= self.size:
            return
        
        if left < len(self.heapList) and self.heapList[left] < self.heapList[smallest]:
            smallest = left
            
        if right < len(self.heapList) and self.heapList[right] < self.heapList[smallest]:
            smallest = right
        
        if smallest != i:
            self.heapList[i], self.heapList[smallest] = self.heapList[smallest], self.heapList[i]
            self.percolateDown2(smallest)
        else:
            if self.heapList[left] < self.heapList[right]:
                self.percolateDown2(left)
            else:
                self.percolateDown2(right)
              
    def percolateUp(self, i):
        # prone to runtime error
        # and infinte loop
        #because of indexing
        
        parent = self.parentIndex(i)
        while parent > -1:
            if self.heapList[i] < self.heapList[parent]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[parent]
                self.heapList[parent] = temp
            parent = self.parentIndex(parent)
            
    def deleteMin(self):
        temp = self.heapList[0]
        self.heapList[0] = self.heapList[self.size - 1]
        self.heapList.pop()
        self.size -= 1
        self.percolateDown2(0)
        return temp
    
    def insert(self, element):
        self.heapList.append(element)
        self.size += 1
        self.percolateUp(self.size - 1)
        
    def buildHeap(self, arr):
        self.heapList = arr
        self.size = len(arr)
        
        parentLast = self.parentIndex(self.size - 1)
              
        while parentLast > 0:
            self.percolateDown2(parentLast)
            parentLast -= 1
        
    # only scan leaves to find the maximum element
    # O(n/2) = O(n) ---> a bit efficient (seemingly)        
    def findMax(self):
        lst = self.size - 1
        fstLeaf = (lst + 1)//2
        
        max = -1
        for i in range(fstLeaf, self.size):
            if self.heapList[i] > max:
                max = self.heapList[i]
                
        return max
    
    def deleteI(self, i):
        if i >= self.size:
            print("Index out of bound")
            raise IndexError
        
        temp = self.heapList[i]
        self.heapList[i] = self.heapList[self.size - 1]
        self.heapList.pop()
        self.percolateDown2(i)
        
        return temp
            
# test
test1 = MinHeap()
test1.buildHeap([1, 4, 3, 7, 9, 2, 8, 20, 10, 2, 2])
test1.insert(1)
print(test1.heapList)
test1.deleteI(3)
print("After deletion: ", test1.heapList)