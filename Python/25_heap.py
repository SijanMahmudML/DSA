""" Heap Data Structure """

class Heap:
    def __init__(self):
        self.heap=[]
    def createHeap(self,list1):
        for i in list1:
            self.insert(i)
    def insert(self,item):
        self.heap.append(item)

        temp=len(self.heap)-1
        while temp>0 and self.heap[temp] > self.heap[(temp-1)//2]:
            self.heap[temp],self.heap[(temp-1)//2]=self.heap[(temp-1)//2],self.heap[temp]
            temp=(temp-1)//2
    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        return self.heap[0]
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        if len(self.heap) == 1:
            return self.heap.pop()
        
        top=self.heap[0]
        self.heap[0]=self.heap.pop()

        index=0
        left_index=(index*2)+1
        right_index=(index*2)+2

        while right_index < len(self.heap):
            if self.heap[left_index] > self.heap[right_index]:
                if self.heap[left_index] > self.heap[index]:
                    self.heap[left_index],self.heap[index]=self.heap[index],self.heap[left_index]

                    index = left_index
                    left_index=(index*2)+1
                    right_index=(index*2)+2
                else:
                    break
            else:
                if self.heap[right_index] > self.heap[index]:
                    self.heap[right_index],self.heap[index]=self.heap[index],self.heap[right_index]

                    index= right_index
                    left_index=(index*2)+1
                    right_index=(index*2)+2
                else:
                    break
        
        while left_index < len(self.heap):
            if self.heap[left_index] > self.heap[index]:
                self.heap[left_index],self.heap[index]=self.heap[index],self.heap[left_index]

                index = left_index
                left_index=(index*2)+1
                right_index=(index*2)+2
            else:
                break
        
        return top
    def heapSort(self,list1):
        self.createHeap(list1)
        sortedList=[]

        for i in range(len(self.heap)):
            sortedList.insert(0,self.delete())
        return sortedList




class EmptyHeapException(Exception):
        def __init__(self,msg="Empty Heap"):
            self.msg=msg
        def __str__(self):
            return self.msg


""" Driver Code """

h=Heap()
# h.createHeap([40,70,10,90,60,30,50,20,80])
# print(h.delete())
# print(h.delete())
# print(h.delete())
# print(h.heap)

print(h.heapSort([40,70,10,90,60,30,50,20,80,3,456,567]))

