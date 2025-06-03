"""Stack By Extending SLL"""

#Singly Linked List
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def delete_first(self):
        temp=self.start
        if temp is not None:
            self.start=temp.next
    def delete_last(self):
        temp=self.start
        if temp is None:
            pass
        elif temp.next is None:
            self.start=None
        else:
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,item):
        temp=self.start
        if temp is None:
            pass
        elif temp.next is None:
            if temp.item==item:
                self.start=None
        else:
            if self.start.item==item:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==item:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

#Stack 
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.item_count +=1
    def pop(self):
        if not self.is_empty():
            deleted_item=self.start.item
            self.delete_first()
            self.item_count -=1
            return deleted_item
        else:
            raise IndexError("The Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("The Stack is Empty")
    def size(self):
        return self.item_count
    
"""Driver Code"""

s1= Stack()
s1.push(5)
s1.push(50)
s1.push(60)
s1.push(40)
s1.push(70)
print(s1.size())
print(s1.pop())
print(s1.peek())
print(s1.size())