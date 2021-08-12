import random

def generarcontrasena():
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    numeros = ['1','2','3','4','5','6','7','8','9']
    simbolos = ['!','@','#','$','%','^','&','*','(',')','-']

    caracteres = mayusculas + minusculas + numeros +simbolos

    contrasena = []
    for i in range(15):
        caracterRandom = random.choice(caracteres)
        contrasena.append(caracterRandom)
    
    contrasena = "".join(contrasena)
    return contrasena




def run():
        contrasena = generarcontrasena()
        print("tu nueva contrasena es: " + contrasena)

if __name__ == '__main__': run()