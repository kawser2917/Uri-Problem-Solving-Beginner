fib = [0,1]
a = 0
b = 1
for i in range(60):
    temp = a + b
    fib.append(temp)
    a = b
    b = temp
t = int(input())
for i in range(t):
    n = int(input())
    print(f"Fib({n}) = {fib[n]}")