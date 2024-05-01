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

# soma_fatorial()

"""
Problema 4
"""

def comida():
    n = int(input())
    for _ in range(n):
        dias = 0
        quantidade = float(input())
        while quantidade > 1:
            quantidade /= 2
            dias += 1
        print(dias, "dias")

# comida()

"""
Problema 5
"""

def frequencia():
    n = int(input())
    lista = []
    for _ in range(n):
        num = int(input())
        lista.append(num)
    lista_unica = list(set(lista))
    lista_unica.sort()

    for i in range(len(lista_unica)):
        print("{} aparece {} vez(es)".format(lista_unica[i], lista.count(lista_unica[i])))


# frequencia()


"""
Problema 6
"""

def primos():
    n = int(input())

    for _ in range(n):
        num = int(input())
        raiz = num ** 0.5
        primo = "Prime"
        for i in range(2, int(raiz+1)):
            if num % i == 0:
                primo = "Not Prime"
                break
        print(primo)


# primos()


"""
Problema 7
"""

def moeda():
    n = int(input())
    while n != 0:
        resultados = input().split()
        print("Mary won {} times and John won {} times".format(resultados.count("0"), resultados.count("1")))
        n = int(input())

# moeda()


"""
Problema 8
"""

def funcoes():
    n = int(input())
    for _ in range(n):
        x_y = [int(s) for s in input().split()]
        x = x_y[0]
        y = x_y[1]
        rafael = (3*x)**2 + y**2
        beto = 2*(x**2) + (5*y)**2
        carlos = -100*x + y**3
        if rafael > beto and rafael > carlos:
            print("Rafael ganhou")
        if beto > rafael and beto > carlos:
            print("Beto ganhou")
        if carlos > beto and carlos > rafael:
            print("Carlos ganhou")

funcoes()