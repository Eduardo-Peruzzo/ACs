"""
Problema 1
"""

def distancia():
    km = int(input())
    print(km*2, "minutos")

# distancia()

"""
Problema 2
"""

def fatorial():
    n = int(input())
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(fatorial)

# fatorial()

"""
Problema 3
"""

def mercado():
    n = int(input())
    produtos = {}
    compras = {}

    for _ in range(n):
        custo = 0

        quantidade_produtos = int(input())
        for _ in range(quantidade_produtos):
            produto = input().split()
            produtos[produto[0]] = float(produto[1])

        lista_de_compra = int(input())
        for _ in range(lista_de_compra):
            compra = input().split()
            compras[compra[0]] = int(compra[1])

        lista = list(compras)
        for c in range(len(lista)):
            custo += (produtos[lista[c]] * compras[lista[c]])

        print("R$ {:.2f}".format(custo))

# mercado()


"""
Problema 4
"""

def cha():
    correto = input()
    tentativas = input().split()
    print(tentativas.count(correto))

# cha()

"""
Problema 5
"""

def folhas():
    dados = [int(s) for s in input().split()]
    if (dados[0] * dados[2]) <= dados[1]:
        print("S")
    else:
        print("N")

# folhas()

"""
Problema 6
"""



"""
Problema 7
"""



"""
Problema 8
"""

