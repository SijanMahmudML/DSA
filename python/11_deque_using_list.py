"""Deque Using List"""

class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rear(self,data):
        self.items.append(data)
    def delete_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("The Deque is Empty")
    def delete_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("The Deque is Empty")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("The Deque is Empty")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("The Deque is Empty")
    def size(self):
        return len(self.items)
        
"""Driver Code"""

d1=Deque()
d1.insert_front(10)
d1.insert_rear(20)
d1.insert_front(30)
d1.insert_rear(40)
d1.delete_front()
d1.delete_rear()

print(d1.get_front())
print(d1.get_rear())
print(d1.size())