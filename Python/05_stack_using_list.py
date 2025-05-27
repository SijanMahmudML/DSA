"""Stack Using List"""

class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self.items)
    
"""Driver Code"""

myStack=Stack()
myStack.push(4)
myStack.push(6)
myStack.push(5)
myStack.push(8)
myStack.push(10)
print(myStack.pop())
print(myStack.peek())
print(myStack.size())
print(myStack.is_empty())