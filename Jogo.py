class Jogo():
    def __init__(self):
        self.jogador="O"
        self.A=[["z","z","z"],["z","z","z"],["z","z","z"]]
        
    def recebe_jogada(self, linha, coluna):
        if self.A[linha][coluna]=="z":
            self.A[linha][coluna]=self.jogador
            if self.jogador=="X":
                self.jogador="O"
            elif self.jogador=="O":
                self.jogador="X"         
        
            
    def verifica_ganhador(self):
        if self.A[0][0]==self.A[0][1] and self.A[0][1]==self.A[0][2]:
            if self.A[0][0]=="O":
                return 1
            elif self.A[0][0]=="X":
                return 2
        elif self.A[1][0]==self.A[1][1] and self.A[1][1]==self.A[1][2]:
            if self.A[1][0]=="O":
                return 1
            elif self.A[1][0]=="X":
                return 2
        elif self.A[2][0]==self.A[2][1] and self.A[2][1]==self.A[2][2]:
            if self.A[2][0]=="O":
                return 1
            elif self.A[2][0]=="X":
                return 2
        elif  self.A[0][0]==self.A[1][0] and self.A[1][0]==self.A[2][0]:
            if self.A[0][0]=="O":
                return 1
            elif self.A[0][0]=="X":
                return 2              
        elif  self.A[0][1]==self.A[1][1] and self.A[1][1]==self.A[2][1]:
            if self.A[0][1]=="O":
                return 1
            elif self.A[0][1]=="X":
                return 2                     
        elif  self.A[0][2]==self.A[1][2] and self.A[1][2]==self.A[2][2]:
            if self.A[0][2]=="O":
                return 1
            elif self.A[0][2]=="X":
                return 2   
        elif (self.A[0][0]==self.A[1][1] and self.A[1][1]==self.A[2][2]):
            if self.A[1][1]=="O":
                return 1
            elif self.A[1][1]=="X":
                return 2
        elif (self.A[0][2]==self.A[1][1] and self.A[1][1]==self.A[2][0]):
            if self.A[1][1]=="O":
                return 1
            elif self.A[1][1]=="X":
                return 2
        else:
            if (self.A[0][0]!="z") and (self.A[0][1]!="z") and (self.A[0][2]!="z") and (self.A[1][0]!="z") and (self.A[1][1]!="z") and (self.A[1][2]!="z") and (self.A[2][0]!="z") and  (self.A[2][1]!="z") and (self.A[2][2]!="z"): 
                return 0
        
    def limpa_jogadas(self):
        if self.verifica_ganhador()==0 or self.verifica_ganhador()==1 or self.verifica_ganhador()==2:
            self.A=[["z","z","z"],["z","z","z"],["z","z","z"]]
            
        