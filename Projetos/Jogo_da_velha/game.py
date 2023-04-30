

"""
Jogo da velha

-exibirtela
-verificar ganhou
    -verificar diagonal
    -linhas vertical/horizontal
    -colunas

"""
import os
import random



tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
jogador = 1 # 0 jogador X, 1 Jogador 2
maxjogadas = 9


def exibirTela():
    print('   0   1   2')
    print('0:',tabuleiro[0][0],"|",tabuleiro[0][1],'|',tabuleiro[0][2])
    print('  -----------')
    print('1:',tabuleiro[1][0],"|",tabuleiro[1][1],'|',tabuleiro[1][2])
    print('  -----------')
    print('2:',tabuleiro[2][0],"|",tabuleiro[2][1],'|',tabuleiro[2][2])
    print('  -----------')


def jogar():
    global jogador
    print( 'Jogador "X"' if jogador == 1 else 'Jogador "O"', 'é a sua vez')
    linha = int(input("Escolha a Linha: "))
    coluna = int(input("Escolha a coluna: "))

    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = 'X' if jogador == 1 else 'O'
        jogador = jogador%2 + 1
        
    else :
        print('Local Ocupado..')
        


def verificarGanhador():
    global tabuleiro
    #verificar linhas 
    for c in range(3):
        soma = tabuleiro[c][0] + tabuleiro[c][1] + tabuleiro[c][2]
        if soma == 'XXX' or soma =='OOO':
            return 1
    
    for l in range(3):
        soma = tabuleiro[0][l] + tabuleiro[1][l] + tabuleiro[2][l]
        if soma == 'XXX' or soma =='OOO':
            return 1    
    
    diagonal1 = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
    diagonal2 = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    if diagonal1=='XXX' or diagonal1=='OOO' or diagonal2=='XXX' or diagonal2=='OOO':
        return 1
    
    return None


print("----------------------------------------------------")
print("            Bem-Vindo ao jogo da Velha: ")
print("----------------------------------------------------")
a = input("Vamos Jogar ? 😊\n")

if a[0].upper() == 'S':
    desejaJogar = True
else:
    desejaJogar = False

while desejaJogar:
    exibirTela()
    jogar()
    maxjogadas += 1
    if maxjogadas == 9:
        print('Acabou e empatou')
        a = input("Deseja jogar Novamente? ? 😊\n")
        if a[0].upper() == 'S':
            desejaJogar = True
        else:
            desejaJogar = False

    if verificarGanhador() != None :
        exibirTela()
        print(jogador %2 +1, "Ganhou")
        a = input("Deseja jogar Novamente? ? 😊\n")
        if a[0].upper() == 'S':
            desejaJogar = True
        else:
            desejaJogar = False
