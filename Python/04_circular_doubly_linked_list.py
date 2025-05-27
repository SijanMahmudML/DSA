"""Circular Doubly Linked List"""

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(item=data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        n=Node(item=data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
    def search(self,data):
        temp=self.start
        if self.is_empty():
            return None
        while temp.next is not self.start:
            if temp.item==data:
                return temp
            temp=temp.next 
        if temp.item==data:
            return temp
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            temp.next.prev=n
            temp.next=n
    def print_list(self):
        temp=self.start
        if not self.is_empty():
            while temp.next is not self.start:
                print(temp.item,end=" ")
                temp=temp.next
            print(temp.item,end=" ")
    def delete_first(self):
        if not self.is_empty():
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.next.prev=self.start.prev
                self.start.prev.next=self.start.next
                self.start=self.start.next
    def delete_last(self):
        if not self.is_empty():
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev
    def delete_item(self,data):
        if not self.is_empty():
            if self.start.item==data:
                self.delete_first()
            else:
                temp=self.start.next
                while temp is not self.start:
                    if temp.item==data:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                    temp=temp.next
    def __iter__(self):
        return CDLLIterator(self.start)
    
class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data = self.current.item
        self.current=self.current.next
        return data







#Driver code
mylist=CDLL()
mylist.insert_at_start(10)
mylist.insert_at_start(0)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(30),35)
# mylist.delete_first()
# mylist.delete_last()
mylist.delete_item(30)

# mylist.print_list()

for i in mylist:
    print(i,end=" ")
    







