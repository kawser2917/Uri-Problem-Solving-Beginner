import math
A,B,C = list(map(float,input().split()))
D = (B**2)-(4*A*C)
if(D>0 and A != 0):
    D = math.sqrt(D)
    R1 = (-B+D)/(2*A)
    R2 = (-B-D)/(2*A)
    print(f"R1 = {R1:.5f}\nR2 = {R2:.5f}")
else:
    print("Impossivel calcular")