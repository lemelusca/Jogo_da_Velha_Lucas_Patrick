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
                aviso=Tk()
                aviso.title("Aviso")
                mensagem=Label(aviso,"Jogada errada, tente novamente")
                mensagem.grid()
                botão_aviso=Button(aviso, width=6, text="OK", command=#tem que colocar um comando de fechar a janela)
                botão_aviso.grid()
                #arrumar posições das widgets da mensagem de aviso
    def verifica_ganhador():
        for x in range(3):
            if (A[x][0]==A[x][1] and A[x][1]==A[x][2]) or (A[0][x]==A[1][x] and A[1][x]==A[2][x]) or (A[0][0]==A[1][1] and A[1][1]==A[2][2]) or (A[0][2]==A[1][1] and A[1][1]==A[0][2]):
                if A[x][0]=="X":
                    return 1
                elif A[x][0]=="O":
                    return 2
            elif A[x][0]==0 or A[x][1]==0 or A[x][2]==0:
                return
            else:
                return 0