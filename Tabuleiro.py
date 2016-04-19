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
        
    def iniciar(self):
        self.tabuleiro.mainloop()
        
jogo=Tabuleiro()
jogo.iniciar() 
        
    

