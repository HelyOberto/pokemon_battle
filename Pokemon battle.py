import random
import time

## Verificador de opciones universales

def notX(message, list, number):
    inp = input(message)
    inList = False
    clarificate = ""
      
    while True:
        for x in range(0, len(list)):
            if x <= len(list) - 3:
                clarificate += list[x] + ", "
            elif x == len(list) - 2:
                clarificate += list[x]
            else:
                clarificate += " o " + list[x]
                
            if list[x] == inp:
                inList = True
                break
        
        if inList == True:
            break
        
        print("Solo puedes usar " + clarificate)
        inp = input(message)
        clarificate = ""
    
    if number == True:
        inp = int(inp)
    return inp

## Pantalla de configuracion especial
def config():
    global flashmode
    global luck
    global nick
    global alternativeMessage
    global cheats
    global eggs
    global pokemons
    global timeMultiplier
    
    print("Bienvenido a pantalla de configuracion")
    stop(0.5)
    cheatsList = ["flash", "luckoff", "superluck", "hideoff"]
    eggsList = ["sika", "osly", "osmio", "ranger", "rrolo", "zelio", "kuroi", "pokegod" ]
    
    while True:
        cheatsInfo = [f"Flash: Elimina el tiempo de espera entre movimientos ({cheats[0]})", f"Luckoff : Elimina el factor suerte, haciendo que no puedas hacer ataques criticos ni fallar ({cheats[1]})", f"SuperLuck: En este modo, o fallas o das golpe critico, no hay punto medio ({cheats[2]})", f"HideOff: Elimina las lineas que ocultan la desicion del jugador 1 ({cheats[3]}) "]
        easterEggs = [ f"Sika: Muestra un mensaje dirigo a creador al principio ({eggs[0]})" , f"Osly: Un mensaje de especial del desarrollador para alguien especial ({eggs[1]})", f"Osmio: Desbloqueas la dificultad imposible si juegas contra la IA ({eggs[2]})", f"Ranger: Suelta informacion sobre Warhammer 40k ({eggs[3]})" , f"Rrolo: Activas el modo de citas ({eggs[4]})", f"Zelio: El jugador 1 gana automaticamente ({eggs[5]})", f"Kuroi: El jugador 1 pierde automaticamente ({eggs[6]})", f"Pokegod: Un pokemon especial y muy poderoso se suma a la lista de los disponibles ({eggs[7]})" ]   
        print("")
        print("Trucos de personalizacion")
        stop(0.5)
        print("")

        for x in cheatsInfo:
            print(x)
        
        stop(0.5)
            
        print("")
        print("Easter eggs")
        stop(0.5)
        print("")

        for x in easterEggs:
            print(x)
            
        print("")
        nick = input("Escriba el codigo que quiera usar, escriba 'exit' para salir (Si esta en 'True' siginifica que esta activo, para desactivarlos solo tienes que poner el codigo de nuevo) (Algunos trucos no se pueden ejecutar al mismo tiempo) (No se guardara cuando reinicies) ").lower()
        
        try:
            if cheats[cheatsList.index(nick)] == True:
                cheats[cheatsList.index(nick)] = False
                nick = ""
                
        except:
            try:
                if eggs[eggsList.index(nick)] == True:
                    eggs[eggsList.index(nick)] = False
                    nick = ""
            except:
                pass
                
        
        if nick == "exit":
            spc()
            break
        elif nick ==  "flash":
            cheats[0] = True
        elif nick == "luckoff":
            cheats[1] = True
            cheats[2] = False
        elif nick == "superluck":
            cheats[2] = True
            cheats[1] = False
        elif nick == "hideoff":
            cheats[3] = True
            
        if nick == "sika":
            eggs[0] = True
            eggs [1] = False
            eggs [3] = False
        elif nick == "osly":
            eggs[0] = False
            eggs [1] = True
            eggs [3] = False
        elif nick == "osmio":
            eggs[2] = True
        elif nick == "ranger":
            eggs[0] = False
            eggs [1] = False
            eggs [3] = True
        elif nick == "rrolo":
            eggs[4] = True
        elif nick == "zelio":
            eggs[5] = True
            eggs[6] = False
        elif nick == "kuroi":
            eggs[5] = False
            eggs[6] = True
        elif nick == "pokegod":
            eggs[7] = True
        
    if cheats[0] == True:
        timeMultiplier = 0
            
    if cheats[1] == True:
        luck[0] = 0
        luck [1] = 101
            
    if cheats[2] == True:
        luck[0] = 50
        luck[1] = 51
            
    if eggs[0] == True:
        alternativeMessage = "Bienvenido de nuevo, padre :)"
            
    if eggs[1] == True:
        alternativeMessage = "Feliz aniversario amoooor"
            
    if eggs[3] == True:
        alternativeMessage = "Warhammer 40k es una franquicia de ciencia ficcion y fantasia oscura para aldultos, o Grimmdark, como suele ser referido, creada en el año 1987 por empresa britanica Games Workshop"
     
    if eggs[7] == True:
        cyrusAtks = ["Cuernazo", "Rayo magico", "Hechizo de salud", "Barrera"]
        cyrusAtksNum = [100, 200, 100, 80]

        cyrus = ["Cyrus", cyrusAtks, cyrusAtksNum]
        pokemons.append(cyrus)
            
