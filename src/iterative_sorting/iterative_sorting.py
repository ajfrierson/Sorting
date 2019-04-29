# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        print(f"LOOP {i}")
        print(f"{arr}")
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
        # from the i'th position to the end of the array if j is smaller than the current value then j is the current smallest index
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        print(f"SMALLEST ELEMENT: {arr[smallest_index]}")


        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp



    return arr


# TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):
#     for n in range(0,len(arr)-1):
#       if arr[n] > arr[n+1]:
#         unsorted = True
#         arr[n], arr[n+1] = arr[n+1], arr[n]
#       if n == len(arr-1) and unsorted:
#         unsorted = False
#         n = 0
def bubble_sort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr