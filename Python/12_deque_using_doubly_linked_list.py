"""Deque Using Doubly Linked List"""

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.item_count==0
    def insert_front(self,data):
        n=Node(None,data,self.front)
        if not self.is_empty():
            self.front.prev=n
        else:
            self.rear=n
        self.front=n
        self.item_count +=1
    def insert_rear(self,data):
        n=Node(self.rear,data)
        if not self.is_empty():
            self.rear.next=n
        else:
            self.front=n
        self.rear=n
        self.item_count +=1
    def delete_front(self):
        if self.is_empty():
            raise IndexError("The Deque is Empty")
        elif self.front.next==None:   
            self.front=None
            self.rear=None
        else:
            self.front.next.prev=None
            self.front=self.front.next
        self.item_count -=1
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("The Deque is Empty")
        elif self.front.next==None:
            self.front=None
            self.rear=None
        else:
            self.rear.prev.next=None
            self.rear=self.rear.prev
        self.item_count -=1
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("The Deque is Empty")
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("The Deque is Empty")
    def size(self):
        return self.item_count

"""Driver Code"""
d1=Deque()
d1.insert_front(30)
d1.insert_front(10)
d1.insert_front(5)
d1.insert_rear(20)

print(d1.size())
print(d1.get_front())
print(d1.get_rear())

d1.delete_front()
d1.delete_rear()

print(d1.is_empty())
print(d1.size())
        
