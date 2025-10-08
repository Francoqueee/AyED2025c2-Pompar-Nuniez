import heapq

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
            # Intentamos devolver un valor comparable; si no, envolvemos como fallback
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

    def insertar(self, elemento, param1=None, param2=None):
        """
        Inserta un nuevo elemento en el montículo.
        Complejidad: O(log n)
        """
        envuelto = self.empaqueta(elemento)
        heapq.heappush(self.heap, envuelto)

    def eliminar_minimo(self):
        """
        Elimina y devuelve el elemento con menor prioridad (mínimo).
        Complejidad: O(log n)
        """
        if self.esta_vacio():
            raise IndexError("El montículo está vacío")
        envuelto = heapq.heappop(self.heap)
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
        Construye el heap a partir de una lista existente.
        Complejidad: O(n)
        """
        envueltos = [self.empaqueta(e) for e in lista]
        heapq.heapify(envueltos)
        self.heap = envueltos

    def esta_vacio(self):
        return len(self.heap) == 0

    def tamano(self):
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