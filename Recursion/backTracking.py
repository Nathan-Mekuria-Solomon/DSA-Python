# Generating binary strings of n

# adding x on each element of array
def appendFront(x, L):
    return([x + element for element in L])

def bitStrings(n):
    """
    recursive calling by fixing the first element
    base case when  n == 1
    """
    if n == 0: return []
    if n == 1: return ['0', '1']
    else:
        return(appendFront('0', bitStrings(n-1)) + appendFront('1', bitStrings(n-1)))

# method 2

def bitString2(n):
    if n == 0: return []
    if n == 1: return ['0', '1']
    return [digit + bitstring for digit in bitString2(1) for bitstring in bitString2(n - 1)]

#Generate all the strings of length n drawn from 0... k-1

def rangeList(k):
    """fill an array from 0, to k-1"""
    result = []
    for i in range(k):
        result.append(str(i))
    
    return result

def binaryString(n, k):
    if n == 0: return []
    if n == 1: return rangeList(k)
    result = []
    for digit in rangeList(k):
        for bitstring in binaryString(n-1, k):
            result.append(digit + bitstring)
    return result
        
def binaryString2(n, k):
    if n == 0: return []
    if n == 1: return rangeList(k)
    return [digit + bitstring for digit in binaryString2(1, k) for bitstring in binaryString2(n-1, k)]
       
"""finding the number of islands when 1s represent a land 0s water and lands form 1 island
if they are connected in adjecent (only vertically and horizontally), not diagonally"""

def island(A):
    row = len(A)
    if row == 0: # empty list
        return 0
    column = len(A[0])
    num = 0
    
    #iterate for all cells
    for i in range(row):
        for j in range(column):
            if A[i][j] == 1:
                mark(A, i, j, row, column)
                num += 1
    return num

def mark(A, i, j, row, column):
    if(i < 0 or j < 0 or i >= row or j >= column or A[i][j] != 1):
        return
    A[i][j] = 2
    
    #recursive call for adjecent cells
    mark(A, i-1, j, row, column)
    mark(A, i, j-1, row, column)
    mark(A, i+1, j, row, column)
    mark(A, i, j+1, row, column)
    
"""Finding the length of connected cells of 1s (region) in a matrix of 1s and 0s
    the two cells are said to be connected if they are adjacent to each other horizontally, vertically or
    diagonally. Find the largest region"""
    
# def getVal(A, i, j, L, H):
#     if(i < 0 or j < 0 or i >= L or j >= H):
#         return 0
#     else:
#         return A[i][j]

# def findMaxBlock(A, r, c, L, H, size):
#     global maxsize
#     global arr
#     if(r >= L or c >= H):
#         return
#     arr[r][c] = 1
#     size += 1
#     if(size > maxsize):
#         maxsize = size
#     #search for the eight direction
#     direction = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
#     for i in range(0,7):
#         newr = r + direction[i][0]
#         newc = c + direction[i][1]
#         val = getVal(A, newr, newc, L, H)
#         if(val > 0 and (arr[newr][newc] == 0)):
#             findMaxBlock(A, newr, newc, L, H, size)
    
#     arr[r][c] = 0
    
# def getMax(A, rmax, colmax):
#     global maxsize
#     global size
#     global arr
#     for i in range(0, rmax):
#         for j in range(0, colmax):
#             if(A[i][j] == 1):
#                 findMaxBlock(A, i, j, rmax, colmax, 0)
#     return maxsize

# z = [[1,1,0,0,0], [0,1,1,0,0], [0,0,1,0,1],[1,0,0,0,1],[0,1,0,1,1]]
# rmax = 5
# colmax = 5
# maxsize = 0
# size = 0
# arr = rmax*[colmax*[0]]
# print(getMax(z, rmax, colmax))

def getval(A, i, j, L, H):
    if(i < 0 or i >= L or j < 0 or j >= H):
        return 0
    else:
        return A[i][j]
    
def findMaxBlock(A, r, c, L, H, size):
    global maxsize
    global entarr
    if (r >= L or c >= H):
        return
    entarr[r][c] = 1
    size += 1
    if (size > maxsize):
        maxsize = size
    direction = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
    for i in range(0,7):
        newi = r + direction[i][0]
        newj = c + direction[i][1]
        val = getval(A, newi, newj, L, H)
        if(val > 0 and (entarr[newi][newj] == 0)):
            findMaxBlock(A, newi, newj, L, H, size)
    entarr[r][c] = 0
    
def getMaxOnes(A, rmax, colmax):
    global maxsize
    global size
    global entarr
    for i in range(0, rmax):
        for j in range(0, colmax):
            if (A[i][j] == 1):
                findMaxBlock(A, i, j, rmax, colmax, 0)
    return maxsize

zarr = [[1,1,0,0,0],[0,1,1,0,0],[0,0,1,0,1],[1,0,0,0,1],[0,1,0,1,1]]
rmax = 5
colmax = 5
maxsize = 0
size = 0
entarr = rmax * [colmax * [0]]
print("Number of maximum 1s are: ")
print(getMaxOnes(zarr, rmax, colmax))
    