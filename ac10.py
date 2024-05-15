"""
Problema 1
"""

"""def camisas():
    n = int(input())
    lista_compradores = []
    lista_camisas = []
    for _ in range(n):
        comprador = input()
        camisa = input()
        lista_camisas.append(camisa)
        lista_compradores.append(comprador)
    lista_camisas_sortidas = lista_camisas.copy()
    lista_camisas_sortidas.sort(reverse=True)
    for _ in range(len(lista_camisas)):
        print(lista_camisas_sortidas[0], lista_compradores[lista_camisas.index(lista_camisas_sortidas[0])])

        if len(lista_camisas_sortidas) > 0:
            lista_compradores.pop(lista_camisas.index(lista_camisas_sortidas[0]))
            lista_camisas_sortidas.pop(0)"""

# Eu não consegui resolver esse problema, então acabei pegando uma resposta que vi na internet:

"""
class Camiseta:
    def __init__(self, n, c, t):
        self.nome = n
        self.cor = c
        self.tamanho = t


def comp(a, b):
    if(a.cor == b.cor):
        if(a.tamanho == b.tamanho):
            if(a.nome < b.nome):
                return -1
            if(a.nome > b.nome):
                return 1
            return 0
        if(a.tamanho > b.tamanho):
            return -1
        return 1
    if(a.cor < b.cor):
        return -1
    return 1


def particao(V, inicio, fim):
    pivo = V[fim - 1]
    i = inicio
    for j in range(inicio, fim):
        if(comp(V[j], pivo) < 0):
            V[j], V[i] = V[i], V[j]
            i += 1

    if(comp(pivo, V[i]) < 0):
        V[fim - 1], V[i] = V[i], V[fim - 1]

    return i


def quickSort(V, inicio, fim):
    if(fim > inicio):
        posicaoPivo = particao(V, inicio, fim)
        quickSort(V, inicio, posicaoPivo)
        quickSort(V, posicaoPivo + 1, fim)


first = True
while True:
    try:
        N = int(input())

        if(N == 0):
            break

        if(first):
            first = False
        else:
            print('')

        camisetas = []
        for _ in range(N):
            nome = input()
            cor, tamanho = input().strip().split(' ')

            camisetas.append(Camiseta(nome, cor, tamanho))

        quickSort(camisetas, 0, len(camisetas))

        for camiseta in camisetas:
            print(f'{camiseta.cor} {camiseta.tamanho} {camiseta.nome}')
    except EOFError:
        break
"""


"""
Problema 2
"""

def odeio_esse_exercicio():
    n = int(input())
    input()

    for i in range(n):
        quantidade_arvores = 0
        arvores = {}


        while True:
            if i == n-1:
                try:
                    x = input()

                    if(x in arvores):
                        arvores[x] += 1
                    else:
                        arvores[x] = 1
                    quantidade_arvores += 1
                except EOFError:
                    break
            else:
                x = input()
                if x == "":
                    break

                if(x in arvores):
                    arvores[x] += 1
                else:
                    arvores[x] = 1
                quantidade_arvores += 1

        arvores_ordenadas = dict(sorted(arvores.items()))
        for arvore, quantidade in arvores_ordenadas.items():
            print(f"{arvore} {((quantidade/quantidade_arvores)*100):.4f}")
        arvores={}
        quantidade_arvores = 0
        if i < n-1:
            print()

# odeio_esse_exercicio()

"""
Problema 3
"""

def escada():
    while True:
        try:
            degraus = int(input())
            h, c, l = input().split()
            h = float(h)
            c = float(c)
            l = float(l)

            h /= 100
            c /= 100
            l /= 100

            hipotenusa = (c**2 + h**2)**0.5

            print("{:.4f}".format(hipotenusa*l*degraus))


        except EOFError:
            return

escada()