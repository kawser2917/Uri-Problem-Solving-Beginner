import math
X1,Y1 = list(map(float,input().split()))
X2,Y2 = list(map(float,input().split()))
distance = math.sqrt(pow((X2-X1),2)+pow((Y2-Y1),2))
print(f"{distance:.4f}")