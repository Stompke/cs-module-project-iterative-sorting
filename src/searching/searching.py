def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        print('\nindex', arr[i])
        print('target', target)
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = ( left + right ) // 2
        print('mid', arr[mid])
        if arr[mid] == target:
            print('target found', target)
            return mid
        if target > arr[mid]:
            print('discard left')
            # discard left
            left = mid+1
        if target < arr[mid]:
            print('discard right')
            # discard right
            right = mid-1

    return -1  # not found


my_arr=[1,2,5,6,6,6,6,6,7,8,9,11,13,14,16,18]
binary_search(my_arr, 5)