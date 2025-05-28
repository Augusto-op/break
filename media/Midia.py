nota_total = 0 
bimestre = 0

while bimestre < 4:
    nota = float(input('Digite a notra  do  aluno :'))
    nota_total += nota 
    bimestre += 1
    print (f'A {nota} digitada do aluno foi amarzanamento com sucesso!')

media = nota_total / 4
print(f'A media do aluno é {media}')