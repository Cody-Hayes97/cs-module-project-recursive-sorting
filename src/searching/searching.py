# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, low, high):
    # Your code here
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, low, mid-1)
        else:
            return binary_search(arr, target, mid+1, high)
        

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, 8, -9, 9))
