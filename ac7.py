"""
Problema 1
"""

def salario():
    salario = float(input())

    if salario >= 0 and salario <= 400:
        print("Novo salario: {:.2f}".format(salario + (salario * 0.15)))
        print("Reajuste ganho: {:.2f}".format((salario * 0.15)))
        print("Em percentual: 15 %")

    if salario >= 400.01 and salario <= 800:
        print("Novo salario: {:.2f}".format(salario + (salario * 0.12)))
        print("Reajuste ganho: {:.2f}".format((salario * 0.12)))
        print("Em percentual: 12 %")

    if salario >= 800.01 and salario <= 1200:
        print("Novo salario: {:.2f}".format(salario + (salario * 0.1)))
        print("Reajuste ganho: {:.2f}".format((salario * 0.1)))
        print("Em percentual: 10 %")

    if salario >= 1200.01 and salario <= 2000:
        print("Novo salario: {:.2f}".format(salario + (salario * 0.07)))
        print("Reajuste ganho: {:.2f}".format((salario * 0.07)))
        print("Em percentual: 7 %")

    if salario > 2000:
        print("Novo salario: {:.2f}".format(salario + (salario * 0.04)))
        print("Reajuste ganho: {:.2f}".format((salario * 0.04)))
        print("Em percentual: 4 %")

# salario()

"""
Problema 2
"""

def numeros_pares():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())

    contagem = 0

    if num1 % 2 == 0:
        contagem += 1
    if num2 % 2 == 0:
        contagem += 1
    if num3 % 2 == 0:
        contagem += 1
    if num4 % 2 == 0:
        contagem += 1
    if num5 % 2 == 0:
        contagem += 1

    print("{} valores pares".format(contagem))

# numeros_pares()

"""
Problema 3
"""

def somas():
    num1 = int(input())
    num2 = int(input())

    soma = 0

    if num2 > num1:
        for contagem in range(num1, num2 + 1):
            if contagem % 13 == 0:
                continue
            soma += contagem

    if num1 > num2:
        for contagem in range(num2, num1 + 1):
            if contagem % 13 == 0:
                continue
            soma += contagem

    print(soma)

# somas()

"""
Problema 4
"""

def progressao_geometrica():
    primeiro = int(input())

    for cont in range(0, 10):
        print("N[{}] = {}".format(cont, primeiro))
        primeiro *= 2

# progressao_geometrica()

"""
Problema 5
"""

def menor_da_lista():
    quantidade = int(input())
    lista = (input()).strip()

    lista2 = lista.split(" ")

    menor = [int(s) for s in lista2]
    lista2 = [int(s) for s in lista2]

    menor.sort()

    print("Menor valor: {}".format(menor[0]))
    for x, y in zip(list(range(0, quantidade)), lista2):
        if y == menor[0]:
            print("Posicao: {}".format(x))


# menor_da_lista()

"""
Problema 6
"""

def coluna():
    coluna = int(input())
    operacao = input().upper()
    array = []
    soma = 0
    media = 0

    for _ in range(0, 144):
        array.append(int(input()))

    if operacao == "S":
        for c in range(0, 12):
            soma += array[coluna]
            coluna += 12
        print(soma)

    if operacao == "M":
        for c in range(0, 12):
            media += array[coluna]
            coluna += 12
        print(media / 12)

coluna()