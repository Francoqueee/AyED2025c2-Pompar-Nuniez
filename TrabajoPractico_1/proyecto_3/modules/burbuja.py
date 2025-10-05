def Burbuji(lista):
    # Burbuji hace varias pasadas por la lista. En la primera pasada recorre toda la lista,
    # en la segunda la recorre un poco menos, y así sucesivamente
    for pasada in range(len(lista)-1, 0, -1):
        
        # En cada pasada, Burbuji va comparando cada número con el que tiene a su derecha
        for i in range(pasada):
            
            # Si el número actual es mayor que el siguiente
            if lista[i] > lista[i+1]:
                # Los intercambia: el mayor va a la derecha y el menor a la izquierda
                temp = lista[i+1]       # Guardo temporalmente el número más pequeño
                lista[i+1] = lista[i]   # Pongo el número grande en la posición de la derecha
                lista[i] = temp         # Pongo el número pequeño en la posición de la izquierda
    
    # Cuando termino todas las pasadas, la lista está ordenada
    return lista


if __name__ =="__main__":
    listaprueba = [54321, 81335, 12345, 8, 3030, 99992, 77960, 78, 23456, 78910, 34447, 88812, -1, 56765]
    print(Burbuji(listaprueba))