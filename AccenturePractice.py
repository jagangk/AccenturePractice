def empty_packets_checker(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j = j + 1
    for k in range(j, len(arr)):
        arr[k] = 0
    return arr
arr = [8,5,0,0,0,0]
result = empty_packets_checker(arr)
print(result)
