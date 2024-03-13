"""
Exercício 1: triângulos
Desenvolva uma função determina_tipo_triangulo que recebe três lados de um triângulo e retorna uma string, "Escaleno", "Isósceles" ou "Equilátero", conforme o tipo do triângulo. A função deve retornar "Não é um triângulo" se os três lados não formarem um triângulo.
"""

def determina_tipo_triangulo(l1, l2, l3):
    if not((l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1):
        return "Não é um triângulo"
    elif l1 == l2 == l3:
        return "Equilátero"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        return "Isósceles"
    else:
        return "Escaleno"


"""
Exercício 2: dia da semana
Desenvolva uma função dia_semana que recebe um número inteiro e retorna uma string indicando o dia da semana equivalente, considerando que o dia da semana igual a 1 é o domingo, 2 é segunda-feira, etc. A função deve retornar uma string vazia caso o número seja inválido.
"""

def dia_semana(dia):
    if dia == 1:
        return "Domingo"
    elif dia == 2:
        return "Segunda-feira"
    elif dia == 3:
        return "Terça-feira"
    elif dia == 4:
        return "Quarta-feira"
    elif dia == 5:
        return "Quinta-feira"
    elif dia == 6:
        return "Sexta-feira"
    elif dia == 7:
        return "Sábado"
    else:
        return ""


"""
Exercício 3: calculadora simples
Desenvolva funções de operações aritméticas soma, subtracao, multiplicacao e divisao, que recebem dois números cada uma e retornam o resultado da operação indicada. Em seguida, crie uma função que elabora uma interface por linha de comando (CLI), que lê dois números e uma operação e exibe na tela o valor do resultado, ou exibe "operação inválida" se o usuário inserir uma mensagem diferente das quatro operações.
"""

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calculadora():
    num1 = float(input("Informe o primeiro número: "))
    num2 = float(input("Informe outro número: "))
    operacao = input("Informe a operação: ")

    if operacao == "soma":
        return soma(num1, num2)
    elif operacao == "subtração":
        return subtracao(num1, num2)
    elif operacao == "multiplicação":
        return multiplicacao(num1, num2)
    elif operacao == "divisão":
        return divisao(num1, num2)
    else:
        return "Operação inválida"



def main():
    print(determina_tipo_triangulo(3, 3, 4))
    print(dia_semana(5))
    print(calculadora())

main()