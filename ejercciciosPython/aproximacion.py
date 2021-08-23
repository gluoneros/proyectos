objetivo = int(input('escoge un numero: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while   abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    