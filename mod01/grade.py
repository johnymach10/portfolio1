prova1 = int(input('Digite a nota da prova 1:'))
prova2 = int(input('Digite a nota da prova 2:'))
trab = int(input('Digite a nota do trabalho:'))

media = ((prova1 * 2) + trab + (prova2 * 2)) / 5

if media >= 6:
    print('Aluno aprovado!')
else:
    if media >= 3:
        print('Aluno em recuperacao')
    else:
        print('Aluno reprovado!')