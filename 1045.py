A,B,C = map(float,input().split())
if(A<B):
    temp = A
    A = B
    B = temp
if(A<C):
    temp = A
    A = C
    C = temp
if(B<C):
    temp = B
    B = C
    C = temp
if(A>=(B+C)):
    print("NAO FORMA TRIANGULO")
elif((A**2) == ((B**2)+(C**2))):
    print("TRIANGULO RETANGULO")
elif((A**2)>((B**2)+(C**2))):
    print("TRIANGULO OBTUSANGULO")
elif((A**2)<((B**2)+(C**2))):
    print("TRIANGULO ACUTANGULO")
if(A==B==C):
    print("TRIANGULO EQUILATERO")
elif(A==B or B==C):
    print("TRIANGULO ISOSCELES")
 
 

 