"""Queue Using List"""

class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
           return self.items.pop(0)
        else:
            raise IndexError("The Queue is Empty")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("The Queue is Empty")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("The Queue is Empty")
    def size(self):
        return len(self.items)
    
"""Driver Code"""
q1=Queue()
print(q1.is_empty())
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(7)
q1.enqueue(10)
print(q1.is_empty())

try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])

try:
    print(q1.get_rear())
except IndexError as e:
    print(e.args[0])

try:
    print(q1.dequeue())
except IndexError as e:
    print(e.args[0])