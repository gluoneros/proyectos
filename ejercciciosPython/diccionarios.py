def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    #print(mi_diccionario['llave1'])
    #print(mi_diccionario['llave2'])
    #print(mi_diccionario['llave3'])
    
    poblacion_pais = {
        'argentina': 4498333,
        'brasil': 67273637,
        'colombia': 499000,
    }
    #print(poblacio_pais['colombia'])

    for pais, poblacion in poblacion_pais.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__': run()