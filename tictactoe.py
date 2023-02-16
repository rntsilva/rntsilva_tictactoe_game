"""

    Jogo da velha em python para praticar

Deve imprimir o tabuleiro 3 X 3
Eperar os jogadores realizem as jogadas
Verificar jogada
Verificar vencedor

"""

def print_board(board):
 
     for i in range(0, 16):
        if (i == 0 or i == 15) or i % 5 == 0:
            print(f" {'-'*7} {'-'*7} {'-'*7} ")
        else:
            print(f"|{' '*7}|{' '*7}|{' '*7}|")


if __name__ == "__main__":

    print('Inicio jogo \n')

    board = [[1, None , None], [None, None, 0], [None, None, None]] 
    print_board(board)



# imprimir

# X , O

#  ------- ------- ------- 
# |*     *|       |       |
# | *   * |       |       |
# |   *   |       |       |
# | *   * |       |       |
# |*     *|       |       |
#  ------- ------- -------
# |       |       |  ***  |
# |       |       | *   * |
# |       |       |*     *|
# |       |       | *   * |
# |       |       |  ***  |
#  ------- ------- -------
# |       |       |  ***  |
# |       |       | *   * |
# |       |       |*     *|
# |       |       | *   * |
# |       |       |  ***  |
#  -----------------------