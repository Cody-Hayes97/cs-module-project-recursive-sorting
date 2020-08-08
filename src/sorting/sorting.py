# # TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(left, right):
#     result = []
#     left_pointer = right_pointer = 0

#     while left_pointer < len(left) and right_pointer < len(right):
#         if left[left_pointer] < right[right_pointer]:
#             result.append(left[left_pointer])
#             left_pointer += 1
#         else:
#             result.append(right[right_pointer])
#             right_pointer += 1
#         result.extend(left[left_pointer:])
#         result.extend(right[right_pointer:])
#         return result
#     # elements = len(arrA) + len(arrB)
#     # merged_arr = [0] * elements

   


   

# # TO-DO: implement the Merge Sort function below recursively
# def merge_sort(arr):
#     # Your code here
#     if len(arr) <= 1:
#         return arr
#     mid = int(len(arr) / 2)
#     left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
#     return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)