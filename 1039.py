n1,n2,n3,n4 = list(map(float,input().split()))
grade = (((n1*2)+(n2*3)+(n3*4)+(n4*1))/10)
print(f"Media: {grade:.1f}")
if(grade>=7.0):
    print("Aluno aprovado.")
elif(grade<5.0):
    print("Aluno reprovado.")
elif(grade>=5.0 and grade<=6.9):
    print("Aluno em exame.")
    n5 = float(input())
    print(f"Nota do exame: {n5:.1f}")
    grade = ((grade+n5)/2)
    if(grade>=5.0):
        print("Aluno aprovado.")
        print(f"Media final: {grade:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {grade:.1f}")