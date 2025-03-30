"""Problem 1:
    Matching opening and closing tags"""

class Stack(object):
    def __init__(self):
        self.stk = []
    
    def push(self, data):
        self.stk.append(data)
        
    def pop(self):
        if len(self.stk) <= 0:
            raise IndexError
        return self.stk.pop()
    
    def peek(self):
        if len(self.stk) <= 0:
            raise IndexError
        return self.stk[-1]
    
    def isEmpty(self):
        return len(self.stk) == 0
    
def checkSymbolBalance(input):
    symbolStack = Stack()
    for data in input:
        if data in ['(', '{', '[']:
            symbolStack.push(data)
        elif data in [')', ']', '}']:
            if symbolStack.isEmpty():
                return 1
            else:
                topSymbol = symbolStack.pop()
                if (topSymbol == '(') and (data != ')'):
                    return 1
                elif (topSymbol == '[') and (data != ']'):
                    return 1
                elif (topSymbol == '{') and (data != '}'):
                    return 1
    
    if not symbolStack.isEmpty():
        return False
    return True

sy = ['(', ')', '(', '[', ']']



"""Problem 2:
    changing infix expressions to postfix (reverse Polish expression)"""
    
class Stack2(object):
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1] 
    
    def isEmpty(self):
        return self.items == []
    
    def __str__(self):
        return str(self.items)
    
def infix2Postfix(infixExp):
    prec = {} # dictionary for precedence
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    
    tokenList = infixExp.split()

    operatorStack = Stack2()
    postfixList = []
    
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in str(list(range(10))):
            postfixList.append(token)
            
        elif token == '(':
            operatorStack.push(token)
        elif token == ')':
            temp = operatorStack.pop()
            while temp != ')':
                postfixList.append(temp)
                temp = operatorStack.pop()
        else:
            while not operatorStack.isEmpty() and (prec[operatorStack.peek()] >= prec[token]):
                postfixList.append(operatorStack.pop())
                
            operatorStack.push(token)
            
    while not operatorStack.isEmpty():
        postfixList.append(operatorStack.pop())
        
    return " ".join(postfixList)

"""Problem 3:
   Evaluating postfix expressions"""
   
