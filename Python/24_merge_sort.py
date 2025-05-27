""" Merge Sort """

def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        leftside=list1[:mid]
        rightside=list1[mid:]

        merge_sort(leftside)
        merge_sort(rightside)

        i=j=k=0
        while i<len(leftside) and j<len(rightside):
            if leftside[i]<rightside[j]:
                list1[k]=leftside[i]
                i+=1
            else:
                list1[k]=rightside[j]
                j+=1
            k+=1
        
        while i<len(leftside):
            list1[k]=leftside[i]
            i+=1
            k+=1
        
        while j<len(rightside):
            list1[k]=rightside[j]
            j+=1
            k+=1


""" Driver Code """

l=[2,3,45,56,1,54,7,86,5,4,8]
merge_sort(l)
print(l)
