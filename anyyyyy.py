arr=[1,5,3,7,6]
n=len(arr)#5 length
for i in range(n):
    for j in range(n-i-1):
        if arr[j]< arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)

arr=[1,5,3,7,6]
n=len(arr)#5 length
for i in range(n):
    for j in range(n-i-1):
        if arr[j]> arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)