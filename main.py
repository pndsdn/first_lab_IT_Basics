def char_check(user_str):
    for i in user_str:
        if ord(i) not in range(48, 58):
            return False

    return True


while True:
    arr_size = input("Enter the number of numbers: ")

    if char_check(arr_size):
        arr_size = int(arr_size)
        if arr_size < 3:
            print("\t\tError!\nMinimum number of numbers is 3")

        else:
            break
    else:
        print("Wrong char!")

arr = [arr_size]
i = 0

while i < arr_size:
    num = input("Enter number #" + str(i+1) + ": ")

    if char_check(num):
        num = int(num)
        if num <= 0:
            print("Wrong number!")

        else:
            arr.append(num)
            i += 1
    else:
        print("Wrong char!")

arr.sort(reverse=True)
p = 0
s = 0
f = 0
for i in range(arr_size - 2):

    if arr[i] < arr[i + 1] + arr[i + 2] and arr[i + 1] < arr[i + 1] + arr[i] and arr[i + 2] < arr[i] + arr[i + 2]:
        p = arr[i] + arr[i + 1] + arr[i + 2]
        s = (p * (p - arr[i]) * (p - arr[i + 1]) * (p - arr[i + 2])) ** 0.5
        print(arr[i], arr[i + 1], arr[i + 2])
        f = 1
        break
if f == 0:
    print("Triangle does not exist")