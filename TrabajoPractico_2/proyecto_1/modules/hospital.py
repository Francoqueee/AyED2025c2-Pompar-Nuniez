# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import modules.paciente as pac
import modules.colaprioridad as cp
import random

n = 20  # cantidad de ciclos de simulación

cola_de_espera = cp.ColaPrioridad()

# Ciclo que gestiona la simulación
for i in range(n):

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente()
    cola_de_espera.insertar(dato=paciente, param1= 'get_riesgo', param2= 'get_hora_llegada')

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.eliminar_minimo()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', cola_de_espera.tamano())
    for paciente in cola_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)
