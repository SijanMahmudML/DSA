'''Circular Linked List'''

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next 

class CLL:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last==None
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp is not self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
    def print_list(self):
        if self.last is not None:
            temp=self.last.next
            while temp is not self.last:
                    print(temp.item,end=' ')
                    temp=temp.next
            print(temp.item)
    def delete_first(self):
        if self.last is None:
            pass
        elif self.last.next is self.last:
            self.last=None
        else:
            self.last.next=self.last.next.next
    def delete_last(self):
        temp=self.last
        if self.last is None:
            pass
        elif temp.next is self.last:
            self.last=None
        else:
            while temp.next is not self.last:
                temp=temp.next
            temp.next=temp.next.next
            self.last=temp
    def delete_item(self,data):
        if self.last is None:
            pass
        elif self.last.next == self.last:
            if self.last.item==data:
                self.last=None
        else:
            if self.last.next.item==data:
                self.delete_first()
            else:
                temp=self.last.next  
                while temp is not self.last:
                    if temp.next == self.last:
                        if temp.next.item==data:
                            self.delete_last()
                            break
                    if temp.next.item==data:
                        temp.next==temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        if self.last==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)

class CLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data = self.current.item
        self.current=self.current.next
        return data
            
            
# Driver code:

mylist=CLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_at_last(50)
mylist.insert_after(mylist.search(50),32)
# mylist.delete_first()
# mylist.delete_last()
# mylist.delete_item(50)

for i in mylist:
    print(i,end=" ")


# mylist.print_list()

    