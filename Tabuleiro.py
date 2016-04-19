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
        
        self.botao1 = tk.Button(self.tabuleiro)
        self.botao1.grid(row=0, column=0)
        
        self.botao2 = tk.Button(self.tabuleiro)
        self.botao2.grid(row=0, column=1)
        
        self.botao3 = tk.Button(self.tabuleiro)
        self.botao3.grid(row=0, column=2)
        
        self.botao4 = tk.Button(self.tabuleiro)
        self.botao4.grid(row=1, column=0)
        
        self.botao5 = tk.Button(self.tabuleiro)
        self.botao5.grid(row=1, column=1)
        
        self.botao6 = tk.Button(self.tabuleiro)
        self.botao6.grid(row=1, column=2)
        
        self.botao7 = tk.Button(self.tabuleiro)
        self.botao7.grid(row=2, column=0)
        
        self.botao8 = tk.Button(self.tabuleiro)
        self.botao8.grid(row=2, column=1)
        
        self.botao9 = tk.Button(self.tabuleiro)
        self.botao9.grid(row=2, column=2)
        
    def iniciar(self):
        self.tabuleiro.mainloop()
        
jogo=Tabuleiro()
jogo.iniciar() 
       
        

        
    

