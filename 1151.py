# n = int(input())
# a,b = 0,1
# for i in range(n):
#     print(str(a).lstrip(),end=' ')
#     a,b = b,a+b

n = int(input())
arr = list()
arr.append(0)
arr.append(1)
for i in range(2, n):
    arr.append(arr[i-1] + arr[i - 2])
for i in range(len(arr)):
    if (i == (n - 1)):
        print(arr[i])
    else:
        print(arr[i], end=" ")
