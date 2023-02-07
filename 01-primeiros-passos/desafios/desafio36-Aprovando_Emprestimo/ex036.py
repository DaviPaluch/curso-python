valor_da_casa = int(input('Digite o valor da casa: '))

salario = int(input('Digite seu salario: '))

anos = int(input('Em quantos anos voce vai pagar a casa?'))

parcelas =  valor_da_casa /(anos * 12)





if (salario * 0.3) > parcelas:
    print("you don't have money to buy this house")
else:
    print("congratulation, what are you mothod of payment?")
    print(f" the installments will be {parcelas} ")
    









