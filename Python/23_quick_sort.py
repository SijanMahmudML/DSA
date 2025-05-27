""" Quick Sort """

def quick_sort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot=list1[0]
        lesser=[x for x in list1[1:] if x<=pivot]
        greater=[x for x in list1[1:] if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
    

""" Driver Code """

l = [58,11,72,68,41,25,18,37,44,80]
l = quick_sort(l)
print(l)