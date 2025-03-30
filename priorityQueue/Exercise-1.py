# sliding window problem using double ended queue or deque
#  O(n)

# create a deque
# for len(lst)
# delete elements smaller that the indexed
# append the indexed one
# if index reached the size append the biggest to result
# if max is out of the window, delete it

from collections import deque


def maxWindow(lst, w): # lst->list input, w- width of the window
    D = deque()
    res = []
    
    for i in range(len(lst)):
        while D and D[-1][0] <= lst[i]:
            D.pop()
            
        D.append((lst[i], i + w -1))
        
        if i >= w - 1:
            res.append(D[0][0])
            if i == D[0][1]:
                D.popleft()
                
    return res

# number of unique three letter strings
def uniqueString(s):
    count = 0
    temp = []
    for letter in s:
        temp.append(letter)
        if len(temp) > 3:
            temp = temp[1:]
            
        if len(temp) == 3:
            if len(set(temp)) == 3:
                count += 1
                
    return count

# minHeap
class Solution(object):
    def __init__(self):
        self.heap = []

    def percolateDown(self, i):
        while i*2 + 1 < len(self.heap):
            min = self.minChild(i)
            if self.heap[min] < self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[min]
                self.heap[min] = temp

            i = min

    def minChild(self, i):
        if i*2 + 2 >= len(self.heap):
            return i*2 + 1
        else:
            if self.heap[i*2+1] < self.heap[i*2 + 2]:
                return i*2 + 1
            else:
                return i*2 + 2

    def deleteMin(self):
        if self.heap == []:
            return
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.percolateDown(0)
        print(temp)
        return temp

    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        fnl = []
        self.heap = nums
        self.percolateDown(0)
        for i in range(len(nums)//2):
            temp = []
            temp.append(self.deleteMin())
            temp.append(self.deleteMin())
            fnl.append(temp.pop())    
            fnl.append(temp.pop())
        
        return fnl
    
sln = Solution()
sln.numberGame([18,26,37,46,13,33,39,1,37,16])