import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('elige el numero de 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('busca un numero mas grande')
        else:
            print('busca un numero mas pequeno')
        numero_elegido = int(input('elige otro numero: '))
    print('ganaste!!!')            


if __name__=='__main__':
    run()