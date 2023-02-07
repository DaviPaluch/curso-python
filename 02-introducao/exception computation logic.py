try:
    number = int(input('digite um numero:'))
    print(number)

except ZeroDivisionError:
    print("divisão por zero não é possivel")
except ValueError:
    print('digite um valor válido.')
except:
    print('erro inesperado')
finally:
    print("Sempre executa")
