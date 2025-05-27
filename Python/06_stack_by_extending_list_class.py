"""Stack By Extending List"""

class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self)

    def insert(self, index, object):
        raise AttributeError("No attribute 'insert' is stack")
    
"""Driver Code"""

myStack=Stack()
myStack.push(2)
myStack.push(5)
myStack.push(10)
myStack.push(20)
myStack.push(30)
print(myStack.size())
print(myStack.peek())
print(myStack.pop())