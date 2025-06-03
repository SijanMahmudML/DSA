"""Priority Queue using List"""

class PriorityQueue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data,priority):
        index=0
        while index < len(self.items) and self.items[index][1] <= priority:
            index +=1
        self.items.insert(index,(data,priority))
    def pop(self):
        if self.is_empty():
            raise IndexError("PriorityQueue is Empty")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)

"""Driver Code"""

pq1=PriorityQueue()
pq1.push("hi",1)
pq1.push("hello",0)
pq1.push("bye",5)
pq1.push("bye",8)
pq1.push("tata",1)

print(pq1.size())
print(pq1.is_empty())

while not pq1.is_empty():
    print(pq1.pop())

print(pq1.size())
print(pq1.is_empty())