"""Queue using Singly Linked List"""

# Singly Linked List Node:
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

# Queue Data Structure :
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.item_count==0
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count +=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("The Queue is Empty")
        else:
            deleted_item=self.front.item
            if self.item_count==1:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next
            self.item_count -=1
            return deleted_item
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("The Queue is Empty")
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("The Queue is Empty")
    def size(self):
        return self.item_count
    
"""Driver Code"""
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
print(q1.size())
print(q1.get_front())
print(q1.get_rear())
print(q1.dequeue())
print(q1.get_rear())
print(q1.get_front())
print(q1.size())
        