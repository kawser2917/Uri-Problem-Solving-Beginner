sum = 1
b = 2
for i in range(3,40,2):
    sum += float(i)/float(b)
    b*=2
print(f"{sum:.2f}")
    