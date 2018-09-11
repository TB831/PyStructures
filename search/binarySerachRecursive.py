def binarSearchRecursive(arr, left, right, value):
    if (left > right): # Edge case
        return False

    mid = int(left + ((right - left)/ 2))
    if arr[mid] == value:
        return True
    elif value < arr[mid]:
        return binarSearchRecursive(arr, left, mid - 1, value)
    else:
        return binarSearchRecursive(arr, mid + 1, right, value)

#Test Arrays
arr = [2, 3, 4, 10, 40]
binarSearchRecursive(arr, 0, len(arr)-1, 3)
