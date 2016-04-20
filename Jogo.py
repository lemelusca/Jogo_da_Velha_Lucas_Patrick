class Jogo():
    def __init__(self):
        self.jogador="O"
        self.A=[["z","z","z"],["z","z","z"],["z","z","z"]]  
        
    def recebe_jogada(self, linha, coluna):
        if A[linha][coluna]=="z":
            A[linha][coluna]=self.jogador
            if self.jogador=="X":
                self.jogador="O"
            elif self.jogador=="O":
                self.jogador="X"         
         
    def verifica_ganhador(self):
        for a in range(3):
            if A[a][0]==A[a][1] and A[a][1]==A[a][2]:
                if A[a][0]=="X":
                    return 1
                elif A[a][0]=="O":
                    return 2
        for b in range(3):
            if  A[0][b]==A[1][b] and A[1][b]==A[2][b]:
                if A[0][b]=="X":
                    return 1
                elif A[0][b]=="O":
                    return 2                                
        if (A[0][0]==A[1][1] and A[1][1]==A[2][2]) or (A[0][2]==A[1][1] and A[1][1]==A[2][0]):
            if A[1][1]=="X":
                return 1
            elif A[1][1]=="0":
                return 2
        else:
            for e in range(3):
                if A[e][0]=="z":
                    return
                else:
                    return 0
                    
    def limpa_jogadas(self):
        if verifica_ganhador()==0 or verifica_ganhador()==1 or verifica_ganhador()==2:
            A=[["z","z","z"],["z","z","z"],["z","z","z"]]
            
        