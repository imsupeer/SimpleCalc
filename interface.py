from funcoes import *

while True:
    print("\nEscolha uma operação: ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair\n")

    operacao = input("Digite o número da operação desejada: ")

    if operacao == '5':
        print("Fechando calculadora...")
        break

    if operacao not in('1', '2', '3', '4'):
        print("Opção inválida! Insira uma das opçãoes válidas")
        continue

    num1 = float(input("Digite o primeiro número para ser operado: "))
    num2 = float(input("Digite o segundo número para ser operado: "))

    if operacao == '1':
        print(num1, "+", num2, "=", adicao(num1, num2))
    elif operacao == '2':
        print(num1, "-", num2, "=", subtracao(num1, num2))
    elif operacao == '3':
        print(num1, "*", num2, "=", multiplicacao(num1, num2))
    elif operacao == '4':
        resultado_divisao = divisao(num1, num2)
        if isinstance(resultado_divisao, str):
            print(resultado_divisao)
        else:
            print(num1, '/', num2, "=", resultado_divisao)
