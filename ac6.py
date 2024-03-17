"""
Problema 1
"""

print("Hello World!")

"""
Problema 2
"""

a = int(input("Informe um número: "))
b = int(input("Informe um número: "))
x = a + b
print("X = {}".format(x))

"""
Problema 3
"""

codigo_prod1 = int(input("Còdigo do produto 1: "))
codigo_prod2 = int(input("Còdigo do produto 2: "))
quantidade_prod1 = int(input("Quantidade restante do produto 1: "))
quantidade_prod2 = int(input("Quantidade restante do produto 2: "))
preco_prod1 = float(input("Preço do produto 1: "))
preco_prod2 = float(input("Preço do produto 2: "))

print("VALOR A PAGAR: R$", (quantidade_prod1 * preco_prod1) + (quantidade_prod2 * preco_prod2))

"""
Problema 4
"""


"""
Problema 5
"""

x1 = float(input("X do ponto 1: "))
y1 = float(input("Y do ponto 1: "))
x2 = float(input("X do ponto 2: "))
y2 = float(input("Y do ponto 2: "))

print(round(((x2 - x1)**2 + (y2 - y1)**2)**(1/2), 4))