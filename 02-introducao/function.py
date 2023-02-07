#                   THE    FUNCTIONS                     #


# the functions serve to organizing your code


# def big_mac():
#print("sandwith big mac ")


# print("início")
# big_mac()
# big_mac()
# big_mac()
# big_mac()
# big_mac()
# big_mac()
# big_mac()
# big_mac()
# print("fim")

# make_big_mac("Davi")
# make_big_mac("Bruno")
# make_big_mac("João")


def make_big_mac(name):
    print(f"sandwith Big Mac {name}")


def make_potato(size):
    print(f"potato {size}")


def make_soda(size, type):

    print(f"{size} {type}")

# make_big_mac("Davi")
# make_potato("big")
# make_soda("small", "sprite")


def make_combo_big_mac(name, size_potato, type_soda, size_soda):
    # i am putting the functions inside other functions
    # i can use this to enjoy my functions
    make_big_mac(name)
    make_potato(size_potato)
    make_soda(size_soda, type_soda)


make_combo_big_mac("davi", "big", "coca", "small")

# ----------------------------------------------------------------------------------#


def soma_num(num1, num2):
    return num1 + num2


# result = soma_num(17, 45)


#-----------------------------------------------------------------------------------#

def most_number(list_num):
    list_num.sort()
    list_num.reverse()
    most_number = list_num[0]
    return most_number

#   RESUMO: dou nome a função
    #   se ela tiver atributos eu dou um nome a ela
    #   e trabalho dentro da função com os atributos


result = most_number([65, 89, 87, 54, 6, 46, 84, 74, 6, 54, 86, 5, 21, 23, 2])
print(result)
# resultado da função de maior número
