import tkinter as tk
import requests 
from PIL import Image,ImageTk
from io import BytesIO

url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/838.png"

Ventana = tk.Tk()
Ventana.title("Imagen desde URL")

response = requests.get(url)
imagen_data = BytesIO(response.content)
image = Image.open(imagen_data)
photo = ImageTk.PhotoImage(image)
label_imagen = tk.Label(Ventana)
label_imagen.config(image=photo)
label_imagen.image = photo
label_imagen.pack()

Ventana.mainloop()