from random import randint
import time
from LDE import ListaDobleEnlazada

def medir_tiempos_len(tamanos):
    # Mide cuanto tarda la funcion len() en listas de diferentes tamaños
    tiempos_len= []

    for n in tamanos:
        # Crear lista con n elementos aleatorios
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 1000))
            
        # Cronometrar el tiempo de len(lista)
        inicio = time.perf_counter()
        len(lista)
        fin = time.perf_counter()
        tiempos_len.append(fin - inicio)
   #     print(f"Tiempo de funcion len para n={n}: {fin - inicio:.10f} segundos")
    
    return tiempos_len  

def medir_tiempos_copia(tamanos):
    # Mide cuanto tarda la funcion copiar() en listas de diferentes tamaños
    tiempos_copia = []
    
    for n in tamanos:
        # Crear lista con n elementos random
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 1000))
        
        # Cronometrar el tiempo de lista.copiar()
        inicio = time.perf_counter()
        aux_lista = lista.copiar()
        fin = time.perf_counter()
        tiempos_copia.append(fin - inicio)
  #      print(f"Tiempo de funcion copia para n={n}: {fin - inicio:.10f} segundos")
    
    return tiempos_copia

def medir_tiempos_invertir(tamanos):
    # Mide cuanto tarda la funcion invertir() en listas de diferentes tamaños
    tiempos_invertir = []
    
    for n in tamanos:
        # Crear lista con n elementos random
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 1000))
        
        # Cronometrar el tiempo de lista.invertir()
        inicio = time.perf_counter()
        lista.invertir()
        fin = time.perf_counter()
        tiempos_invertir.append(fin - inicio)
      #  print(f"Tiempo de funcion invertir para n={n}: {fin - inicio:.10f} segundos")
    
    return tiempos_invertir
        
if __name__ == '__main__':
    # Tamaños de lista que vamos a probar
    tamanos = [1, 10, 100, 200, 500, 700, 1000, 1000000]
    
    # Llamar a las funciones para medir tiempos
    medir_tiempos_len(tamanos)      # Prueba la funcion len()
    
    medir_tiempos_copia(tamanos)    # Prueba la funcion copiar()
    
    medir_tiempos_invertir(tamanos) # Prueba la funcion invertir()