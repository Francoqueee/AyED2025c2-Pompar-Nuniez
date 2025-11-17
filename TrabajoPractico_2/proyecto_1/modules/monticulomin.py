class Monticulo:
    """
    Implementa un montículo (heap mínimo) genérico con comparación jerárquica.
    Permite definir uno o dos parámetros de prioridad (atributos, índices o claves).
    """

    def __init__(self, param1=None, param2=None):
        self.heap = []               # Lista interna que almacena los elementos en forma de heap
        self.param1 = param1         # Criterio principal de comparación
        self.param2 = param2         # Criterio secundario (opcional)
        self._contador = 0           # Sirve para mantener orden de llegada en empates

    def _obtener_valor(self, elem, param):
        """
        Obtiene el valor de comparación de un elemento según el parámetro dado.
        Admite distintos tipos: objetos, diccionarios, listas o tuplas.
        """
        # Si no hay parámetro, devolvemos el elemento tal cual como clave primaria
        if param is None:
            # Intentamos devolver un valor comparable; si no, envolvemos como fallback (opcion de contingencia)
            try:
                return (0, elem)
            except TypeError:
                return (1, repr(elem))

        # Intención: siempre devolver una tupla (flag, valor) donde flag=0 indica
        # valor 'normal' y flag=1 indica fallback (garantiza que todas las claves sean comparables)

        # Si el elemento es un diccionario
        if isinstance(elem, dict):
            if param in elem:
                val = elem.get(param)
                return (0, val)
            else:
                return (1, float('inf'))

        # Si el parámetro es un índice (lista o tupla o secuencias)
        if isinstance(param, int) and hasattr(elem, '__getitem__'):
            try:
                val = elem[param]
                return (0, val)
            except Exception:
                return (1, float('inf'))

        # Si el parámetro es un nombre de atributo o método
        if isinstance(param, str):
            try:
                attr = getattr(elem, param)
                val = attr() if callable(attr) else attr
                return (0, val)
            except Exception:
                return (1, float('inf'))

        # En cualquier otro caso, intentamos usar el elemento directamente
        try:
            return (0, getattr(elem, param)) if hasattr(elem, param) else (0, elem)
        except Exception:
            return (1, float('inf'))

    def empaqueta(self, elemento):
        """
        Empaqueta el elemento en una tupla que heapq pueda comparar correctamente.
        Si hay dos parámetros de comparación, usa ambos.
        """
        val1 = self._obtener_valor(elemento, self.param1)
        val2 = self._obtener_valor(elemento, self.param2) if self.param2 else None
        self._contador += 1  # evita colisiones entre elementos iguales

        if self.param2 is None:
            return (val1, self._contador, elemento)
        else:
            return (val1, val2, self._contador, elemento)

    def desempaqueta(self, elemento_envuelto):
        """
        Desempaqueta el elemento y devuelve el dato original.
        """
        if self.param2 is None:
            return elemento_envuelto[2]
        else:
            return elemento_envuelto[3]
    def _padre(self, i):
        """Devuelve el índice del padre de i."""
        return (i - 1) // 2

    def _hijo_izq(self, i):
        """Devuelve el índice del hijo izquierdo de i."""
        return 2 * i + 1

    def _hijo_der(self, i):
        """Devuelve el índice del hijo derecho de i."""
        return 2 * i + 2

    def _burbujeo(self, i):
        """
        Mueve el elemento en el índice i hacia arriba (hacia la raíz)
        mientras sea menor que su padre, para mantener la propiedad del heap.
        Usado en 'insertar'.
        """
        padre = self._padre(i)
        
        # 
        
        # Mientras no lleguemos a la raíz (i > 0) y el hijo sea menor que el padre
        while i > 0 and self.heap[i] < self.heap[padre]:
            # Intercambiamos hijo y padre
            self.heap[i], self.heap[padre] = self.heap[padre], self.heap[i]
            # Ahora el elemento está en la posición 'padre'
            i = padre
            padre = self._padre(i)

    def _hundir(self, i):
        """
        Mueve el elemento en el índice i hacia abajo (hacia las hojas)
        mientras sea mayor que el menor de sus hijos, para mantener la
        propiedad del heap. Usado en 'eliminar_minimo' y 'construir_monticulo'.
        """
        n = len(self.heap)
        
        # 

        while True:
            min_idx = i # Suponemos que el padre es el mínimo
            izq = self._hijo_izq(i)
            der = self._hijo_der(i)

            # Comprobar si el hijo izquierdo existe y es menor que el padre
            if izq < n and self.heap[izq] < self.heap[min_idx]:
                min_idx = izq

            # Comprobar si el hijo derecho existe y es menor que el
            # (actual) mínimo (que podría ser el padre o el hijo izq)
            if der < n and self.heap[der] < self.heap[min_idx]:
                min_idx = der

            # Si el mínimo sigue siendo el padre (i), el elemento está
            # en su lugar correcto y terminamos.
            if min_idx == i:
                break

            # Intercambiamos el padre con el hijo menor
            self.heap[i], self.heap[min_idx] = self.heap[min_idx], self.heap[i]
            
            # Continuamos hundiendo desde la nueva posición del hijo
            i = min_idx

    def insertar(self, elemento, param1=None, param2=None):
        """
        Inserta un nuevo elemento en el montículo.
        Complejidad: O(log n)
        """
        envuelto = self.empaqueta(elemento)
        self.heap.append(envuelto)
        self._burbujeo(len(self.heap) - 1)
    def eliminar_minimo(self):
        """
        Elimina y devuelve el elemento con menor prioridad (mínimo).
        Complejidad: O(log n)
        """
        if self.esta_vacio():
            raise IndexError("El montículo está vacío")
        n = len(self.heap)
            
        if n == 1:
            # Si solo hay un elemento, lo sacamos y listo
            envuelto = self.heap.pop()
        else:
            # 1. Guardamos el mínimo (la raíz) para devolverlo
            envuelto = self.heap[0]
            # 2. Movemos el último elemento a la raíz
            self.heap[0] = self.heap.pop()
            # 3. "Hundimos" la nueva raíz a su posición correcta
            self._hundir(0)
        return self.desempaqueta(envuelto)

    def buscar_minimo(self):
        """
        Devuelve el elemento mínimo sin eliminarlo.
        Complejidad: O(1)
        """
        if self.esta_vacio():
            return None
        return self.desempaqueta(self.heap[0])

    def construir_monticulo(self, lista):
        """
        Construye el heap a partir de una lista existente (método "heapify").
        Complejidad: O(n)
        """
        # 1. Empaquetamos todos los elementos
        envueltos = [self.empaqueta(e) for e in lista]
        self.heap = envueltos
        n = len(self.heap)

        # 2. Comenzamos desde el último nodo no-hoja
        # (el padre del último elemento)
        # y "hundimos" cada uno hacia arriba hasta la raíz.
        start_idx = (n // 2) - 1
        
        for i in range(start_idx, -1, -1):
            self._hundir(i)

    def esta_vacio(self):
        return len(self.heap) == 0

    def tamanio(self):
        return len(self.heap)

    def __str__(self):
        """
        Muestra los elementos almacenados (solo para depuración).
        """
        elementos = [self.desempaqueta(e) for e in self.heap]
        return f"Monticulo({elementos})"
    def __iter__(self):
        """
        Iterador para recorrer los elementos del montículo.
        """
        for elemento in self.heap:
            yield self.desempaqueta(elemento)
if __name__ == "__main__":
    
    print("PRUEBA 1: Números simples (param1=None)")
    
    # Probamos construir_monticulo e insertar
    heap_num = Monticulo(param1=None)
    heap_num.construir_monticulo([10, 5, 20, 8])
    heap_num.insertar(3)
    heap_num.insertar(12)
    
    print(f"Estado del heap (interno): {heap_num.heap}")
    print(f"Mínimo actual: {heap_num.buscar_minimo()}")
    
    print("Extrayendo todos los elementos en orden:")
    while not heap_num.esta_vacio():
        print(f"Eliminado: {heap_num.eliminar_minimo()}", end=" | ")
    print("FIN\n")

    
    # ---
    
    # Clase de ejemplo para la Prueba 2
    class Nodo:
        def __init__(self, nombre, distancia):
            self.nombre = nombre
            self.distancia = distancia
        def __repr__(self):
            # Una representación amigable para imprimir
            return f"Nodo({self.nombre}, dist={self.distancia})"

    print("PRUEBA 2: Objetos (param1='distancia')")
    heap_nodos = Monticulo(param1='distancia')
    heap_nodos.insertar(Nodo('A', 100))
    heap_nodos.insertar(Nodo('B', 10))
    heap_nodos.insertar(Nodo('C', 50))
    heap_nodos.insertar(Nodo('D', 5)) # Este debe ser el mínimo

    print(f"Mínimo actual: {heap_nodos.buscar_minimo()}")
    
    print("Extrayendo todos los elementos en orden:")
    while not heap_nodos.esta_vacio():
        print(f"Eliminado: {heap_nodos.eliminar_minimo()}", end=" | ")
    print("FIN\n")

    
    # ---
    
    print("PRUEBA 3: Diccionarios (Doble prioridad: 'puntaje' y 'nombre')")
    # Prioridad 1: 'puntaje' (mínimo)
    # Prioridad 2: 'nombre' (alfabético, como desempate)
    heap_dict = Monticulo(param1='puntaje', param2='nombre')

    lista_items = [
        {'nombre': 'Zelda', 'puntaje': 100},
        {'nombre': 'Mario', 'puntaje': 50},
        {'nombre': 'Link', 'puntaje': 100}, # Empate en puntaje con Zelda
        {'nombre': 'Bowser', 'puntaje': 50}  # Empate en puntaje con Mario
    ]
    heap_dict.construir_monticulo(lista_items)
    
    print(f"Mínimo actual: {heap_dict.buscar_minimo()}") # Debería ser Bowser
    
    print("Extrayendo todos los elementos en orden:")
    # Debería salir: Bowser (50), Mario (50), Link (100), Zelda (100)
    while not heap_dict.esta_vacio():
        print(f"Eliminado: {heap_dict.eliminar_minimo()}")
    print("FIN\n")
    
    # ---
    print("PRUEBA 4: Tuplas (Prioridad por índice 1)")
    
    # Queremos ordenar por el segundo ítem de la tupla (el número)
    heap_tuplas = Monticulo(param1=1) 
    
    lista_tuplas = [('Manzana', 10), ('Banana', 2), ('Naranja', 15), ('Uva', 1)]
    heap_tuplas.construir_monticulo(lista_tuplas)
    
    print(f"Mínimo actual: {heap_tuplas.buscar_minimo()}") # Debería ser ('Uva', 1)

    print("Extrayendo todos los elementos en orden:")
    while not heap_tuplas.esta_vacio():
        print(f"Eliminado: {heap_tuplas.eliminar_minimo()}", end=" | ")
    print("FIN\n")