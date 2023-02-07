
#  PARA IMPORTAR DETERMINADA LISTA OU ITEM PODEMOS USAR O "IMPORT"
import math #para importar toda a biblioteca math
from math import sqrt,floor # para importar a função 'sqrt'& 'floor'

#floor arrredonda um numero para baixo
#sqrt raiz quadrada

num = int(input("Digite o número: "))
raiz = sqrt(num) # não preciso escrever .math se importar função diretamente, caso contrario (math.sqrt)


print("A raiz de {} é igual a {:.2f}".format(num,raiz))







