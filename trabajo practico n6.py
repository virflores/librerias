#ejercicio 1
import math
def redondear(numero):
    if numero > 3.50:
        return math.ceil(numero)
    else:
        return math.floor(numero)
print(redondear(3.49))  
print(redondear(3.50))  
print(redondear(3.51))  
print(redondear(4.00))  

#ejercicio 2
from modulos_1 import redondear2 
def suma_y_redondea(a, b):
    suma = a + b
    return redondear2(suma)
print(suma_y_redondea(1.2, 2.3))  
print(suma_y_redondea(1.8, 2.0))  
print(suma_y_redondea(2.0, 2.0))  


#ejercicio 3
from datetime import datetime
def fecha_hora():
    fecha_hora_actual = datetime.now()
    fecha_hora_formateada = fecha_hora_actual.strftime("%y-%m-%d %H:%M:%S")
    print("Fecha y hora actuales del sistema:", fecha_hora_formateada)
fecha_hora()

#ejercicio 4
import random
def numero_azar():
    return random.choice([2, 4, 6, 8, 10])
print(numero_azar())
def comprobar_todos_los_pares():
    encontrados = set()
    while len(encontrados) < 5:
        numero = numero_azar()
        print(f"Número generado: {numero}")
        encontrados.add(numero)
        print(f"Números encontrados hasta ahora: {encontrados}")
    print("Se han generado todos los números pares entre 2 y 10.")
comprobar_todos_los_pares()

#ejercicio 5
import random
def bola_magica():
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    return random.choice(respuestas)
def consulta():
    while True:
        pregunta = input("Haz una pregunta a la bola mágica (o escribe 'salir' para terminar): ")
        if pregunta.lower() == 'salir':
            print("Gracias por jugar con la bola mágica.")
            break
        respuesta = bola_magica()
        print(f"La bola mágica dice: {respuesta}")
consulta()

#ejercicio 6
import time
from datetime import datetime
def mostrar_fecha_hora_actual():
    start_time = time.time()
    fecha_hora_actual = datetime.now()
    fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
    print("Fecha y hora actuales del sistema:", fecha_hora_formateada)
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
mostrar_fecha_hora_actual()

#ejercicio 7
import random
def sorteo(participantes, num_ganadores):
    if num_ganadores > len(participantes):
        print("El número de ganadores no puede ser mayor que el número de participantes.")
        return []
    ganadores = random.sample(participantes, num_ganadores)
    return ganadores
def cuerpo_principal():
    participantes = [
        "Ana", "Luis", "Carlos", "Marta", "Elena", "Juan", "Lucía", "Pedro", "Laura", "Andrés"
    ]
    num_ganadores = int(input("Ingrese el número de ganadores: "))
    ganadores = sorteo(participantes, num_ganadores)
    if ganadores:
        print("Los ganadores del sorteo son:")
        for ganador in ganadores:
            print(ganador)
cuerpo_principal()

#ejercicio 8
from datetime import datetime
def calcular_dias_desde_nacimiento():
    fecha_nacimiento_str = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
    try:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")
    except ValueError:
        print("Formato de fecha incorrecto. Por favor, use el formato YYYY-MM-DD.")
        return
    fecha_actual = datetime.now()
    diferencia_dias = (fecha_actual - fecha_nacimiento).days
    print(f"Han pasado {diferencia_dias} días desde su nacimiento.")
calcular_dias_desde_nacimiento()
