arr = [10,15,3,7]
k = 17
dict = {}

# for i in range(len(arr)):
#     sum = k - arr[i]
#     if sum in dict:
#         print("Pair found: {} and {}".format(sum, arr[i]))
#     else:
#         dict[arr[i]] = i

def quick_sort(Arr):
    if len(Arr) <= 1:
        return Arr
    else:
        pivot = Arr[len(Arr)//2]
        left = [i for i in Arr if i < pivot]
        middle = [i for i in Arr if i == pivot]
        right = [i for i in Arr if i > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def find(arr, sum):
    global dict
    for i in range(len(arr)):
        Tsum = sum - arr[i]
        if Tsum in dict:
            print("Pair found: {} and {}".format(Tsum, arr[i]))
            return True
        else:
            dict[arr[i]] = i
    print("Not found")
    return False

# print(quick_sort(arr))
find(quick_sort(arr), k)