def romance():
    print("Estas con tu novia vaporeon en una isla paradisiaca")
    ask()
    print("El escenario es perefecto, el sol, el mar, las avez...")
    ask()
    print("Todo va bien, hasta que...")
    print("...ella se acecar a ti y te pregunta si te gusta su tipo de huevo")
    input("Tu respondes: ")
    print("'COMO?!' responde ella sorprendida y enojada")
    ask()
    print("'Pensé que eras alguien serio'")
    ask()
    print("'Eres un maldito degenerado'")
    input("Tu respondes: ")
    print("'No me importa, que esperar de un naco y estupido?'")
    ask()
    print("Ella se va lanzandote chorro de agua dejandote todo mojado")
    ask()
    print("Otra mina mas, otra mina menos")
    ask()
    print("Al menos esta no tenia sifilis")
    stop(0.5)
    print("Good ending")
    ask()
    
def rockPaperScissor():
    global player
    global player2
    
    options = ["","Piedra","Papel", "Tijeras"]
    
    pOnePoints = 0
    pTwoPoints = 0
    
    while True:
        
        print("Que quieres hacer?")
        spc()
        print("1. Partida simple: Se decide quien gana el numero con una ronda")
        print("2. 2 de 3: Se juegan hasta maximo 3 partidas, gana el primero en ganar 2 partidas")
        spc()
        configuration = notX(f"Seleccione entre '1' o '2' ", "12", False)
        spc()
        
        while True:
            pOne = notX(f"{player[0]}, ingrese 1 para elegir piedra, 2 para elegir papel, o 3 para elejir tijeras ", "123", True)
            hide()
            pTwo = notX(f"{player2[0]}, ingrese 1 para elegir piedra, 2 para elegir papel, o 3 para elejir tijeras ", "123", True)
            spc()
            
            stop(0.5)
            
            print(player[0], "uso", options[pOne], "/", player2[0], "uso", options[pTwo])
            spc()
            
            stop(0.5)
            
            if pOne == pTwo:
                print("Intenten de nuevo")
                ask()
                spc()
                continue
            
            if pOne == 1:
                pOne = 4
                
            if pOne == pTwo + 1:
                pOnePoints += 1
            else:
                pTwoPoints += 1
            
            
            if configuration == "2" and (pOnePoints < 2 and pTwoPoints < 2):   
                if pOnePoints == pTwoPoints:
                    print("Partida de desempate")
                    ask()
                    spc()
                    continue
                elif pOnePoints > pTwoPoints:
                    print(player[0], "lleva la delantera")
                    ask()
                    spc()
                    continue
                else:
                    print(player2[0], "lleva la delantera")
                    ask()
                    spc()
                    continue
                
            else:
                if pOne == pTwo + 1:
                    print(f"{player[0]} gana el punto de la partida!")
                    player[6] = 1
                    ask()
                    spc()
                    break
                else:
                    print(f"{player2[0]} gana el punto de la partida!")
                    player2[6] = 1
                    ask()
                    spc()
                    break
        
        break
    
    
    
    

