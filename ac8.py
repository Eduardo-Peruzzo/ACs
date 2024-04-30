"""
Problema 1
"""

def mdc():
    n = int(input())

    for _ in range(n):
        numeros = [int(s) for s in input().split()]
        numeros.sort()
        n1 = numeros[1]
        n2 = numeros[0]
        resto = n1 % n2
        while resto != 0:
            n1 = n2
            n2 = resto
            resto = n1 % n2
        print(n2)

# mdc()

"""
Problema 2
"""

def xadrez():
    while True:
        coordenadas = [int(s) for s in input().split()]
        if coordenadas[0] == 0 and coordenadas[1] == 0 and coordenadas[2] == 0 and coordenadas[3] == 0:
            break
        rainha = [coordenadas[0], coordenadas[1]]
        destino = [coordenadas[2], coordenadas[3]]
        # for y in range(1, 9):
        #     for x in range(1, 9):
        #         if [x, y] == rainha:
        #             print("X", end=" ")
        #         elif [x, y] == destino:
        #             print("Y", end=" ")
        #         else:
        #             print(".", end=" ")
        #     print()
        if destino[0] == rainha[0] and destino[1] == rainha[1]:
            print("0")
            continue
        if destino[0] == rainha[0] or destino[1] == rainha[1]:
            print("1")
            continue
        if abs(destino[0] - rainha[0]) == abs(destino[1] - rainha[1]):
            print("1")
        else:
            print("2")
            continue

# xadrez()


"""
Problema 3
"""

def soma_fatorial():
    while True:
        try:
            numeros = [int(s) for s in input().split()]
            n1 = numeros[0]
            n2 = numeros[1]
            fatorial1 = 1
            fatorial2 = 1

            for i in range(1, n1 + 1):
                fatorial1 *= i

            for c in range(1, n2 + 1):
                fatorial2 *= c

            print(fatorial1 + fatorial2)


        except EOFError:
            return

soma_fatorial()

"""
Problema 4
"""



"""
Problema 5
"""



"""
Problema 6
"""



"""
Problema 7
"""



"""
Problema 8
"""