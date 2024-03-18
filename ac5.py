"""
Pesquise sobre o módulo random, em particular sobre a função randint() (veja aqui a documentação oficial). Entendendo como essa função é utilizada, elabore um jogo por CLI e que você controla um aventureiro e está lutando contra um monstro. Considere os seguintes requisitos:

O aventureiro possui uma vida inicial igual a 100, seu ataque é um valor aleatório entre 10 e 20, e sua defesa é um valor aleatório entre 1 e 5;
O monstro possui uma vida aleatória entre 60 e 80, seu ataque é um valor aleatório entre 20 e 30, e não possui defesa;
Após a definição dos atributos do aventureiro e do monstro, o programa deve exibir os atributos iniciais e em seguida rodar um loop até que a vida de um dos dois fique igual ou abaixo de zero;
No loop, considere as seguintes ações:
O programa escreve o número da rodada do combate;
O aventureiro ataca o monstro, reduzindo da vida do monstro um valor aleatório entre 1 e o ataque do aventureiro;
Se a vida do monstro ficar igual ou abaixo de zero, o programa deve escrever na tela que o monstro morreu e encerrar o loop;
Em seguida, o monstro ataca o aventureiro, reduzindo da vida deste um valor aleatório entre 1 e o ataque do monstro, menos a defesa do aventureiro;
Se a vida do aventureiro ficar igual ou abaixo de zero, o programa deve escrever na tela que o aventureiro morreu e encerrar o loop;
Por fim, o programa deve escrever os atributos do aventureiro e do monstro.
O programa não deve possuir inputs do usuário, ele apenas deve exibir as informações. Faça o exercício em uma única função, main().
"""


from random import randint

def main():
    vida_aventureiro = 100
    atk_aventureiro = randint(10, 20)
    def_aventureiro = randint(1, 5)
    vida_monstro = randint(60, 80)
    atk_monstro = randint(20, 30)

    rodada = 1

    print("Aventureiro: vida", vida_aventureiro, "- atk", atk_aventureiro, "- def", def_aventureiro)
    print("Monstro: vida", vida_monstro, "- atk", atk_monstro)

    while vida_aventureiro >= 0 and vida_monstro >= 0:
        print("Rodada", rodada)
        vida_monstro = (vida_monstro - randint(1, atk_aventureiro))
        if vida_monstro <= 0:
            print("O monstro morreu!")
            break
        dano_monstro = (randint(1, atk_monstro) - def_aventureiro)
        if dano_monstro >= 0:
            vida_aventureiro = (vida_aventureiro - dano_monstro)
        if vida_aventureiro <= 0:
            print("Você morreu!")
            break
        rodada += 1
        print("Aventureiro: vida", vida_aventureiro, "- atk", atk_aventureiro, "- def", def_aventureiro)
        print("Monstro: vida", vida_monstro, "- atk", atk_monstro)



main()