while True:  
        try:
            referenceLife(input(int("Ingrese la cantidad de vida con la quiera iniciar, esto puede hacer variar la duracion de las partidad (Ingrese 300 o 400 para una duracion normal) ")))
            break
        except:
            print("Solo puedes poner numeros enteros")
            spc()