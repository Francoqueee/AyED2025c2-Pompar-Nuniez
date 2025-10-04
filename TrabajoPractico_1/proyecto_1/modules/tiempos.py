from random import randint
import time

def medir_tiempos(metodo_ordenamiento, tamanos_lista):
    # Esta funcion mide cuanto tarda un 'metodo de ordenamiento' en ordenar listas de diferentes tamaños
    tiempos_resultado = []  # Aquí guardaremos todos los tiempos que midamos

    for tamaño in tamanos_lista:
        # Creo una lista con números aleatorios del tamaño que estoy probando
        numeros_aleatorios = [randint(10000, 99999) for _ in range(tamaño)]  # Números de 5 digitos como dice la consigna

        # Mido el tiempo exacto antes de empezar a ordenar
        inicio_tiempo = time.perf_counter()
        
        # Llamo al metodo de ordenamiento que quiero probar
        metodo_ordenamiento(numeros_aleatorios)
        
        # Mido el tiempo exacto después de terminar de ordenar
        fin_tiempo = time.perf_counter()
        
        # Calculo cuanto tiempo tardo en ordenar
        tiempo_transcurrido = fin_tiempo - inicio_tiempo
        tiempos_resultado.append(tiempo_transcurrido)
        
        # Muestro por pantalla el resultado de esta prueba
        print(f"El método {metodo_ordenamiento.__name__} tardó {tiempo_transcurrido:.6f} segundos para ordenar {tamaño} números")
    
    # Devuelvo la lista con todos los tiempos medidos
    return tiempos_resultado

if __name__ == '__main__':
    # Estos son los tamaños de lista que voy a probar: desde 1 hasta 1000 números
    tamaños_a_probar = [1, 10, 100, 200, 500, 700, 1000]
    
    # Mido cuánto tarda la función sorted de Python en ordenar cada lista
    medir_tiempos(sorted, tamaños_a_probar)