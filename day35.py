#i forgot
arr = [1, 5, 3, 7, 6]
count = 0
n = len(arr)
for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            count = count + 1

print(arr)
print("Number of swaps:", count)

#selection maybe
arr = [33, 4, 65, 3, 5, 6, 7, 8, 9]
n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)