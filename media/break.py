soma = 0 
nota = 0

while True:
    nota = float(input('Digite a nota do aluno /n ou /nDigite a 99 para sair ;'))
    if nota == 99:
        break
    soma += nota
    print(f'A media do aluno é {soma / 4}') 
   