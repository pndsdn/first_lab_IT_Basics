arr_size = 50
arr = []

for i in range(arr_size):
    arr.append(i + 1)

arr.reverse()
p = 0
s = 0

for i in range(arr_size - 2):

    if arr[i] < arr[i + 1] + arr[i + 2] and arr[i + 1] < arr[i + 1] + arr[i] and arr[i + 2] < arr[i] + arr[i + 2]:
        p = arr[i] + arr[i + 1] + arr[i + 2]
        s = (p * (p - arr[i]) * (p - arr[i + 1]) * (p - arr[i + 2])) ** 0.5
        print(arr[i], arr[i + 1], arr[i + 2])
        break
