distancia = int(input('Distancia de control: '))
hora = int(input('Hora de llegada: '))
minutos = int(input('Minutos de llegada: '))
velocidad = float(input('Cual es tu objetivo?: '))
def calcular_tiempo(hora,minuto):
    horaDePartida = 8 # Hora de partida de la competencia
    lista = [] # lista para almacenar las horas de llegada del competidor
    for i in range(horaDePartida,hora): # bucle que recorre un rango entre la hora de partida y la hora de llegada
        lista.append(i) # metodo que introduce el rango a una lista
    minutos = (len(lista) * 60) + minuto # calculo para transformar la hora de llegada a minutos
    return int(minutos)

def calcular_ritmo(distancia,minutos):
    return int(minutos/distancia)
    
# Compara la velocidad propuesta con la que va el atleta
if velocidad < calcular_ritmo(distancia,calcular_tiempo(hora,minutos)):
    print(f'Debes apresurarte a ese ritmo llegaras en {float(calcular_ritmo(distancia,calcular_tiempo(hora,minutos)))-1/velocidad} horas')
elif velocidad >= calcular_ritmo(distancia,calcular_tiempo(hora,minutos)):
    res = (calcular_ritmo(distancia,calcular_tiempo(hora,minutos))/velocidad) * 60 # calcula a mintos
    print(f'Vas bien deberias llegar en {int(res)} minutos.') 

