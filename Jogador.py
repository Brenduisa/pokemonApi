import tkinter
from ApiPoke import Pokemon
import requests
from PIL import Image,ImageTk
from io import BytesIO
import tkinter as tk
from random import randint


class Jugador:
    def __init__(self):                   
        self.mochila = []
        for i in range(6):
            id = randint(1,1000)
            self.pk = Pokemon(id)
            self.mochila.append(self.pk)
            



#jugador1 = Jugador()

#print(jugador1.mochila)

#jugador2 = Jugador()
#print(jugador2.mochila)

#print(jugador2.mochila[3].atk)




