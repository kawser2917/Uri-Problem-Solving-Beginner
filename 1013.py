A,B,C = list(map(int,input().split()))
maior = (A+B+abs(A-B))/2
result = int((maior+C+abs(maior-C))/2)
print(result,"eh o maior")