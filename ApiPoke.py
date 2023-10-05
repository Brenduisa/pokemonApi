import requests
import random

lista = []

class Pokemon():
    nombre = ""
    vida = 0
    velocidad = 0
    tipo1 = ""
    tipo2 = ""
    atk = 0
    specialAtk = 0
    specialDefensa = 0
    defensa = 0
    id = 0
    img = ""
    imgEspalda = ""
    

    def __init__(self,id):
        self.id = id
        self.ataques = [] #Lista de ataques del pokemon 
        self.obtenerDatosPoke(id)
        print(f"datos obtenidos pokemon {self.nombre}")
        
        
    def agregar_ataque(self,nombre_ataque):
        self.ataques.append(nombre_ataque)
        

    def obtenerDatosPoke(self, id):
        self.id = id
        res = ""
        while "200" not in str(res):
            #self.id = random.randint(1, 1281)
            
            url = f"https://pokeapi.co/api/v2/pokemon/{self.id}/"

            res = requests.get(url)
            if "200" in str(res):
                data = res.json()
                self.img = data['sprites']['front_default']
                self.nombre = data['forms'][0]['name']
                self.vida = data['stats'][0]['base_stat']
                self.velocidad = data['stats'][5]['base_stat']
                self.atk = data['stats'][1]['base_stat']
                self.specialAtk = data['stats'][3]['base_stat']
                self.defensa = data['stats'][2]['base_stat']
                self.tipo1 = data['types'][0]['type']['name']
                self.specialDefensa = data['stats'][4]['base_stat']
                self.imgEspalda = data['sprites']['back_default']
                if len(data["types"]) > 1:
                    self.tipo2 = data['types'][1]['type']['name']
    
    def __repr__(self):
        return f'{self.nombre} - {self.id}'
    
    def obtenerAtaques(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.id}/"
        res = requests.get(url)
        if "200" in str(res):
            data = res.json()
            ataques = data['moves'][:4]  # Obtiene los primeros 4 ataques
            for ataque in ataques:
                nombre_ataque = ataque['move']['name']
                self.agregar_ataque(nombre_ataque)
            return ataques
        return []
        

if __name__ == '__main__':            
        
    pk1 = Pokemon(1)
    pk1.obtenerAtaques()
    print(pk1.ataques)
    
    pk2 = Pokemon(2)
    pk2.obtenerAtaques()
    print(pk2.ataques)
    
    
    
