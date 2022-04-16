num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b


calculadora = Calculadora(num1, num2)
print('Primerio valor: {}'.format(calculadora.valor_a))
print('Segundo valor: {}'.format(calculadora.valor_b))
print('Soma: {}'.format(calculadora.soma()))
print('Subtração: {}'.format(calculadora.subtracao()))
print('Divisão: {}'.format(calculadora.divisao()))
print('Multiplicação: {}'.format(calculadora.multiplicacao()))