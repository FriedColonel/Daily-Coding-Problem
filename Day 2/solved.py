list = [1, 2, 3, 4, 5]

def productExceptSelf(arr):
    result = [0] * len(arr)
    result[0] = 1
    for i in range(1,len(arr)):
        result[i] = result[i-1] * arr[i-1]
    product = 1
    for i in range(len(arr)):
        result[len(arr)-1-i] *= product
        product *= arr[len(arr)-1-i]
    return result

print(productExceptSelf(list))