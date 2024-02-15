n = int(input())
nums = []
for i in range(1000):
    for j in range(n):
        nums.append(j)
pos = 0
for n in range(1000):
    print(f"N[{pos}] = {nums[n]}")
    pos+=1