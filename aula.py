print ("Digite 1 para Soma e 2 para Subtração: ")
operacao = int (input("1- Soma 2-Subtracao: "))
a = int (input)("Primeira operação: ")
b = int (input)("Segundo operação: ")
resultado = 0
if operacao == 1:
    resultado = a + b
    else: resultado = a -b

print(resultado)
