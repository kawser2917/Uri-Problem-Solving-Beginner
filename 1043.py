A,B,C = list(map(float,input().split()))
if((A+B)>C and (B+C)>A and (C+A)>B):
    Perimetro = A+B+C
    print(f"Perimetro = {Perimetro:.1f}")
else:
    area = (A+B)*C/2
    print(f"Area = {area:.1f}")