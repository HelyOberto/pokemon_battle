import random
import time

## Funciones de texto
def spc():
    print("----------------------")
    
def hide():
    for x in range(0, 100):
        print("--------------------------------")
    
def stop(segundos):
    global flashmode
    time.sleep(segundos * flashmode)
    
def ask():
    input(" Ingrese 'Enter' para continuar ")
    spc()

## Inicializador de vida
    
def referenceLife(initialLife):
    global player
    global player2
    
    player[5] = initialLife
    player[6] = initialLife
    player2[5] = initialLife
    player2[6] = initialLife

## dificultades

difficulty = 0
difficultyInfo = ["1. Facil: El enemigo empieza con la mitad de de vida que tu", "2. Normal: Los 2 empiezan con la misma vida", "3. Dificil: Tu rival empieza con %50 de vida mas", "4. Muy dificil: Tu rival empieza con el doble de vida", "5. Insano: Tu rival tiene 3 veces mas vida que tu"]

def Xdifficulty(multiplier):
    global player2
    global player
    
    player2[5] = int(player2[5] * multiplier)
    player2[6] = player2[5]
    if player2[5] > player[5]:
        player[5] = player2[5]
    else:
        player2[5] = player[5]

## Lista de pokemones
pokemons = []

## 1) Volcanus

volcanusAtks = ["Bola de fuego", "Rencor", "Recalentar", "Barrera de magma"]
volcaunusAtksNum = [40, 80, 35, 45]

volcanus = ["Volcanus", volcanusAtks, volcaunusAtksNum]
pokemons.append(volcanus)

## 2) Watwo

watwoAtks = ["Chorro de agua", "Venganza", "Hidrolisis", "Pared de cascada"]
watwoAtksNum = [35, 85, 40, 50]

watwo = ["Watwo", watwoAtks, watwoAtksNum]
pokemons.append(watwo)

## 3) Gife

gifeAtks = ["Estocada", "Concentracion solar", "Fotosintesis", "Escudo de hojas"]
gifeAtksNum =  [30, 75, 50, 60]

gife = ["Gife", gifeAtks, gifeAtksNum]
pokemons.append(gife)

## Informacion de cada pokemon

def pokemonsInfo(info):
    match info:
        case 1:
            print("Volcanus es un pokemon de tipo fuego hecho de magma con forma humanoide, nomalmente encontrado en lugares con actividad volcania")
            spc()
            ask()
            print("Sus movmientos son:")
            spc()
            print("Bola de fuego: A traves de la acomulacion de calor en la palma de sus manos, Volcanus es capaz de generar bolas de fuego que quitan 40 puntos de vida a su rival")
            spc()
            ask()
            print("Rencor: Volcanus acomula fuego dentro de si durante un turno, dejandose golpear, para en el siguiente liberarlo quitando 60 puntos de vida su rival")
            spc()
            ask()
            print("Recalentar: Volcanus recupera 30 puntos de vida a travez de reabsorcion de su calor emitido")
            spc()
            ask()
            print("Barrera de fuego: Volcanus se cubre de recibir el 40% daño durante ese turno ")
            spc()
            ask()

        case 2:
            print("Watwo es un pokemon de tipo agua con forma de pez gigante dentro de una esfera de agua controlada por el mismo, nomalmente encontrado en profundos lagos")
            spc()
            ask()
            print("Sus movmientos son:")
            spc()
            ask()
            print("Chorro de agua: Watwo acomula agua en alta presion con el fin de disparlare al rivas quitandole 35 puntos de vida")
            spc()
            ask()
            print("Venganza: Watwo concentra la presion del agua dentro de durante un turno, dejandose golpear, para despues liberarla quitandole asu rival 50 puntos de vida")
            spc()
            ask()
            print("Hidrolisis: Watwo absorve la energia de los enlaces del agua para recupuar 40 punto de vida")
            spc()
            ask()
            print("Pared de cascada: Watwo se cubre de recibir el 50% daño durante ese turno  ")
            spc()
            ask()

        case 3:
            print("Gife es un pokemon de tipo planta con forma de arbol viviente que se arrastra a travez de sus raices, nomalmente encontrado en las profundidades de los bosques")
            spc()
            ask()
            print("Sus movmientos son:")
            spc()
            ask()
            print("Estocada: Gife usas sus ramas para apuñalar a su rival, quitandole 30 puntos de vida ")
            spc()
            ask()
            print("Concentracion solar: Gife cocentra la luz del sol durante un turno, dejandose golpear, para liberarla en el sigueinte quitanole 50 puntos de vida al rival ")
            spc()
            ask()
            print("Fotosintesis: Gife absorve la luz solar para recuperar 50 puntos de vida")
            spc()
            ask()
            print("Escudo de hojas: Gife se cubre de recibir el 60% daño duarante ese turno  ")
            spc()
            ask()
    
    
