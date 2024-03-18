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

prod1 = input()
dados1 = prod1.split(" ")
quantidade_prod1 = int(dados1[1])
preco_prod1 = round(float(dados1[2]), 2)
prod2 = input()
dados2 = prod2.split(" ")
quantidade_prod2 = int(dados2[1])
preco_prod2 = round(float(dados2[2]), 2)
valor = round(quantidade_prod1 * preco_prod1 + quantidade_prod2 * preco_prod2, 2)

print("VALOR A PAGAR: R${:.2f}".format(valor))

"""
Problema 4
"""
nums = input()
num123 = nums.split()
num1 = float(num123[0])
num2 = float(num123[1])
num3 = float(num123[2])
num4 = (num1 + num2 + abs(num1 - num2))/2
num_final = (num4 + num3 + abs(num4 - num3))/2
print("{:.0f} eh o maior".format(num_final))

"""
Problema 5
"""
recebe_valores1 = input()
recebe_valores2 = input()
ponto1 = recebe_valores1.split()
ponto2 = recebe_valores2.split()
x1 = float(ponto1[0])
y1 = float(ponto1[1])
x2 = float(ponto2[0])
y2 = float(ponto2[1])
distancia = float(((x2 - x1)**2 + (y2 - y1)**2)**(1/2))
print("{:.4f}".format(distancia))
