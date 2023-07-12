"""" Count the number of elements that have at least 1 elements greater than itself"""

""" Approach - 1) find the max value in array
               2) count the occurrence of max_value
               3) subtract with length of the array (len(arr) - count) """
def arr_greater(arr):
    size = len(arr)
    max_value = float("-inf")
    for i in range(size):
        if max_value < arr[i]:
            max_value = arr[i]
    count = 0

    for j in range(size):
        if max_value == arr[j]:
            count += 1

    return size - count

array = list(map(int, input("Enter the elements of array : ").split()))
print(arr_greater(array))