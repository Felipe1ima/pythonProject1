a = float(input('Nota do primeiro bimestre: '))
if a > 10 or a < 0:
    a = float(input('Você digitou uma valor inválido, digite novamente a nota do bimestre: '))
b = float(input('Nota do segundo bimestre: '))
if b > 10 or b < 0:
    b = float(input('Você digitou uma valor inválido, digite novamente a nota do bimestre: '))
c = float(input('Nota do terceiro bimestre: '))
if c > 10 or c < 0:
    c = float(input('Você digitou uma valor inválido, digite novamente a nota do bimestre: '))
d = float(input('Nota do terceiro bimestre: '))
if d > 10 or d < 0:
    d = float(input('Você digitou uma valor inválido, digite novamente a nota do bimestre: '))
boletim = ('  Primeiro Bimestre: {a}\n  Segundo Bimestre:  {b}\n  Tercerio Bimestre: {c}\n  Quarto Bimestre:   {d}'.format(a=a,b=b,c=c,d=d))
media = (a + b + c + d)/4
print(' *------------------------*')
print(boletim)
print('  Média: {}'.format(media))
print(' *------------------------*\n')
if media == 10:
    print('Parabéns, você passou!!')
elif media > 6:
    print('Aprovado')
else:
    print('Reprovado')
