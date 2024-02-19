# l = int(input())
# n= input()
# s= 0
# for i in range(12):
#     for j in range(12):
#         v = float(input())
#         if (i == l):
#             s += v

# if (n == 'S'):
#     print("%.1f" % s)
# else:
#     print("%.1f" % (s / 12.0)
M = []
l = int(input())
op = input()
sum = 0
for i in range(12):
    element = []
    for j in range(12):
        v = float(input())
        element.append(v)
    M.append(element)
for i in range(12):
    sum += M[l][i]
if(op.upper() == "S"):
    print(f"{sum:.1f}")
else:
    print(f"{(sum/12):.1f}")