# A partir de un valor pivote, ordena parcialmente, donde los valores menores al pivote quedan a la izquierda y los mayores, a la derecha. 
# Modifica la lista y devuelve el punto de division (ubicacion del pivote)
# En resumen, divido la lista en 3 partes: los menores al pivote, el pivote, y los mayores al pivote
def particion(lista,primero,ultimo):
    #Tomamos el primer elemento de la lista como el valor pivote
    valorPivote = lista[primero]

    # marcaIzq inicia como el indice del elemento que le sigue al valor pivote 
    # Es una variable creciente, varia como indice de la lista y compara el valor correspondiente de la lista con el pivote
    marcaIzq = primero+1

    # marcaDer inicia como el indice del ultimo elemento de la lista
    # Es una variable decreciente, varia como indice de la lista y compara el valor correspondiente de la lista con el pivote
    marcaDer = ultimo

    vuelta_completa = False
    while not vuelta_completa:
        # La marcaizq se va a mover hasta que su valor correspondiente en la lista sea mayor al valor pivote o que sea igual o mayor a la marca derecha
        while marcaIzq <= marcaDer and lista[marcaIzq] <= valorPivote:
            marcaIzq = marcaIzq + 1
        # La marcader se va a mover hasta que su valor correspondiente en la lista sea menor al valor pivote o que sea igual o menor a la marca izquierda
        while lista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
            marcaDer = marcaDer -1
        # Al terminar si las marcas se cruzan es pq ya estan parcialmente ordenados los elementos, con los menores a la izquierda y los mayores a la derecha del pivote
        if marcaDer < marcaIzq:
            vuelta_completa = True
        # Si las marcas no se cruzaron, intercambiamos los valores asociados.
        else:
            temp = lista[marcaIzq]
            lista[marcaIzq] = lista[marcaDer]
            lista[marcaDer] = temp

# intercambia los valores del elemento correspondiente a la marca derecha y el del pivote
    temp = lista[primero]
    lista[primero] = lista[marcaDer]
    lista[marcaDer] = temp


    return marcaDer

# este modulo maneja la recursión y controla QUÉ PARTE de la lista ordenar.
def ordenamientoRapidoAuxiliar(lista,primero,ultimo):
    if primero<ultimo:

        #la funcion particion ordena parcialmente la lista y retorna el punto de division
        puntoDivision = particion(lista,primero,ultimo)

        #llamamos recursivamente a la funcion dos veces con la parte previa y siguiente al punto de division como indices
        ordenamientoRapidoAuxiliar(lista,primero,puntoDivision-1)
        ordenamientoRapidoAuxiliar(lista,puntoDivision+1,ultimo)

# Esta seria la interfaz limpia para el usuario
# solo recibe la lista y hace el primer llamado con los indices iniciales (0 y último)
def ordenamientoRapido(lista):
    # primer llamado a la funcion auxiliar
    ordenamientoRapidoAuxiliar(lista,0,len(lista)-1)


if __name__ == "__main__":
    from random import randint
    listaprueba = [randint(10000,99999) for _ in range(15)]
    ordenamientoRapido(listaprueba)
    print(listaprueba)