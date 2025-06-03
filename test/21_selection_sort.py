""" Selection Sort"""

def selection_sort(list1):
    n=len(list1)

    for i in range(n-1): #no need to run the loop n time n-1 is preferable
        min_index=i
        for j in range(i+1,n):
            if list1[j]<list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]


""" Driver Code """

l = [1,24,4,657,34,7,56,4,7,45,76]
selection_sort(l)
print(l)