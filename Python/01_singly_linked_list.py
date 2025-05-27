'''Singly Linked List'''

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
    def __iter__(self):
        return SLLIterator(self.start)

class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data



#Driver Code
"""myList=SLL()
myList.insert_at_last(10)
myList.insert_at_start(20)
myList.insert_at_last(30)
myList.insert_at_last(40)
myList.insert_after(myList.search(40),50)
myList.insert_at_start(60)
# myList.delete_item(50)
for x in myList:
    print(x,end=" ")

# myList.print_list()

# print(myList.search(40))"""