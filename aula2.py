a = int(input('entre com um valor: '))
b = int(input('entre com um valor: '))
c = '4'
soma = a + b
multiplicacao = a * b
divisao = a / b
subtracao = a - b
resto = a % b
resultado = (' Soma:{soma}. \n Multiplicação: {multiplicacao}.  \n Divisão: {divisao}. \n Subtração: {subtracao}. \n Resto: {resto}.'.format(soma=soma,subtracao=subtracao,resto=resto,multiplicacao=multiplicacao,divisao=divisao))
print(resultado)