while True:
    
    ## Variables del jugador

    name = ""
    pokemon = 0
    atks = []
    atksNum = []
    election = 0
    maxLife = 0
    life = 0
    effect = False
    shield = False

    player = [name, pokemon, atks, atksNum, election, maxLife, life, effect, shield]
    
    clarification = ""

    nick = ""
    ## Variables de IA

    enmName = "la IA"
    enmPokemon = 0
    enmAtks = []
    enmAtksNum = []
    enmElection = 0
    enmMaxLife = 0
    enmLife = 0
    enmEffect = False
    enmShield = False

    player2 = [enmName, enmPokemon, enmAtks, enmAtksNum, enmElection, enmMaxLife, enmLife, enmEffect, enmShield]
    
    posibilidad = []
    clarification2 = ""
 
    ## Extra
    
    info = ""
    restart = ""
    start = ""
    flashmode = 1
    luck = [20, 90]
    pokemonInList = False
    AI = True
    critical = 1
        
    ## Introduccion
    
    player[0] = str(input("Ingresa tu nombre: "))
    
    nick = player[0].lower()
    
    if nick ==  "flash":
        flashmode = 0
    elif nick == "luckoff":
        luck[0] = 0
        luck [1] = 100
    
    if nick == "sika" or nick == "hely":
        print("Bienvenido de nuevo, padre :)")
        stop(1)
        spc()
    elif nick == "osly":
        print("Feliz aniversario amooooor")
        stop(1)
        spc()  
    else:
        print("Bienvenid@", player[0], "al simulador de peleas pokemon!")
        stop(1)
        print("Hecho por: Hely")
        stop(1)
        spc()
        
        
    if input("Ingrese '1' para jugar contra la maquina, ingrese '2' para el modo jugador vs jugador ") == "2":
        AI = False
        spc()
        player2[0] = input("Ingrese el nombre del jugador 2 ")
        
        while player[0] == player2[0]:
            print("No puedes usar el mismo nombre que el otro jugador")
            player2[0] = input("Ingrese el nombre del jugador 2 ")
        
        spc()
        
        
        stop(0.5)
    referenceLife(int(input("Ingrese la cantidad de vida con la quiera iniciar, esto puede hacer variar la duracion de las partidad (Ingrese 300 o 400 para una duracion normal) ")))
    spc()
    
    if AI == True:
        if nick != "osmio" and nick != "oscar":
            print("Elige la dificultad")
            spc()
            
            for x in difficultyInfo:
                print(x)
                
            spc()
            difficulty = input("Selecciona la dificultad por su numero ")
            
            while difficulty != "1" and difficulty != "2" and difficulty != "3" and difficulty != "4" and difficulty != "5":
                spc()
                print("Valor no valido")
                difficulty = input("Selecciona la dificultad por su numero ")
                
            difficulty = int(difficulty)
        
        else:
            difficulty = 6
        
        match difficulty:
            case 1:
                Xdifficulty(0.5)
            case 2:
                Xdifficulty(1)
            case 3:
                Xdifficulty(1.5)
            case 4:
                Xdifficulty(2)
            case 5:
                Xdifficulty(3)
            case 6:
                Xdifficulty(10)
                print("Dificultad", player[0], "activada")
                stop(1)
        spc()
        

    while start != "1":
        pokemonInList = False
        
        for e in range(0, len(pokemons)):
            print(f"{e + 1}. {pokemons[e][0]}")

        player[1] = input(f"{player[0]}, elige tu pokemon segun su numero ")

        while True:
            for x in range(0, len(pokemons)):
                if str(x + 1) == player[1]:
                    pokemonInList = True
                    break
                
            if pokemonInList == True:
                break
            else:
                print("Opcion no valida")
                player[1] = input("Elija el pokemon que desee segun su numero ")
        
        player[1] = int(player[1])
        spc()
        
        info = input(f"Ingrese '0' saber informacion de {(pokemons[player[1] - 1][0] + clarification)}, cualquier otro para omitir ")
        
        if info == "0":
            pokemonsInfo(player[1])
                    
        player[2] = pokemons[player[1] - 1][1]
        player[3] = pokemons[player[1] - 1][2]

                    
        start = input(f"Quieres quedarte con {(pokemons[player[1] - 1][0] + clarification)}? Ingrese 1 para quedartelo, 0 para volver a elegir ")
        while start != "1" and start != "0":
            start = input("Valor no valido, intente de nuevo ")
        spc()

    start = "0"
    
    if AI == False:
        while start != "1":
            pokemonInList = False
            
            for e in range(0, len(pokemons)):
                print(f"{e + 1}. {pokemons[e][0]}")

            player2[1] = input(f"{player2[0]}, elige tu pokemon segun su numero ")

            while True:
                for x in range(0, len(pokemons)):
                    if str(x + 1) == player2[1]:
                        pokemonInList = True
                        break
                    
                if pokemonInList == True:
                    break
                else:
                    print("Opcion no valida")
                    player[1] = input("Elija el pokemon que desee segun su numero ")
            
            player2[1] = int(player2[1])
            spc()
            
            info = input(f"Ingrese '0' saber informacion de {(pokemons[player2[1] - 1][0] + clarification2)}, cualquier otro para omitir ")
            
            if info == "0":
                pokemonsInfo(player2[1])
                        
            player2[2] = pokemons[player2[1] - 1][1]
            player2[3] = pokemons[player2[1] - 1][2]

                        
            start = input(f"Quieres quedarte con {(pokemons[player2[1] - 1][0] + clarification2)}? Ingrese 1 para quedartelo, 0 para volver a elegir ")
            while start != "1" and start != "0":
                start = input("Valor no valido, intente de nuevo ")
            spc()
    else: 
        player2[1] = random.randrange(1,4)

        while player[1] == player2[1]:
            player2[1] = random.randrange(1,4)

        player2[2] = pokemons[player2[1] - 1][1]
        player2[3] = pokemons[player2[1] - 1][2]
        
        
    print("La batalla comienza!")
    stop(1)
    spc()
    print(f"{player[0]} elige a", (pokemons[player[1] - 1][0]))
    stop(1)
    print(f"{player2[0]} elije a", (pokemons[player2[1] - 1][0]) )
    stop(1)
    spc()
    print(f"Empieza {player[0]}!")
    stop(1)
    
    if player[1] == player2[1]:
        clarification = " de " + player[0]
        clarification2 = " de " + player2[0]

    while True:
        
        print(f"Vida de {(pokemons[player[1] - 1][0] + clarification)}: {player[6]} Vida de {(pokemons[player2[1] - 1][0] + clarification2)}: {player2[6]}")
        spc()

        ## Desiciones de moviemientos
            
        if player[7] == False:
            if AI != True:
                print("Turno del jugador 1")
                spc()
            print(player[0] + ", que quieres que haga", pokemons[player[1] - 1][0] + "?")
            stop(1)
            spc()

            for x in range(0,4):
                print(str(x + 1) + ".", player[2][x])
            spc()
             
                        
            player[4] = input("Seleccione el movimiento que quiera usar por su numero ")
            spc()
            
            
            while (player[4] != "1" and player[4] != "2" and player[4] != "3" and player[4] != "4") or (player[4] == "3" and player[6] == player[5]):
                if player[4] == "3" and player[6] == player[5]:
                    print("Ya tienes la vida llena",player[0] +", intenta otro movimiento")
                else:
                    print("Valor no valido")
                player[4] = input("Seleccione el movimiento que quiera usar por su numero ")
                spc()

            player[4] = int(player[4])
        
        if player2[7] == False:
            if AI == True:       
                while True:
                    if player2[6] == (player2[5]*0.5):
                        posibilidad1 = [25, 50, 75, 100]
                    elif player2[6] < (player2[5]*0.5) and player2[6] > (player2[5]*0.3):
                        posibilidad1 = [20, 40, 70, 100]
                    elif player2[6] < (player2[5]*0.3) and player2[6] > (player2[5]*0.1):
                        posibilidad1 = [15, 30, 65, 100]
                    elif player2[6] < (player2[5]*0.1):
                        posibilidad1 = [10, 20, 60, 100]
                    elif player2[6] > (player2[5]*0.5) and player2[6] < (player2[5]*0.8):
                        posibilidad1 = [30, 60, 80, 100]
                    else:
                        posibilidad1 = [40, 80, 90, 100]

                    if player[6] == (player[5]*0.5):
                        posibilidad2 = [25, 50, 75, 100]
                    elif player[6] < (player[5]*0.5) and player[6] > (player[5]*0.3):
                        posibilidad2 = [30, 60, 80, 100]
                    elif player[6] < (player[5]*0.1):
                        posibilidad2 =  [40, 80, 90, 100]
                    elif player[6] > (player[5]*0.5) and player[6] < (player[5]*0.8):
                        posibilidad2 = [20, 40, 70, 100] 
                    else:
                        posibilidad2 = [10, 20, 60, 100]
                    
                    for x in range(0, len(posibilidad1)):
                        posibilidad.append(int((posibilidad1[x] + posibilidad2[x])/2))

                    rand = random.randrange(1,101)

                    if player2[3][0] >= player[6] or (rand > 0 and rand < posibilidad[0]):
                        player2[4] = 1
                    elif rand > posibilidad[0] and rand < posibilidad[1]:
                        player2[4] = 2
                    elif rand > posibilidad[1] and rand < posibilidad[2]:
                        player2[4] = 3
                    elif rand > posibilidad[2]:
                        player2[4] = 4

                    posibilidad = []
                    if player2[4] == 3 and (player2[6] + player2[3][2] ) >  player2[5]:
                        continue
                    break
            
            else:
                hide()
                print(f"Vida de {(pokemons[player[1] - 1][0] + clarification)}: {player[6]} Vida de {(pokemons[player2[1] - 1][0] + clarification2)}: {player2[6]}")
                spc()
                print("Turno del jugador 2")
                spc()
                print(player2[0] + ", que quieres que haga", pokemons[player2[1] - 1][0] + "?")
                stop(1)
                spc()

                for x in range(0,4):
                    print(str(x + 1) + ".", player2[2][x])
                spc()
             
                        
                player2[4] = input("Seleccione el movimiento que quiera usar por su numero ")
                spc()
            
            
                while (player2[4] != "1" and player2[4] != "2" and player2[4] != "3" and player2[4] != "4") or (player2[4] == "3" and player2[6] == player2[5]):
                    if player2[4] == "3" and player2[6] == player2[5]:
                        print("Ya tienes la vida llena",player2[0] +", intenta otro movimiento")
                    else:
                        print("Valor no valido")
                        
                    player2[4] = input("Seleccione el movimiento que quiera usar por su numero ")
                    spc()

                player2[4] = int(player2[4])
        
        if player[4] == 4:
            player[8] = True
            print((pokemons[player[1] - 1][0] + clarification), "2se cubrio con",player[2][3])
            stop(1)
                
        if player2[4] == 4:
            player2[8] = True
            print((pokemons[player2[1] - 1][0] + clarification2), "se cubrio con",player2[2][3])
            spc()
            stop(1)
        
        if player[7] == False:    
            match player[4]:
                case 1:
                    if random.randrange(1,101) <= luck[0]:
                        print((pokemons[player[1] - 1][0] + clarification), "utilizó " + str(player[2][0]) + ", pero falló")
                        
                    elif player2[8] != True:
                        if random.randrange(1, 101) >= luck[1]:
                            print("Ataque critico!")
                            critical = 2    
                        player2[6] -= (player[3][0] * critical)
                        print((pokemons[player[1] - 1][0] + clarification), "utilizo",player[2][0], "quitandole", (player[3][0] * critical), "de vida a", (pokemons[player2[1] - 1][0] + clarification2))
                    else:
                        if random.randrange(1, 101) >= luck[1]:
                            print("Ataque critico!")
                            critical = 2
                        player2[6] -= int((player[3][0] * critical) * ((100 - player2[3][3]) / 100))
                        print((pokemons[player[1] - 1][0] + clarification), "utilizo",player[2][0], "pero al estar",(pokemons[player2[1] - 1][0] + clarification2),"cubierto, solo le quito", int((player[3][0] * critical) * ((100 - player2[3][3]) / 100)), "de vida a tu rival")
                case 2:
                    player[7] = True
                    print((pokemons[player[1] - 1][0] + clarification), "utilizo",player[2][1], "llenandose de energia")
                case 3:    
                    if player[6] + player[3][2] < player[5]:
                        player[6] += player[3][2]
                        print((pokemons[player[1] - 1][0] + clarification), "utilizo",player[2][2], "recuperando", player[3][2], "de vida")
                    else:
                        player[6] = player[5]
                        print((pokemons[player[1] - 1][0] + clarification), "Recuperó toda la vida")
            
        else:
            if random.randrange(1,101) <= luck[0]:
                print((pokemons[player[1] - 1][0] + clarification), "Libero la energia contenida, pero fallo")    
            elif player2[8] != True:
                player2[6] -= player[3][1]
                print((pokemons[player[1] - 1][0] + clarification), "Libero la energia contenida quitandole", player[3][1], " de vida a", (pokemons[player2[1] - 1][0] + clarification2))
            else:
                player2[6] -= int(player[3][1] * ((100 - player2[3][3]) / 100))
                print((pokemons[player[1] - 1][0] + clarification), "libero la energia contenida, pero al", (pokemons[player2[1] - 1][0] + clarification2),"estar cubierto, solo le quito", player[3][1] * int((100 - player2[3][3]) / 100) )
                
            player[7] = False
            critical = 1
        
        if player[8] == True:
            stop(0.5)
            player[8] = False
            print((pokemons[player[1] - 1][0] + clarification), "perdió su escudo")
            
        
        if player2[8] == True:
            stop(0.5)
            player2[8] = False
            print((pokemons[player2[1] - 1][0] + clarification2), "perdió su escudo")
            spc()
            
        stop(2)
            
        if player2[7] == False:           
            match player2[4]:
                case 1:
                    if random.randrange(1,101) <= luck[0]:
                        print((pokemons[player2[1] - 1][0] + clarification2), "utilizó " + str(player2[2][0]) + ", pero falló")
                        spc()     
                    elif player[8] != True:
                        if random.randrange(1, 101) >= luck[1]:
                            print("Ataque critico!")
                            critical = 2 
                        player[6] -= (player2[3][0] * critical)
                        print((pokemons[player2[1] - 1][0] + clarification2), "utilizo",player2[2][0], "quitandole", (player2[3][0] * critical), "de vida a", (pokemons[player[1] - 1][0] + clarification) )
                        spc()
                    else:
                        if random.randrange(1, 101) >= luck[1]:
                            print("Ataque critico!")
                            critical = 2 
                        player[6] -= int(player2[3][0] * ((100 - player[3][3]) / 100))
                        print((pokemons[player2[1] - 1][0] + clarification2), "utilizo",player2[2][0], "pero al estar cubierto, solo te quito", int((player2[3][0] * critical) * ((100 - player[3][3]) / 100)), "de vida a", (pokemons[player[1] - 1][0] + clarification))
                        spc()
                case 2:
                    player2[7] = True
                    print((pokemons[player2[1] - 1][0] + clarification2), "utilizo",player2[2][1], "llenandose de energia")
                    spc()
                case 3:
                    if player2[6] + player2[3][2] < player2[5]:
                        player2[6] += player2[3][2]
                        print((pokemons[player2[1] - 1][0] + clarification2), "utilizo", player2[2][2],"recuperando", player2[3][2], "de vida")
                        spc()
                    else:
                        player2[6] = player2[5]
                        print((pokemons[player2[1] - 1][0] + clarification2), "utilizo", player2[2][2],"recuperando toda la vida")
                        spc()
        else:
            
            if random.randrange(1,101) <= luck[0]:
                print((pokemons[player2[1] - 1][0] + clarification2), "liberó la energia que tenia guardada, pero falló")
                spc()
            elif player[8] != True:
                player[6] -= player2[3][1]
                print((pokemons[player2[1] - 1][0] + clarification2), "libero la energia que tenia guardada quitandole", player2[3][1], "de vida a", (pokemons[player[1] - 1][0] + clarification))
                spc()
            else:
                player[6] -= int(player2[3][1] * ((100 - player[3][3]) / 100))
                print((pokemons[player2[1] - 1][0] + clarification2), "libero la energia que tenia guardada, pero al estar cubierto, tan solo le quito", int(player2[3][1] * ((100 - player[3][3]) / 100)), "de vida a", (pokemons[player[1] - 1][0] + clarification))
                spc()
                
            player2[7] = False
            critical = 1
        
        ## Pantalla de muerte
        
        if (player[6] <= 0 and player2[6] <= 0) and player[6] == player2[6]:
            spc()
            print(f"{pokemons[player[1] - 1][0] + clarification} y {pokemons[player2[1] - 1][0] + clarification2} atacaron al mismo tiempo, por lo que es un empate!")
            stop(1)
            print("Gracias por jugar!!!!")
            break
        elif player2[6] <= 0 and player[6] > player2[6]:
            spc()
            print("Felicidades", player[0] + "! has ganado!")
            if (player[6] < 0 and player2[6] < 0) and player[6] > player2[6]:
                print(f"({pokemons[player[1] - 1][0] + clarification} hizo mas daño en el ultimo movimiento)")
            stop(1)
            print("Gracias por jugar!!!!")
            break
        elif player[6] <= 0 and player[6] < player2[6]:
            if AI == True:
                spc()
                print("Que mal", player[0] +"! has perdido...")
                if (player[6] < 0 and player2[6] < 0) and player[6] < player2[6]:
                    print(f"({pokemons[player2[1] - 1][0] + clarification2} hizo mas daño en el ultimo movimiento)")
                stop(1)
                print("Gracias por jugar!!!!")
                break
            else:
                spc()
                print("Felicidades", player2[0] + "! has ganado!")
                if (player[6] < 0 and player2[6] < 0) and player[6] < player2[6]:
                    print(f"({pokemons[player2[1] - 1][0] + clarification2} hizo mas daño en el ultimo movimiento)")
                stop(1)
                print("Gracias por jugar!!!!")
                break
        
        stop(1)
    
    spc()
    restart = input("Ingrese 1 para jugar de nuevo, ingrese 0 para salir ")
    while restart != "1" and restart != "0":
        print("Valor no valido")
        
        restart = input("Ingrese 1 para jugar de nuevo, ingrese 0 para salir ")
    
    if restart == "1":
        spc()
        clarification = ""
        clarification2 = ""
        flashmode = 1
        continue
    
    break