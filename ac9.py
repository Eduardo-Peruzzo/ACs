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

    for _ in range(n):
        custo = 0

        quantidade_produtos = int(input())
        for _ in range(quantidade_produtos):
            produto = input().split()
            produtos[produto[0]] = float(produto[1])

        lista_de_compra = int(input())
        for _ in range(lista_de_compra):
            fruta, quantidade = input().split()
            if fruta in produtos.keys():
                custo += (produtos[fruta] * int(quantidade))

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

def tacografo():
    n = int(input())
    total = 0
    for _ in range(n):
        tempo, km = input().split()
        total += float(tempo) * float(km)
    print("{:.0f}".format(total))

# tacografo()

"""
Problema 7
"""

def joao_burro():
    n = int(input())
    print(n*4)

# joao_burro()


"""
Problema 8
"""

def sequencia():
    n = int(input())
    lista = []
    total = 1
    for _ in range(n):
        num = int(input())
        lista.append(num)
    item_anterior = lista[0]
    for item in lista:
        if item_anterior == item:
            continue
        else:
            total += 1
        item_anterior = item
    print(total)

sequencia()