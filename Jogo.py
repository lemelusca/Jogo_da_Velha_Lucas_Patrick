class Jogo():
    def __init__(self):
        self.jogador="O"  
        
    def recebe_jogada(self, linha, coluna):
        if A[linha][coluna]=="z":
            A[linha][coluna]=self.jogador
            if self.jogador=="X":
                self.jogador="O"
            elif self.jogador=="O":
                self.jogador="X"         
        
            
    def verifica_ganhador(self):
        for a in range(3):
            for b in range(3):
                if A[a][0]==A[a][1] and A[a][1]==A[a][2]:
                    if A[a][0]=="O":
                        return 1
                    elif A[a][0]=="X":
                        return 2
                elif  A[0][b]==A[1][b] and A[1][b]==A[2][b]:
                    if A[0][b]=="O":
                        return 1
                    elif A[0][b]=="X":
                        return 2                                
                elif (A[0][0]==A[1][1] and A[1][1]==A[2][2]) or (A[0][2]==A[1][1] and A[1][1]==A[2][0]):
                    if A[1][1]=="O":
                        return 1
                    elif A[1][1]=="X":
                        return 2
                else:
                    if A[a][b]!="z":
                        return 0
                    else:
                        return 
                    
    def limpa_jogadas(self):y
        if verifica_ganhador()==0 or verifica_ganhador()==1 or verifica_ganhador()==2:
            A=[["z","z","z"],["z","z","z"],["z","z","z"]]
            
        