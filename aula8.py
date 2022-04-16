conjunto = {1,2,3,4,5}
conjunto2 = {6,7,8,9,4,5,7}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {} '.format(conjunto_uniao))

# conjunto3 = {1,2,3,4,5,3,7,7,9,9}
# conjunto.add(10)
# conjunto.discard(1)
# print(type(conjunto3))
# print(conjunto)

conjunto_inter =conjunto.intersection(conjunto2)
print("intersecção:{} ".format(conjunto_inter))
conjunto_diferecial1 = conjunto.difference(conjunto2)
conjunto_diferecial2 = conjunto2.difference(conjunto)
print("diferença do 1 do 2: {}".format(conjunto_diferecial1))
print("diferença do 2 do 1: {}".format(conjunto_diferecial2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print("Diferença simetrica: {}".format(conjunto_diff_simetrica))

conjunto_a = {1,2,3,4,5}
conjunto_b = {1,2,3,4,5,6,7,8}
conjunto_subset = conjunto_a.issubset(conjunto_b)
conjunto_superset= conjunto_b.issuperset(conjunto_a)
print("É subconjunto de B: {}".format(conjunto_subset))
print("É superconjunto de A: {}".format(conjunto_superset))

lista = ['cachorro', 'cachorro', 'gato', 'elefante']
print('É uma lista: {}'.format(lista))
conjunto_animais = set(lista)
print('É um conjunto: {}'.format(conjunto_animais))
lista_animais = list(conjunto_animais)
print('É uma lista: {}'.format(lista_animais))
