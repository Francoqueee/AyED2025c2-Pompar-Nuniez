from modules.LDE import ListaDobleEnlazada  
from modules.carta import Carta  

class DequeEmptyError(Exception):
    # Excepcion personalizada para indicar que el mazo esta vacio.
    pass 

class Mazo:
    def __init__(self):
        self.lista= ListaDobleEnlazada()  # Crea una lista doblemente enlazada vacia para almacenar las cartas
    
    def poner_carta_arriba(self,carta):
        self.lista.agregar_al_inicio(carta)  # Agrega una carta al principio del mazo (arriba del todo)
    
    def sacar_carta_arriba(self,mostrar=False):
        if self.lista.esta_vacia():
            raise DequeEmptyError("El mazo está vacío")  # Si no hay cartas, lanza error
        
        if mostrar == True:
            self.lista.cabeza.dato.visible = True  # Si mostrar es True, hace visible la carta de arriba
        
        temp = self.lista.cabeza.dato  # Guarda la carta que está arriba del mazo
        self.lista.extraer(0)  # Saca la primera carta (posición 0) del mazo
        return temp  # Devuelve la carta que sacó
    
    def poner_carta_abajo(self,carta):
        self.lista.agregar_al_final(carta)  # Agrega una carta al final del mazo (abajo del todo)
    
    def __len__(self):
        return len(self.lista)  # Devuelve cuántas cartas hay en el mazo


if __name__ == "__main__":
    mazo = Mazo()  # Crea un nuevo mazo vacío
    carta1 = Carta("♣", "3")  # Crea una carta: 3 de trébol
    carta2 = Carta("♦", "A")  # Crea una carta: As de diamantes
    carta3 = Carta("♣", "8")  # Crea una carta: 8 de trébol
    
    
    mazo.poner_carta_arriba(carta1)  # Pone el 3♣ arriba del mazo
    mazo.poner_carta_arriba(carta2)  # Pone el A♦ arriba del 3♣ (ahora el mazo tiene A♦ arriba y 3♣ abajo)

    print(mazo.sacar_carta_arriba())  # Saca la carta de arriba (A♦) y la muestra