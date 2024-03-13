"""
Exercício 1: revisite a AC1
Desenvolva duas funções em Python:

eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma equação de segundo grau no formato ax² + bx + c = 0, supondo as raízes sempre reais;
bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.
"""

def eq_seg_grau(a, b, c):
    return (-b + (b**2 - 4*a*c)**(1/2)) / 2*a, (-b - (b**2 - 4*a*c)**(1/2)) / 2*a

def bissexto(ano):
    return ((ano % 100 == 0 and ano % 400 == 0) and ano % 4 == 0) or (ano % 4 == 0 and ano % 100 != 0)


"""
Exercício 2: salário
Desenvolva uma função em Python cujo nome é calcula_salario. Essa função recebe dois parâmetros posicionais reais, valor_hora e num_horas, que correspondem ao valor do salário por hora e o número de horas trabalhadas no mês, respectivamente. Além disso, a função tem um parâmetro-chave irpf, que calcula o imposto de renda a ser deduzido, cujo valor padrão é 0.275. A função retorna o salário líquido de um funcionário, calculado como o produto do valor por hora pelo número de horas, reduzido o percentual do imposto de renda dado.
"""

def calcula_salario(valor_hora, num_horas, irpf=0.275):
    return (valor_hora * num_horas) - (valor_hora * num_horas * irpf)




def main():
    print(eq_seg_grau(1, -4, 4))
    print(bissexto(2012))
    print(calcula_salario(1000, 10))

main()