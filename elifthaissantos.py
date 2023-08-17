nome = input ("digite o nome do aluno: ")
BIM1 =float(input ("digite a nota do bimestre 1: "))
BIM2 = float(input ("digite a nota do bimestre 2: "))
BIM3 = float(input ("digite a nota do bimestre 3: "))
BIM4 = float(input ("digite a nota do bimestre 4: "))
media = ((BIM1+BIM2+BIM3+BIM4)/4 )
print ("a media foi: ",media)

if media >=9:
    print("aprovado com louvor ")

elif media >=7:
    print ("aprovado  ")

elif media <=7:
    print ("reprovado ")
