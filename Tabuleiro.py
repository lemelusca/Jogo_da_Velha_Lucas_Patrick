# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:53:11 2016

@author: Lucas
"""

import tkinter as tk


class Tabuleiro:
    
    def __init__(self):
        self.tabuleiro = tk.Tk()
        self.tabuleiro.title("Jogo da Velha")
        
        
                  
        self.botao1 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao1.configure(command = self.click1)
        self.botao1.configure(command = self.mudar_label)
        self.botao1.grid(row=0, column=0,)
        
        self.botao2 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao2.configure(command = self.click2)
        self.botao2.configure(command = self.mudar_label)
        self.botao2.grid(row=0, column=1)
        
        self.botao3 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao3.configure(command = self.click3)
        self.botao3.configure(command = self.mudar_label)
        self.botao3.grid(row=0, column=2)
        
        self.botao4 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao4.configure(command = self.click4)
        self.botao4.configure(command = self.mudar_label)
        self.botao4.grid(row=1, column=0)
        
        self.botao5 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao5.configure(command = self.click5)
        self.botao5.configure(command = self.mudar_label)
        self.botao5.grid(row=1, column=1)
        
        self.botao6 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao6.configure(command = self.click6)
        self.botao6.configure(command = self.mudar_label)
        self.botao6.grid(row=1, column=2)
        
        self.botao7 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao7.configure(command = self.click7)
        self.botao7.configure(command = self.mudar_label)
        self.botao7.grid(row=2, column=0)
        
        self.botao8 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao8.configure(command = self.click8)
        self.botao8.configure(command = self.mudar_label)
        self.botao8.grid(row=2, column=1)
        
        self.botao9 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao9.configure(command = self.click9)
        self.botao9.configure(command = self.mudar_label)
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
            
    #funções para os botões receber a jogada                 
    def click1(self):
        self.jogo.recebe_jogada(0,0)
        self.botao1.configure(text = self.jogo.jogador)
        
            
    def click2(self):
        self.jogo.recebe_jogada(0,1)
        self.botao2.configure(text = self.jogo.jogador)
    
    def click3(self):
        self.jogo.recebe_jogada(0,2)
        self.botao3.configure(text = self.jogo.jogador) 
        
    def click4(self):
        self.jogo.recebe_jogada(1,0)
        self.botao4.configure(text = self.jogo.jogador)    
    
    def click5(self):
        self.jogo.recebe_jogada(1,1)
        self.botao5.configure(text = self.jogo.jogador)   
    
    def click6(self):
        self.jogo.recebe_jogada(1,2)
        self.botao6.configure(text = self.jogo.jogador)    
        
    def click7(self):
        self.jogo.recebe_jogada(2,0)
        self.botao7.configure(text = self.jogo.jogador) 
        
    def click8(self):
        self.jogo.recebe_jogada(2,1)
        self.botao8.configure(text = self.jogo.jogador)
        
    def click9(self):
        self.jogo.recebe_jogada(2,2)
        self.botao9.configure(text = self.jogo.jogador)
        

       
app=Tabuleiro()
app.iniciar() 
       
        

        
    

