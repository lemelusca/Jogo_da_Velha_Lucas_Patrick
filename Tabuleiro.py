# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:53:11 2016

@author: Lucas
"""

import tkinter as tk

import tkinter.messagebox as tkm

from Jogo import Jogo


class Tabuleiro:
    
    def __init__(self):
        self.tabuleiro = tk.Tk()
        self.tabuleiro.title("Jogo da Velha")

        self.jogo = Jogo()
        
        self.botao1 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao1.configure(command = self.mudancas1)
        self.botao1.grid(row=0, column=0,)
        
        self.botao2 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao2.configure(command = self.mudancas2)
        self.botao2.grid(row=0, column=1)
        
        self.botao3 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao3.configure(command = self.mudancas3)
        self.botao3.grid(row=0, column=2)
        
        self.botao4 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao4.configure(command = self.mudancas4)
        self.botao4.grid(row=1, column=0)
        
        self.botao5 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao5.configure(command = self.mudancas5)
        self.botao5.grid(row=1, column=1)
        
        self.botao6 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao6.configure(command = self.mudancas6)        
        self.botao6.grid(row=1, column=2)
        
        self.botao7 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao7.configure(command = self.mudancas7)        
        self.botao7.grid(row=2, column=0)
        
        self.botao8 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao8.configure(command = self.mudancas8)        
        self.botao8.grid(row=2, column=1)
        
        self.botao9 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao9.configure(command = self.mudancas9)
        self.botao9.grid(row=2, column=2)
        
        self.jogada = tk.Label(self.tabuleiro, width= 50, text = "Proxima Jogada: X", anchor = "w")
        self.jogada.grid(row=4, column=0, columnspan=20)       
        
    #função para iniciar o programa   
    def iniciar(self):
        self.tabuleiro.geometry("310x330")
        self.tabuleiro.mainloop()
                            
    def limpar_painel(self):
        self.botao1.configure(text = "", state="normal")
        self.botao2.configure(text = "", state="normal")
        self.botao3.configure(text = "", state="normal")
        self.botao4.configure(text = "", state="normal")
        self.botao5.configure(text = "", state="normal")
        self.botao6.configure(text = "", state="normal")
        self.botao7.configure(text = "", state="normal")
        self.botao8.configure(text = "", state="normal")
        self.botao9.configure(text = "", state="normal") 
            
    def mudancas1(self):
        self.click1()
        
        if self.jogada["text"]=="Proxima Jogada: X":
            self.jogada["text"]="Proxima Jogada: O"
        elif self.jogada["text"]=="Proxima Jogada: O":
            self.jogada["text"]="Proxima Jogada: X"
                
        if self.jogo.verifica_ganhador()==1:
            tkm.showinfo(title = "Game Over", message = "Jogador X Ganhou")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
        elif self.jogo.verifica_ganhador()==2:
            tkm.showinfo(title = "Game Over", message = "Jogador O Ganhou")
            self.jogada["text"]="Proxima Jogada: O"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "X"
        elif self.jogo.verifica_ganhador()==0:
            tkm.showinfo(title = "Game Over", message = "Empate")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
                                    
    def mudancas2(self):
        self.click2()  
        
        if self.jogada["text"]=="Proxima Jogada: X":
            self.jogada["text"]="Proxima Jogada: O"
        elif self.jogada["text"]=="Proxima Jogada: O":
            self.jogada["text"]="Proxima Jogada: X"
               
        if self.jogo.verifica_ganhador()==1:
            tkm.showinfo(title = "Game Over", message = "Jogador X Ganhou")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
        elif self.jogo.verifica_ganhador()==2:
            tkm.showinfo(title = "Game Over", message = "Jogador O Ganhou")
            self.jogada["text"]="Proxima Jogada: O"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "X"
        elif self.jogo.verifica_ganhador()==0:
            tkm.showinfo(title = "Game Over", message = "Empate")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
            
                    
    def mudancas3(self):
        self.click3()  
        
        if self.jogada["text"]=="Proxima Jogada: X":
            self.jogada["text"]="Proxima Jogada: O"
        elif self.jogada["text"]=="Proxima Jogada: O":
            self.jogada["text"]="Proxima Jogada: X"
              
        if self.jogo.verifica_ganhador()==1:
            tkm.showinfo(title = "Game Over", message = "Jogador X Ganhou")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
        elif self.jogo.verifica_ganhador()==2:
            tkm.showinfo(title = "Game Over", message = "Jogador O Ganhou")
            self.jogada["text"]="Proxima Jogada: O"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "X"
        elif self.jogo.verifica_ganhador()==0:
            tkm.showinfo(title = "Game Over", message = "Empate")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
            
    def mudancas4(self):
        self.click4()  
        
        if self.jogada["text"]=="Proxima Jogada: X":
            self.jogada["text"]="Proxima Jogada: O"
        elif self.jogada["text"]=="Proxima Jogada: O":
            self.jogada["text"]="Proxima Jogada: X"
              
        if self.jogo.verifica_ganhador()==1:
            tkm.showinfo(title = "Game Over", message = "Jogador X Ganhou")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
        elif self.jogo.verifica_ganhador()==2:
            tkm.showinfo(title = "Game Over", message = "Jogador O Ganhou") 
            self.jogada["text"]="Proxima Jogada: O"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "X"
        elif self.jogo.verifica_ganhador()==0:
            tkm.showinfo(title = "Game Over", message = "Empate")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
                    
    def mudancas5(self):
        self.click5()  
        
        if self.jogada["text"]=="Proxima Jogada: X":
            self.jogada["text"]="Proxima Jogada: O"
        elif self.jogada["text"]=="Proxima Jogada: O":
            self.jogada["text"]="Proxima Jogada: X"
                
        if self.jogo.verifica_ganhador()==1:
            tkm.showinfo(title = "Game Over", message = "Jogador X Ganhou")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
        elif self.jogo.verifica_ganhador()==2:
            tkm.showinfo(title = "Game Over", message = "Jogador O Ganhou") 
            self.jogada["text"]="Proxima Jogada: O"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "X"
        elif self.jogo.verifica_ganhador()==0:
            tkm.showinfo(title = "Game Over", message = "Empate")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
                    
    def mudancas6(self):
        self.click6()
        
        if self.jogada["text"]=="Proxima Jogada: X":
            self.jogada["text"]="Proxima Jogada: O"
        elif self.jogada["text"]=="Proxima Jogada: O":
            self.jogada["text"]="Proxima Jogada: X"
                   
        if self.jogo.verifica_ganhador()==1:
            tkm.showinfo(title = "Game Over", message = "Jogador X Ganhou")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
        elif self.jogo.verifica_ganhador()==2:
            tkm.showinfo(title = "Game Over", message = "Jogador O Ganhou")
            self.jogada["text"]="Proxima Jogada: O"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "X"
        elif self.jogo.verifica_ganhador()==0:
            tkm.showinfo(title = "Game Over", message = "Empate")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
                    
    def mudancas7(self):
        self.click7()  
        
        if self.jogada["text"]=="Proxima Jogada: X":
            self.jogada["text"]="Proxima Jogada: O"
        elif self.jogada["text"]=="Proxima Jogada: O":
            self.jogada["text"]="Proxima Jogada: X"
                
        if self.jogo.verifica_ganhador()==1:
            tkm.showinfo(title = "Game Over", message = "Jogador X Ganhou")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
        elif self.jogo.verifica_ganhador()==2:
            tkm.showinfo(title = "Game Over", message = "Jogador O Ganhou") 
            self.jogada["text"]="Proxima Jogada: O"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "X"
        elif self.jogo.verifica_ganhador()==0:
            tkm.showinfo(title = "Game Over", message = "Empate")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
                       
    def mudancas8(self):
        self.click8()  
    
        if self.jogada["text"]=="Proxima Jogada: X":
            self.jogada["text"]="Proxima Jogada: O"
        elif self.jogada["text"]=="Proxima Jogada: O":
            self.jogada["text"]="Proxima Jogada: X"
               
        if self.jogo.verifica_ganhador()==1:
            tkm.showinfo(title = "Game Over", message = "Jogador X Ganhou")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
        elif self.jogo.verifica_ganhador()==2:
            tkm.showinfo(title = "Game Over", message = "Jogador O Ganhou")
            self.jogada["text"]="Proxima Jogada: O"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "X"
        elif self.jogo.verifica_ganhador()==0:
            tkm.showinfo(title = "Game Over", message = "Empate")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
            
    def mudancas9(self):
        self.click9()  
       
        if self.jogada["text"]=="Proxima Jogada: X":
            self.jogada["text"]="Proxima Jogada: O"
        elif self.jogada["text"]=="Proxima Jogada: O":
            self.jogada["text"]="Proxima Jogada: X"
               
        if self.jogo.verifica_ganhador()==1:
            tkm.showinfo(title = "Game Over", message = "Jogador X Ganhou")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
        elif self.jogo.verifica_ganhador()==2:
            tkm.showinfo(title = "Game Over", message = "Jogador O Ganhou")
            self.jogada["text"]="Proxima Jogada: O"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "X"
        elif self.jogo.verifica_ganhador()==0:
            tkm.showinfo(title = "Game Over", message = "Empate")
            self.jogada["text"]="Proxima Jogada: X"
            self.limpar_painel()
            self.jogo.limpa_jogadas()
            self.jogo.jogador = "O"
                        
            
    #funções para os botões receber a jogada                 
    def click1(self):
        self.jogo.recebe_jogada(0,0)
        self.botao1.configure(text = self.jogo.jogador, state = "disabled") 
        self.jogo.verifica_ganhador()
            
    def click2(self):
        self.jogo.recebe_jogada(0,1)
        self.botao2.configure(text = self.jogo.jogador, state = "disabled")
        self.jogo.verifica_ganhador()
        
    def click3(self):
        self.jogo.recebe_jogada(0,2)
        self.botao3.configure(text = self.jogo.jogador, state = "disabled") 
        self.jogo.verifica_ganhador()
        
    def click4(self):
        self.jogo.recebe_jogada(1,0)
        self.botao4.configure(text = self.jogo.jogador, state = "disabled")    
        self.jogo.verifica_ganhador()
        
    def click5(self):
        self.jogo.recebe_jogada(1,1)
        self.botao5.configure(text = self.jogo.jogador, state = "disabled")   
        self.jogo.verifica_ganhador()
        
    def click6(self):
        self.jogo.recebe_jogada(1,2)
        self.botao6.configure(text = self.jogo.jogador, state = "disabled")    
        self.jogo.verifica_ganhador()
        
    def click7(self):
        self.jogo.recebe_jogada(2,0)
        self.botao7.configure(text = self.jogo.jogador, state = "disabled") 
        self.jogo.verifica_ganhador()
        
    def click8(self):
        self.jogo.recebe_jogada(2,1)
        self.botao8.configure(text = self.jogo.jogador, state = "disabled")
        self.jogo.verifica_ganhador()
        
    def click9(self):
        self.jogo.recebe_jogada(2,2)
        self.botao9.configure(text = self.jogo.jogador, state = "disabled") 
        self.jogo.verifica_ganhador()
     
app=Tabuleiro()
app.iniciar() 
       
        

        
    

