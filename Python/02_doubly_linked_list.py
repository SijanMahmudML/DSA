'''Doubly Linked List'''
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            n=Node(temp,data)
            temp.next=n
        else:
            n=Node(None,data)
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def delete_first(self):
        temp=self.start
        if temp is None:
            pass
        elif temp.next is None:
            self.start=None
        else:
            temp.next.prev=None
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
            if temp.item==item:
                temp.next.prev=None
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==item:
                        if temp.next.next is not None:
                            temp.next.next.prev=temp
                        temp.next=temp.next.next
                        break
                    temp=temp.next

    # Replacing DLLIterator logic here inside DLL:
    def __iter__(self):
        self.current=self.start
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    
    # def __iter__(self):
    #     return DLLIterator(self.start)
    
# class DLLIterator:
#     def __init__(self,start):
#         self.current=start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         data=self.current.item
#         self.current=self.current.next
#         return data
        

'''Driver Code'''
myList=DLL()
myList.insert_at_last(50)
myList.insert_at_start(40)
myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_after(myList.search(50),60)
# myList.delete_first()
# myList.delete_last()
myList.delete_item(10)
# myList.print_list()

for i in myList:
    print(i,end=' ')


        
