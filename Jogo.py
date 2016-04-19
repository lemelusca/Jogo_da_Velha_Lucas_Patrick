import tkinter as tk

class Jogo:
#criar uma matrz de elementos 0 antes de iniciar o programa
    def recebe_jogada(linha, coluna):#achar como atribuir as coordenadas dos botões para linha e coluna 
        #tem que atribuir as coordenadas do botão para a matriz
         while #alguma coisa:   
         
            if A[linha][coluna]==0:
                A[linha][coluna]=jogador
                if jogador=="X":
                    jogador="O"
                elif jogador=="O":
                    jogador="X"
                #Falta alterar o texto do botão   
            
            else:
                #aviso
    
    def verifica_ganhador():
        for x in range(3):
            if A[x][0]==A[x][1] and A[x][1]==A[x][2]:
                if A[x][0]=="X":
                    return 1
                elif A[x][0]=="O":
                    return 2
        for y in range(3):
            if  A[0][y]==A[1][y] and A[1][y]==A[2][y]:
                if A[0][y]=="X":
                    return 1
                elif A[0][y]=="O":
                    return 2                                
        if (A[0][0]==A[1][1] and A[1][1]==A[2][2]) or (A[0][2]==A[1][1] and A[1][1]==A[2][0]):
            if A[1][1]=="X":
                return 1
            elif A[1][1]=="0":
                return 2
        elif:
            for e in range(3):
                if A[e][0]==0:
                    return
                else:
                    return 0
                    
    def limpa_jogadas():
        