# def factorial(n):
#     if n == 0: return 1
#     return n*factorial(n-1)

# print(factorial(5))

def hanoi(n, start, end):
    """
    number of steps required to move n disks to destination
    >>>hanio(2, 1, 3)
    1->2
    1->3
    2->
    """
    
    if n == 1: pm(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n-1, start, other)
        pm(start, end)
        hanoi(n-1, other, end)

def pm(start, end):
    """
    print the starting and ending of the top disk
    """
    print(start, "->", end)
    

def isSorted(A):
    if len(A) == 1:
        return True
    return A[0] <= A[1] and isSorted(A[1:])

#time and space complexity O(n)