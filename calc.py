#def = define function
#if = se
#else = senão
#while = enquanto

def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erro: Impossível dividir por 0!"
    
while True:
    print("Escolha uma operação: ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")