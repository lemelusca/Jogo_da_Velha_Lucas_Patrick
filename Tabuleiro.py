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
        
        self.jogo = Jogo()
        
        self.botao1 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao1.configure(command = self.click1)
        self.botao1.grid(row=0, column=0,)
        
        self.botao2 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao2.configure(command = self.click2)
        self.botao2.grid(row=0, column=1)
        
        self.botao3 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao3.configure(command = self.click3)
        self.botao3.grid(row=0, column=2)
        
        self.botao4 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao4.configure(command = self.click4)
        self.botao4.grid(row=1, column=0)
        
        self.botao5 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao5.configure(command = self.click5)
        self.botao5.grid(row=1, column=1)
        
        self.botao6 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao6.configure(command = self.click6)
        self.botao6.grid(row=1, column=2)
        
        self.botao7 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao7.configure(command = self.click7)
        self.botao7.grid(row=2, column=0)
        
        self.botao8 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao8.configure(command = self.click8)
        self.botao8.grid(row=2, column=1)
        
        self.botao9 = tk.Button(self.tabuleiro, height=6, width= 13)
        self.botao9.configure(command = self.click9)
        self.botao9.grid(row=2, column=2)
        
        self.jogada = tk.Entry(self.tabuleiro, width= 50)
        self.jogada.grid(row=4, column=0, columnspan=4)       
        
    #função para iniciar o programa   
    def iniciar(self):
        self.tabuleiro.geometry("300x330")
        self.tabuleiro.mainloop()
        
    #funções para os botões receber a jogada                 
    def click1(self):
        self.botao1.configure(text = self.jogada.get())
    
    def click2(self):
        self.botao2.configure(text = self.jogada.get())
    
    def click3(self):
        self.botao3.configure(text = self.jogada.get()) 
        
    def click4(self):
        self.botao4.configure(text = self.jogada.get())    
    
    def click5(self):
        self.botao5.configure(text = self.jogada.get())   
    
    def click6(self):
        self.botao6.configure(text = self.jogada.get())    
        
    def click7(self):
        self.botao7.configure(text = self.jogada.get()) 
        
    def click8(self):
        self.botao8.configure(text = self.jogada.get())
        
    def click9(self):
        self.botao9.configure(text = self.jogada.get()) 
       

        
    
    
jogo=Tabuleiro()
jogo.iniciar() 
       
        

        
    

