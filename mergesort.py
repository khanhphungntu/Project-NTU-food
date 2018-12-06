 
def merge(left, right):

    result_list = []

    
    while left and right:
        if left[0] < right[0]:
            result_list.append(left[0])
            left.pop(0)
        else:
            result_list.append(right[0])
            right.pop(0)

    if left:
        result_list.extend(left)
    else:
        result_list.extend(right)
    
    return result_list


def mergesort(list_of_items):
    length = len(list_of_items)


    if length < 2:
        return list_of_items
    left = list_of_items[:length // 2]   
    right = list_of_items[length // 2:]  

    # merge sort left and right list recursively
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)



