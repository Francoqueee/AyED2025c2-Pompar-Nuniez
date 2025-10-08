from monticulomin import Monticulo
class ColaPrioridad:
    def __init__(self, param1=None, param2=None):
        """
        Inicializa la cola de prioridad.
        param1: función para obtener la prioridad del elemento.
        param2: función para obtener una segunda prioridad en caso de empate.
        """
        self.monticulo = Monticulo(param1, param2)

    def insertar(self, dato, param1=None, param2=None):
        """
        Inserta un nuevo elemento en la cola de prioridad.
        Complejidad: O(log n)
        """
        self.monticulo.insertar(dato, param1, param2)

    def eliminar_minimo(self):
        """
        Elimina y devuelve el elemento con mayor prioridad (mínimo).
        Complejidad: O(log n)
        """
        return self.monticulo.eliminar_minimo()

    def buscar_minimo(self):
        """
        Devuelve el elemento con mayor prioridad sin eliminarlo.
        Complejidad: O(1)
        """
        return self.monticulo.buscar_minimo()

    def esta_vacio(self):
        return self.monticulo.esta_vacio()

    def tamanio(self):
        return self.monticulo.tamanio()

    def __str__(self):
        """
        Muestra los elementos almacenados (solo para depuración).
        """
        return str(self.monticulo)
    
    def __iter__(self): # Método para iterar sobre los elementos de la cola de prioridad
        return iter(self.monticulo)
    