def evaluatePostfix(Exp):
    stack = Stack2()
    tokenList = Exp.split()
    
    for token in tokenList:
        if token in str(list(range(10))):
            stack.push(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            temp = doMath(token, operand1, operand2)
            stack.push(temp)
            
    return stack.pop()

def doMath(operator, operand1, operand2):
    if operator == '*':
        return operand2 * operand1
    elif operator == '/':
        return operand2 / operand1
    elif operator == '-':
        return operand2 - operand1
    elif operator == '+':
        return operand2 + operand1
    
# print(evaluatePostfix("1 2 3 * + 5 -")) # answer 2

"""Problem 4:
    infix expression evaluation"""
    
def infixEvaluation(Exp):
    operatorStack = Stack2()
    operandStack = Stack2()
    tokenList = Exp.split()
    



"""Problem 5:
    getMinimum() function in O(1) time complexity"""
    
class SmartStack:
    def __init__(self):
        self.stack1 = []
        self.min = []
        
    def push(self, x):
        self.stack1.append(x)
        if not self.min or (x <= self.min[-1]):
            self.min.append(x)
        else:
            self.min.append(self.min[-1])
            
    def pop(self):
        self.min.pop()
        return self.stack1.pop()
    
    def getMinimum(self):
        return self.min[-1]
    
"""checking whether array of letter is palindrome"""
def isPalindrome(lst):
    i = 0
    j = len(lst) - 1
    while i < j and lst[i] == lst[j]:
        i += 1
        j -= 1
        
    if i == j:
        print("It is palindrome")
    else:
        print("it is not palindrome")
        
"""Implementing queue using two stacks"""
class Stack12(object):
    def __init__(self):
        self.stk = []
        
    def push(self, element):
        self.stk.append(element)
        
    def pop(self):
        if self.isEmpty():
            print("Attempting pop on empty stack")
            raise IndexError
        
        return self.stk.pop()
    
    def isEmpty(self):
        return self.stk == []
    
class Queue15(object):
    def __init__(self):
        self.pushStack = Stack12()
        self.popStack = Stack12()
        
    def enQueue(self, element):
        self.pushStack.push(element)
        
    def deQueue(self):
        if self.pushStack.isEmpty() and self.popStack.isEmpty():
            print("Attempting popping empty queue")
            raise IndexError
        
        if self.popStack.isEmpty():
            while not self.pushStack.isEmpty():
                self.popStack.push(self.pushStack.pop())
                
        return self.popStack.pop()
    
    def isEmpty(self):
        return self.popStack.isEmpty() and self.pushStack.isEmpty()

#time complexity pop() O(n), push O(1), space complexity O(n)

"""Queue implementation of stack"""
class Queue13(object):
    def __init__(self):
        self.queue = []
        
    def enQueue(self, element):
        self.queue.append(element)
        
    def deQueue(self):
        if self.queue == []:
            print("deQueue empty queue")
            raise IndexError
        
        temp = self.queue[0]
        self.queue.remove(temp)
        return temp
    
    def isEmpty(self):
        return self.queue == []
    
class Stack13(object):
    def __init__(self):
        self.queue1 = Queue13()
        self.queue2 = Queue13()
        
    def push(self, element):
        if self.queue1.isEmpty():
            self.queue2.enQueue(element)
        elif self.queue2.isEmpty():
            self.queue1.enQueue(element)
            
    def pop(self):
        if self.queue1.isEmpty() and self.queue2.isEmpty():
            print("popping empty stack")
            raise IndexError
        
        if not self.queue1.isEmpty():
            temp = self.queue1.deQueue()
            while not self.queue1.isEmpty():
                self.queue2.enQueue(temp)
                temp = self.queue1.deQueue()
        elif not self.queue2.isEmpty():
            temp = self.queue2.deQueue()
            while not self.queue2.isEmpty():
                self.queue1.enQueue(temp)
                temp = self.queue2.deQueue()
                
        return temp
    
    def isEmpty(self):
        return self.queue1.isEmpty() and self.queue2.isEmpty()
    
"""Span of a number array"""
class Stack21(object):
    def __init__(self):
        self.stk = []
        
    def push(self, element):
        self.stk.append(element)
        
    def pop(self):
        if not self.stk:
            print("popping empty stack")
            raise IndexError
        
        return self.stk.pop()
    
    def peek(self):
        if self.isEmpty():
            print("Peek an empty stack")
            raise IndexError
        
        return self.stk[-1]
    
    def isEmpty(self):
        return self.stk == []
    
def span(A):
    stk = [None] * len(A)
    for i in range(len(A)):
        j = 1
        while j <= i and A[i] > A[i - j]:
            j = j + 1
        stk[i] = j
        
    print(stk)

# time complexity of O(n^2) ----> a bit greedy algorithm

def spanImproved(A):
    spanStk = Stack21()
    spanArray = len(A) * [None]
    for i in range(len(A)):
        while not spanStk.isEmpty() and A[i] > A[spanStk.peek()]:
            spanStk.pop()
            
        if spanStk.isEmpty():
            p = -1
        else:
            p = spanStk.peek()
            
        spanArray[i] = i - p
        spanStk.push(i)
        
    print(spanArray)
        
# time complexity of O(n) --> because the nested loop is gonna be executed at most n times

def largestRectangleArea(height):
    stack = []; maxArea = 0; i = 0
    while i < len(height):
        if stack == []  or height[i] > height[stack[-1]]:
            stack.append(i)
        else:
            curr = stack.pop()
            width = i if stack == []  else (i - stack[-1] -1)
            maxArea = max(maxArea, height[curr] * width)
            i -= 1
        i += 1
        
    while stack:
        curr = stack.pop()
        width = i if stack == [] else (len(height) - stack[-1] - 1)
        maxArea = max(maxArea, width * height[curr])
        
    return maxArea

print(largestRectangleArea([3, 2, 5, 6, 1, 4, 4]))