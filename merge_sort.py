import math

# initializing a list
list = [5,2,4,7,1,3,2,6]

def merge(list, start, mid, end):
    print("List is:", list)
    print("Start is:", start)
    print("Mid is:", mid)
    print("End is:", end)
    # computing length of sublists
    n1 = mid - start + 1
    n2 = end - mid

    print("n1:", n1)
    print("n2:", n2)

    # Extra position to hold infinity value
    left_list = [None] * (n1 + 1)
    right_list = [None] * (n2 + 1)

    # copying the value to left and right lists
    for i in range(0, n1):
        left_list[i] = list[start + i]

    for j in range(0, n2):
        right_list[j] = list[mid + j + 1]

    left_list[n1] = math.inf
    right_list[n2] = math.inf

    
    print("Left List:", left_list)
    print("Right List", right_list)

    # sorting logic
    i = 0 
    j = 0
    for k in range (start, end + 1):
        if left_list[i] <= right_list[j]:
            list[k] = left_list[i]
            i += 1

        else:
            list[k] = right_list[j]
            j += 1



def merge_sort(list,start,end):
    if start < end:
        # finding the mid point
        mid = math.floor((start + end)/2)
        # sorting recursively
        merge_sort(list, start, mid) 
        merge_sort(list, mid + 1, end)
        # merging recursively
        merge(list, start, mid, end)

print("Length of list is:", len(list))
merge_sort(list, 0, len(list) - 1)
print("Sorted List is:", list)