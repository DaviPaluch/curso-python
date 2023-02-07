

my_string = "  my text"

print(f"{my_string}")
# f"{my_string} está armazenando a variavel desse texto

print(f"concatenar {my_string} em string")
# Colocar "f" para puxar a variavel "str"(string)

print(my_string.upper())
# funções de strings #a função "upper" deixa todas as letras em maiúsculo
# os dois parenteses dentro servem para usar a função, algumas funções pedem parametros dentro deles

print(my_string.isupper())
# verifica se minha string é maiúscula
# valor boleano, e no caso, FALSO

print(my_string.lower())
# coloca a string toda em minúscula

print(my_string.islower())
# verifica se a string é minuscula
# valor boleano, e no caso, VERDADEIRO

print(my_string.capitalize())
# deixa a primeira letra str maiúscula

print(my_string.strip())
#remove os espaços no inicio do texto e no final, no meio não remove#
# pode ser util em um banco de dados quando um usuário colocar um nome
# e voce precisa comparar os dados sem espaçamento que ele fez

print(my_string.replace("my", "her"))
# substitui uma palavra, texto ou uma letra, por outra
# necessita de parametros

print(len(my_string))
# conta quantos algorismos tem mimha string

print(my_string.replace("t", "T", 1))
# faz com que a letra "t" fique maiúscula uma vez

print(my_string[3])
# retorna o numero da letra que está destro do conchete
# lembrar que em programação a contagem começa em "0"

print(my_string[2:7])
# retorna o número do caractére 2 ao 5

print(my_string[-5:-2])
# retorna o caráctere de trás para frente
# my textd
# ...-3-2-1

print(my_string.index("x"))
# retorna o valor do nímero da stg "x"
print(my_string.index("ext"))
# pode retornar uma palavra e o resultado é a primeira letra

x = "texto" in my_string
print(x)
# para saber se existe a stg na "my_string"

my_string2 = """linha 01 
linha 02
linha 03"""
# para escrever cada texto em uma linha diferente, mas não é muito usado
print(my_string2)

my_strin3 = "linha01 \nlinha02 \nlinha 03 "
print(my_strin3)
# serve para inserir novas linhas no código
