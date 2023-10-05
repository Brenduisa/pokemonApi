import tkinter
from ApiPoke import Pokemon
import requests
from PIL import Image,ImageTk
from io import BytesIO
import tkinter as tk
from random import randint
from Jogador import Jugador
from pantalla import Pantalla

class Juego:
    
    def __init__(self):
        self.pantalla = Pantalla()
        self.jugador1 = self.pantalla.jg1
        self.jugador2 = self.pantalla.jg2
        pkInicial1 = self.jugador1.mochila[0]
        pkInicial2 = self.jugador2.mochila[0]
   

        for banco in range(len(self.pantalla.bancoDeSuplentes)):
            self.pantalla.insertarFoto(self.pantalla.bancoDeSuplentes[banco], self.jugador1.mochila[banco].img )
        self.pantalla.insertarFoto(self.pantalla.lp7,pkInicial1.imgEspalda)
        self.pantalla.insertarFoto(self.pantalla.lp3,pkInicial2.img)
        self.pantalla.mostrarInfopk1(pkInicial1)
        self.pantalla.mostrarInfopk2(pkInicial2)
        self.pantalla.juego.mainloop()
        self.Ataques = self.pantalla.Ataques    
       # self.botones_ataques = []
    
    def descontar_vida():
        self.pantalla   
       
       
       
       
       
       
       
    #     # Crea los botones de ataques después de que se haya creado la instancia de Pantalla
    #     self.Ataques = self.pantalla.Ataques
    #     self.botones_ataques = []
    #     for i in range(4):
    #         boton_ataque = tk.Button(self.Ataques, text=f"Ataque {i+1}", command=lambda i=i: self.ejecutar_ataque(i))
    #         boton_ataque.grid(row=1, column=i)
    #         self.botones_ataques.append(boton_ataque)
            
    

    # # def ejecutar_ataque(self, indice_ataque):
    # #     # Obtener el Pokémon atacante (supongamos que es el primer Pokémon del jugador 1)
    # #     atacante = self.jugador1.mochila[0]

    # #     # Obtener el Pokémon objetivo (supongamos que es el primer Pokémon del jugador 2)
    # #     objetivo = self.jugador2.mochila[0]

    # #     # Obtener el ataque seleccionado según el índice
    # #     ataque_seleccionado = list(atacante.ataque.keys())[indice_ataque]
    # #     poder_ataque = atacante.ataques[ataque_seleccionado]

    # #     # Calcular el daño causado por el ataque (simplificado)
    # #     daño = (atacante.atk * poder_ataque) / objetivo.defensa

    # #     # Reducir la vida del Pokémon objetivo
    # #     objetivo.vida -= daño

    # #     # Actualizar la información en la pantalla
    # #     self.pantalla.mostrarInfo(atacante, objetivo)



def iniciar_juego():
    a = Juego()
    a.pantalla.juego.mainloop()


if __name__ == '__main__':
    iniciar_juego()