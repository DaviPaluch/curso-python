

# posso fazer uma lista de nome, números, boleanos, uma lista de listas
from tkinter import N


familia = ["Zéxinho", "Uguinho", "Clorisvaldo", "Everaldo", "Jozilene"]
#            0       1         2          3        4
#           -5      -4        -3         -2       -1

# da mesma forma que a stg funciona, a collection também funciona por índices
# se voce análisar a string é uma coleção de letras
listadenumeros = [0, 0, 0, 0, 0, 0, 0, 0]
#                 0  1  2  3  4  5  6  7

# as listas são feitas entre conchetes e vírgulas

print(familia[0])
# irá imprimir o Zéxinho
print(familia[-3])
# retorna um índice de trás para frente
print(familia[2:])
# retorna a partir do índice 2 até o final
print(familia[1:4])
# retorna o índice 1 até o 3, o 4 é o limite
print(familia[1:5])
# retorna o índice 1 até o 4, e 5 é o limite

familia[0] = "x"
print(familia)

familia.extend(["Jó", "Leoncio"])
# adiciona várias valores a coleção
print(familia)

familia.append("melisa")
# adiciona um valor a coleção, mas é adicionado no final
print(familia)

familia.insert(1, "taylerina")
print(familia)
# adiciona um valor na lista de acordo com a posição do índice

familia.pop()
# remove o ultimo valor
print(familia)

familia.remove("taylerina")
# remove o valor desejado na collection
print(familia)

# familia.clear()
# remove todos os valores da lista
print(familia)

print(familia.index("luiz"))
# retorna o indice com base em um valor, retornou o indice do pai, que é 3

print(familia.count("davi"))
# a funçao "count" conta quantos valores repitidos estão dentro da coleção
# no caso nenhum, porque davi agora é "x"

idade_familia = [20, 21, 47, 46, 11, 20, 82]
print(idade_familia)

idade_familia.sort()
# funçao .sort serve para ordenar os valores do menor para o maior
print(idade_familia)

idade_familia.reverse()
print(idade_familia)
# a função .reverse é usada para reverter os valores do conjunto

print(familia)
familia.sort()
# a função .sort coloca as strings em ordem alfabética se for string
print(familia)

familia2 = familia.copy
familia.remove("x")
print(familia2)
print(familia)
# "familia2" está em uma memória de referencia da "familia", isso é uma referencia
# então se for manipulado irá afetar o outro
# o comando ".copy" ira fazer uma nova vatiável da lista familia


#                            TUPLES                         #

# Definição: um tuple, diferente de uma lista; é imutável
# não pode ser alterado

cordenadas = (-41, 105)
# cordenadas.pop()
print(cordenadas)
