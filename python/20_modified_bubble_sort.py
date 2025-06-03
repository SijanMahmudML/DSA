""" Modified Bubble Sort"""

def modified_bubble_sort(data_list):
    for r in range(1,len(data_list)):
        flag=False
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag=True
        if not flag:
            break

""" Driver Code"""

l = [12,34,56,34,65,767,34,56,3,6,87,56,8,98]
modified_bubble_sort(l)
print(l)