## Funciones de texto
def spc():
    print("----------------------")
    
def hide():
    global cheats
    if cheats[3] == False:
        for x in range(0, 100):
            print("--------------------------------")
    
def stop(segundos):
    global timeMultiplier
    time.sleep(segundos * timeMultiplier)
    
def ask():
    input("Ingrese 'Enter' para continuar ")
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

def Xdifficulty(multiplier):
    global player2
    global player
    
    player2[5] = int(player2[5] * multiplier)
    player2[6] = player2[5]
    if player2[5] > player[5]:
        player[5] = player2[5]
    else:
        player2[5] = player[5]
        
def pokemonListCheck(player):
    global pokemons
    global pokemonInList
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
    return int(player[1])
    
    

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
        case _:
            print("No hay informacion disponible de ese pokemon")
            ask()
    
secretMessagge = False

while True:
    
    ## Dificultad
    
    difficulty = 2
    difficultiesX = ["", 0.5, 1, 1.5, 2, 3, 10]
    difficultyInfo = ["1. Facil: El enemigo empieza con la mitad de de vida que tu", "2. Normal: Los 2 empiezan con la misma vida", "3. Dificil: Tu rival empieza con %50 de vida mas", "4. Muy dificil: Tu rival empieza con el doble de vida", "5. Insano: Tu rival tiene 3 veces mas vida que tu"]
    
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
    score = 0

    player = [name, pokemon, atks, atksNum, election, maxLife, life, effect, shield, score]
    
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
    enmScore = 0
    
    player2 = [enmName, enmPokemon, enmAtks, enmAtksNum, enmElection, enmMaxLife, enmLife, enmEffect, enmShield, enmScore]
    
    posibilidad = []
    clarification2 = ""
 
    ## Extras
    
    info = ""
    restart = ""
    start = ""
    gameMode = ""
    default = ""
    
    customedLife = 400
    critical = 1
    timeMultiplier = 1
    
    luck = [10, 95]
    
    pokemonInList = False
    AI = True
    
    ## Partidas largas
    rounds = 1
    scoreLimit = 1
    
    ## cheats
    
    flashmode = False
    luckOffMode = False
    superLuckMode = False
    hideOff = False
    
    cheats = [flashmode, luckOffMode, superLuckMode, hideOff]   
     
    ## easters eggs
    
    sika = False
    osly = False
    osmio = False
    ranger = False
    rrolo = False
    zelio = False
    kuroi = False
    pokegod = False
    
    eggs = [sika, osly, osmio, ranger, rrolo, zelio, kuroi, pokegod]
    alternativeMessage = ""

    
    ## Introduccion
    while True:
        if eggs[4] == True:
            romance()
            break
        elif secretMessagge == True and random.randrange(1, 101) >= 50:
            print("Ingresa el nombre 'config' para acceder a la pantalla de trucos")
            spc()
        
        player[0] = str(input("Ingresa tu nombre: "))
        nick = player[0].lower()

        if nick == "config":
            config()
            continue
        
        break
    
    if eggs[4] == True:
        break
    
    if alternativeMessage == "":
        print("Bienvenid@", player[0], "al simulador de peleas pokemon!")
        stop(1)
        print("Hecho por: Sika")
        stop(1)
        spc()
    else:
        print(alternativeMessage)
        stop(1)
        spc()
     
    gameMode = notX("Ingrese '1' para jugar contra la maquina, ingrese '2' para el modo jugador vs jugador ", "12", False) 

        
    if gameMode == "2":
        AI = False
        spc()
        player2[0] = input("Ingrese el nombre del jugador 2: ")
        spc()
        
        while player[0] == player2[0]:
            print("No puedes usar el mismo nombre que el otro jugador")
            player2[0] = input("Ingrese el nombre del jugador 2: ")
            spc()
        stop(0.5)
    
    while True:
        try:
            scoreLimit = int(input("Ingrese la cantidad de partidas minimas que necesita un jugador para ganar (Pon '1' para una partida normal) "))
            break
        except:
            print("Solo puedes poner numeros enteros")
            stop(0.5)
            spc()  
    spc()
    
    default = notX("Ingrese '1' para jugar con la configuracion por defecto, ingrese '2' para personalizar algunas cosas ", "12", False)
    spc()
    
    if default == "2":
        while True:
            try:
                customedLife = int(input("Ingrese la cantidad de vida con la quiera iniciar, esto puede hacer variar la duracion de las partidad (Ingrese 300 o 400 para una duracion normal) "))
                break
            except:
                print("Solo puedes poner numeros enteros")
                stop(0.5)
                spc()
            
        referenceLife(customedLife)
            
        if eggs[5] == True:
            player2[6] = 0
        elif eggs[6] == True:
            player[6] = 0
            
        spc()
        
        if AI == True:
            if eggs[2] == False:
                print("Elige la dificultad")
                spc()
                
                for x in difficultyInfo:
                    print(x)
                    
                spc()
                difficulty = notX("Selecciona la dificultad por su numero ", "12345", True)
                
                Xdifficulty(difficultiesX[difficulty])
                spc()
            else:
                difficulty = 6
                print("Dificultad Osmio activada")
                stop(1)
                spc()
    
    else:
        referenceLife(customedLife)
        
        if eggs[5] == True:
            player2[6] = 0
        elif eggs[6] == True:
            player[6] = 0
        
        if eggs[2] == True:
            difficulty = 6
            print("Dificultad Osmio activada")
            stop(1)
            spc()
        
        Xdifficulty(difficultiesX[difficulty])
    
        
    while player[9] < scoreLimit and player2[9] < scoreLimit:
        if scoreLimit > 1:
            print(f"Ronda {rounds}!!")
            stop(0.5)
        
        start = "2"
        
        while start != "1":
            spc()
            pokemonInList = False
            
            for e in range(0, len(pokemons)):
                print(f"{e + 1}. {pokemons[e][0]}")

            player[1] = pokemonListCheck(player)
            spc()
            
            start = notX(f"Quieres quedarte con {pokemons[player[1] - 1][0]}? Ingrese 1 para quedartelo, 2 para volver a elegir ", "12", False)
            if start == "2":
                continue
            
            info = notX(f"Ingrese '2' saber informacion de {pokemons[player[1] - 1][0]}, ingrese '1' para omitir ", "12", False)
            
            if info == "2":
                pokemonsInfo(player[1])
                        
            player[2] = pokemons[player[1] - 1][1]
            player[3] = pokemons[player[1] - 1][2]

                        

        start = "2"
        
        if AI == False:
            while start != "1":
                spc()
                pokemonInList = False
                
                for e in range(0, len(pokemons)):
                    print(f"{e + 1}. {pokemons[e][0]}")

                player2[1] = pokemonListCheck(player2)
                spc()
                
                start = start = notX(f"Quieres quedarte con {pokemons[player2[1] - 1][0]}? Ingrese 1 para quedartelo, 2 para volver a elegir ", "12", False)
                 
                if start == "2":
                    continue
                
                info = notX(f"Ingrese '2' saber informacion de {pokemons[player2[1] - 1][0]}, ingrese '1' para omitir ", "12", False)
                
                if info == "2":
                    pokemonsInfo(player2[1])
                            
                player2[2] = pokemons[player2[1] - 1][1]
                player2[3] = pokemons[player2[1] - 1][2]

        else: 
            player2[1] = random.randrange(1,len(pokemons))

            while player[1] == player2[1]:
                player2[1] = random.randrange(1,len(pokemons))

            player2[2] = pokemons[player2[1] - 1][1]
            player2[3] = pokemons[player2[1] - 1][2]
            
        spc()
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
        spc()
        
        if player[1] == player2[1]:
            clarification = " de " + player[0]
            clarification2 = " de " + player2[0]

        while True:
            ## Pantalla de muerte

            if (player[6] <= 0 and player2[6] <= 0) and player[6] == player2[6]:
                spc()
                print(f"{pokemons[player[1] - 1][0] + clarification} y {pokemons[player2[1] - 1][0] + clarification2} atacaron con la misma fuerza al final, por lo que es un empate!")
                spc()
                if notX("Ingrese '2' para decidirlo con piedra papel o tijeras, ingrese '1' para omitir ", "12", False) == "2":
                    rockPaperScissor()
                    continue
                stop(1)
                if scoreLimit < 2:
                    print("Gracias por jugar!!!!")
                break
            elif player2[6] <= 0 and player[6] > player2[6]:
                spc()
                print("Felicidades", player[0] + "! has ganado!")
                if (player[6] < 0 and player2[6] < 0) and player[6] > player2[6]:
                    print(f"({pokemons[player[1] - 1][0] + clarification} hizo mas daño en el ultimo movimiento)")
                player[9] += 1
                stop(1)
                if scoreLimit < 2:
                    print("Gracias por jugar!!!!")
                break
            elif player[6] <= 0 and player[6] < player2[6]:
                if AI == True:
                    spc()
                    print("Que mal", player[0] +"! has perdido...")
                    if (player[6] < 0 and player2[6] < 0) and player[6] < player2[6]:
                        print(f"({pokemons[player2[1] - 1][0] + clarification2} hizo mas daño en el ultimo movimiento)")
                    player2[9] += 1
                    stop(1)
                    if scoreLimit < 2:
                        print("Gracias por jugar!!!!")
                    break
                else:
                    spc()
                    print("Felicidades", player2[0] + "! has ganado!")
                    if (player[6] < 0 and player2[6] < 0) and player[6] < player2[6]:
                        print(f"({pokemons[player2[1] - 1][0] + clarification2} hizo mas daño en el ultimo movimiento)")
                    player2[9] += 1
                    stop(1)
                    if scoreLimit < 2:
                        print("Gracias por jugar!!!!")
                    break
            
            
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
                
                
                while True:            
                    player[4] = notX("Seleccione el movimiento que quiera usar por su numero ", "1234", True)
                    spc()
                    
                    if player[4] == "3" and player[6] == player[5]:
                        print("Ya tienes la vida llena",player[0] +", intenta otro movimiento")
                        spc()
                        continue
                    break
            
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
                        
                    while True:            
                        player2[4] = notX("Seleccione el movimiento que quiera usar por su numero ", "1234", True)
                        spc()
                        
                        if player2[4] == "3" and player2[6] == player2[5]:
                            print("Ya tienes la vida llena",player2[0] +", intenta otro movimiento")
                            spc()
                            continue
                        break
                    hide()

                input("Ingrese 'Enter' para ver el resultado ")
                spc()
                
            if player[4] == 4:
                player[8] = True
                print((pokemons[player[1] - 1][0] + clarification), "se cubrio con",player[2][3])
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
                    print((pokemons[player[1] - 1][0] + clarification), "libero la energia contenida, pero al estar cubierto, solo le quito", int(player[3][1] * ((100 - player2[3][3]) / 100)), "de vida a", (pokemons[player2[1] - 1][0] + clarification2))
                    
                player[7] = False
            critical = 1
            
            stop(1)
                
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
            
            stop(0.5)
            
            if player[8] == True:
                stop(0.5)
                player[8] = False
                print((pokemons[player[1] - 1][0] + clarification), "perdió su escudo")
                spc()
                stop(0.5)
                
            
            if player2[8] == True:
                stop(0.5)
                player2[8] = False
                print((pokemons[player2[1] - 1][0] + clarification2), "perdió su escudo")
                spc()
                stop(0.5)
                
            ask()
            hide()
        
        rounds += 1
        referenceLife(customedLife)
        
        if scoreLimit > 1:
            spc()
            print("Rondas ganadas de:")
            stop(0.5)
            spc()
            print(f"{player[0]}: {player[9]}")
            stop(0.5)
            print(f"{player2[0]}: {player2[9]}")
            spc()
            ask()
    
    spc()
    
    if scoreLimit > 1:
        if player[9] > player2[9]:
            print(f"Felicidades {player[0]}!! Ganaste las rondas!!!")
            stop(1)
            print("Gracias por jugar!!!")
            ask()
    
    restart = notX("Ingrese 1 para jugar de nuevo, ingrese 2 para salir ", "12", False)
    
    if restart == "1":
        secretMessagge = True
        spc()
        continue
    
    break