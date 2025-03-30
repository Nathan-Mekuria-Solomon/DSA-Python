class MinHeap:
    def __init__(self):
        self.heapList = []
        self.size = 0
        
    def parent(self, index):
        return (index - 1)//2
    
    def leftChild(self, index):
        return (index * 2) + 1
    
    def rightChild(self, index):
        return (index * 2) + 2
    
    def getMin(self):
        return self.heapList[0]
    
    def percolateDown(self, i): 
       # only adjusts the smallest half tree
       # for overall fix, we need to implement d/t approach
       
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
            self.percolateDown(smallest)
        else: # I don't understand the purpose of this block
            if self.heapList[left] < self.heapList[right]:
                self.percolateDown(left)
            else:
                self.percolateDown(right)           
        
            
    def percolateUp(self, i):
        while (i - 1) // 2 >= 0: # prone to infinte loop and runtime error: adding "="
            if self.heapList[i] < self.heapList[(i-1)//2]:
                temp = self.heapList[(i-1)//2]
                self.heapList[(i-1)//2] = self.heapList[i]
                self.heapList[i] = temp
            i = (i-1)//2
            
    def deleteMin(self):
        if self.size == 0:
            print("Empty heap")
            raise IndexError
        elif self.size == 1:
            return self.heapList.pop()
        else:
            temp = self.heapList[0]
            self.heapList[0] = self.heapList[-1]
            self.heapList.pop()
            self.size -= 1
            self.percolateDown(0)
            return temp
        
    def deleteRand(self, index):
        if self.size <= index:
            print("Index out of bound")
            raise IndexError
        else:
            temp = self.heapList[index]
            self.heapList[index] = self.heapList[-1]
            self.heapList.pop()
            self.size -= 1
            self.percolateDown(index)
            return temp
        
    def insert(self, value):
        self.heapList.append(value)
        self.size += 1
        self.percolateUp(self.size - 1)
        
    def printList(self):
        print(self.heapList)
        
    def findMax(self):
        max = -1
        for i in range(self.size//2, self.size):
            if self.heapList[i] > max:
                max = self.heapList[i]
                
        return max
    
    def deleteIndex(self, index):
        if index >= self.size:
            print("index out of bound")
            raise IndexError
        
        temp = self.heapList[index]
        self.heapList[index] = self.heapList[self.size - 1]
        self.heapList.pop()
        self.size -= 1
        self.percolateDown(index)
        return temp
        
def heapOrder(A):
    heap = MinHeap()
    for i in A:
        heap.insert(i)
    
    while heap.heapList:
        temp = A[0]
        A.append(heap.deleteMin())
        A.pop(temp)
        
    print(A)
    
# deleting a random element
def deleteRandom(minheap, value):
    valIndex = -1
    for i in range(0, len(minheap.heapList)-1):
        if minheap.heapList[i] == value:
            valIndex = i
            break
        
    if valIndex != -1:
        minheap.deleteRand(valIndex)
        
    return minheap.heapList

def mergingHeaps(heap1, heap2):
    for val in heap2.heapList:
        heap1.insert(val)
        
    heap1.printList()

example = MinHeap()
example.insert(10)
example.insert(1)
example.insert(13)
example.insert(2)
example.insert(14)
example.insert(9)
example.insert(5)
deleteRandom(example, 10)
example2 = MinHeap()
example2.insert(1)
example2.insert(3)
example2.insert(4)
example2.insert(1)
example2.insert(7)
example2.insert(2)

mergingHeaps(example, example2)

        
