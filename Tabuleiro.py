# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:53:11 2016

@author: Lucas
"""

import tkinter as tk
from Jogo import Jogo


class Tabuleiro:
    
    def __init__(self):
        self.tabuleiro = tk.Tk()
        self.tabuleiro.title("Jogo da Velha")

        self.jogo = Jogo()
        
        
                  
        self.botao1 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao1.configure(command = self.mudanças1)
        self.botao1.grid(row=0, column=0,)
        
        self.botao2 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao2.configure(command = self.mudanças2)
        self.botao2.grid(row=0, column=1)
        
        self.botao3 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao3.configure(command = self.mudanças3)
        self.botao3.grid(row=0, column=2)
        
        self.botao4 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao4.configure(command = self.mudanças4)
        self.botao4.grid(row=1, column=0)
        
        self.botao5 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao5.configure(command = self.mudanças5)
        self.botao5.grid(row=1, column=1)
        
        self.botao6 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao6.configure(command = self.mudanças6)        
        self.botao6.grid(row=1, column=2)
        
        self.botao7 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao7.configure(command = self.mudanças7)        
        self.botao7.grid(row=2, column=0)
        
        self.botao8 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao8.configure(command = self.mudanças8)        
        self.botao8.grid(row=2, column=1)
        
        self.botao9 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao9.configure(command = self.mudanças9)
        self.botao9.grid(row=2, column=2)
        
        self.jogada = tk.Label(self.tabuleiro, width= 50, text = "Proxima Jogada: X", anchor = "w")
        self.jogada.grid(row=4, column=0, columnspan=20)       
        
    #função para iniciar o programa   
    def iniciar(self):
        self.tabuleiro.geometry("310x330")
        self.tabuleiro.mainloop()
        
    #funçao para avisar quem é o proximo Jogador    
    def mudar_label(self):
        if self.jogada["text"]=="Proxima Jogada: X":
            self.jogada["text"]="Proxima Jogada: O"
        elif self.jogada["text"]=="Proxima Jogada: O":
            self.jogada["text"]="Proxima Jogada: X"  
            
    def limpar_painel(self):
        self.botao1["text"]=""
        self.botao2["text"]=""
        self.botao3["text"]=""
        self.botao4["text"]=""
        self.botao5["text"]=""
        self.botao6["text"]=""
        self.botao7["text"]=""
        self.botao8["text"]=""
        self.botao9["text"]="" 
            
    def mudanças1(self):
        self.click1()
        self.mudar_label()
        if self.verifica_ganhador()==0 or self.verifica_ganhador==1 or self.verifica_ganhador==2:
        
            
    def mudanças2(self):
        self.click2()  
        self.mudar_label()
        
    def mudanças3(self):
        self.click3()  
        self.mudar_label()
        
    def mudanças4(self):
        self.click4()  
        self.mudar_label()
        
    def mudanças5(self):
        self.click5()  
        self.mudar_label()
        
    def mudanças6(self):
        self.click6()  
        self.mudar_label()
        
    def mudanças7(self):
        self.click7()  
        self.mudar_label()
        
    def mudanças8(self):
        self.click8()  
        self.mudar_label()
        
    def mudanças9(self):
        self.click9()  
        self.mudar_label()
            
            
    #funções para os botões receber a jogada                 
    def click1(self):
        self.jogo.recebe_jogada(0,0)
        self.botao1.configure(text = self.jogo.jogador)
        self.jogo.verifica_ganhador()
            
    def click2(self):
        self.jogo.recebe_jogada(0,1)
        self.botao2.configure(text = self.jogo.jogador)
        self.jogo.verifica_ganhador()
        
    def click3(self):
        self.jogo.recebe_jogada(0,2)
        self.botao3.configure(text = self.jogo.jogador) 
        self.jogo.verifica_ganhador()
        
    def click4(self):
        self.jogo.recebe_jogada(1,0)
        self.botao4.configure(text = self.jogo.jogador)    
        self.jogo.verifica_ganhador()
        
    def click5(self):
        self.jogo.recebe_jogada(1,1)
        self.botao5.configure(text = self.jogo.jogador)   
        self.jogo.verifica_ganhador()
        
    def click6(self):
        self.jogo.recebe_jogada(1,2)
        self.botao6.configure(text = self.jogo.jogador)    
        self.jogo.verifica_ganhador()
        
    def click7(self):
        self.jogo.recebe_jogada(2,0)
        self.botao7.configure(text = self.jogo.jogador) 
        self.jogo.verifica_ganhador()
        
    def click8(self):
        self.jogo.recebe_jogada(2,1)
        self.botao8.configure(text = self.jogo.jogador)
        self.jogo.verifica_ganhador()
        
    def click9(self):
        self.jogo.recebe_jogada(2,2)
        self.botao9.configure(text = self.jogo.jogador)
        self.jogo.verifica_ganhador()  

     
app=Tabuleiro()
app.iniciar() 
       
        

        
    

