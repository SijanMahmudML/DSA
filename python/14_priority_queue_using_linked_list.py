"""Priority Queue using Linked List"""

class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next

class PriorityQueue:
    def __init__(self):
        self.start=None
        self.item_count=0
    def is_empty(self):
        return self.start==None
    def push(self,data,priority):
        n=Node(data,priority)
        if self.is_empty() or priority < self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next is not None and temp.next.priority <= priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count +=1
    def pop(self):
        if self.is_empty():
            raise IndexError("PriorityQueue is Empty")
        deleted_item=self.start.item
        self.start=self.start.next
        self.item_count -=1
        return deleted_item
    def size(self):
        return self.item_count
    
"""Driver Code"""
p1=PriorityQueue()
p1.push(3,1)
p1.push(45,5)
p1.push(451,2)
p1.push(30,1)
p1.push(7,3)
p1.push(60,6)

print(p1.pop())
print(p1.pop())
print(p1.pop())
print(p1.pop())
print(p1.pop())
print(p1.pop())
