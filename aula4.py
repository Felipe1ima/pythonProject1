a = float(input('Nota do primeiro bimestre: '))
while a > 10 or a < 0:
    a = float(input('Você digitou uma valor inválido, digite novamente: '))
b = float(input('Nota do segundo bimestre: '))
while b > 10 or b < 0:
    b = float(input('Você digitou uma valor inválido, digite novamente: '))
c = float(input('Nota do terceiro bimestre: '))
while c > 10 or c < 0:
    c = float(input('Você digitou uma valor inválido, digite novamente: '))
d = float(input('Nota do terceiro bimestre: '))
while d > 10 or d < 0:
    d = float(input('Você digitou uma valor inválido, digite novamente: '))
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
