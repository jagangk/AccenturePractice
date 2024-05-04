# function define
def cyclic_reverse(arr, k):
    n = len(arr)
    k = k % n
    arr[n-k:] = arr[n-k:][::-1]
    arr[:n-k] = arr[:n-k][::-1]
    arr[:] = arr[::-1]
    return arr
# Driver code to get input from the user
k = int(input('Enter the count to be rotated: '))
n = int(input('Enter the size of array: '))
arr = []
count = 1
for i in range(0, n):
    print(f'Enter element {count}: ')
    nums = int(input())
    arr.append(nums)
    count+=1
print('Rotated array: ', cyclic_reverse(arr, k))
