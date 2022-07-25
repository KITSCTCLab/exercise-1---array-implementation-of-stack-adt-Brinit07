import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        # Write code here
         if self.top==-1:
            print("Stack is empty")
        

    def is_full(self):
        # Write code here
        return self.top==self.n-1

    def push(self, data):
        if not self.is_full():
            # Write code here
            if self.isfull():
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            # Write code here
            if self.top==-1:
            print("Stack is not empty")

    def status(self):
        # Write code here
        for i in range (self.top+1):
            print(self.st[i])
        
        

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
