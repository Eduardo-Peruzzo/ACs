"""
Exercício 1: equações de segundo grau
Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0. O programa deve ler os parâmetros a, b e c da equação e deve calcular as raízes pela fórmula de Bhaskara.

Considere que as raízes dadas pelo usuário são sempre reais, e os valores passados pelo usuário são sempre numéricos.
"""

a = float(input("Informe o parâmetro a da equação: "))
b = float(input("Informe o parâmetro b da equação: "))
c = float(input("Informe o parâmetro c da equação: "))

x1 = (-b + (b**2 - 4*a*c)**(1/2)) / 2*a
x2 = (-b - (b**2 - 4*a*c)**(1/2)) / 2*a

print("A primeira raiz da equação é ", x1)
print("A primeira raiz da equação é ", x2)

print("-" * 30)

"""
Exercício 2: anos bissextos
Elabore um programa em Python que leia uma variável inteira ano. Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto. Um ano é bissexto se ele é múltiplo de quatro. No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos. Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

O programa deve utilizar apenas as funções print(), input() e int(), além dos operadores lógicos and, or ou not e de operadores aritméticos ou de comparação necessários.
"""

print("Informações: o usuário deve informar um ano, e o programa retornará True caso o ano seja bissexto, ou retornará False caso o ano não seja bissexto.")

ano = int(input("Informe o ano: "))

print(((ano % 100 == 0 and ano % 400 == 0) and ano % 4 == 0) or (ano % 4 == 0 and ano % 100 != 0))