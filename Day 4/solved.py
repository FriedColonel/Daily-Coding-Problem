def quicksort(arr):
    if len(arr) < 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# time complexity: O(n)
def find(arr):
    result = 0
    for x in arr:
        if x <= 0:
            del x
            continue
        if x - result == 1:
            result = x
        if x - result > 1:
            break
    return result + 1

arr = [3, 4, -1, 1]
print(find(quicksort(arr)))
# print(quicksort(arr))