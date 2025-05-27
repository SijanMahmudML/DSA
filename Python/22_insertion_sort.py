""" Insertion Sort """

def insertion_sort(list1):
    n=len(list1)
    for i in range(1,n):
        temp=list1[i]
        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=temp


""" Driver Code """

l=[50,20,37,91,64,18,43,59,72,81,35,56,67]

insertion_sort(l)
print(l)
