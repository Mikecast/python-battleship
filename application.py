#!/usr/bin/env python
 # -*-coding: 850 -*-
 
#esos codigos raros de arriva son para que la letra ñ y las tilden funcionen
 
 
import random #<-------------para generar numeros al azar hasta donde se yo
import os  #<----- para ejercutar comandos de la consola shell, y para otras cosas mas que desconosco
import time #<-------------para detener el programa por tiempos determinados
#-------------------------------------------------------------------------------
 
#-TABLEROs
TABLERO = [[" ", " ", " ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 "], [" ", "-------------------------------------------"], [" ", "A", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "B", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "C", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "D", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "E", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "F", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "G", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "H", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "I", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ']]
TABLERO_bot = [[" ", " ", " ", " 1 ", " 2 ", " 3 ", " 4 "," 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 "], [" ", "------------------------------------------"], [" ", "A", "|" ,' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "B", "|",' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "C", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "D", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "E", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "F", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "G", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "H", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "I", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ']]
#------------------------------------------------------------------------------------------
#-funciones basicas del juego

#Funcion #1 Impresor de TABLERO (el que lo organiza):
def print_TABLERO(esto):
  for fila in esto:
    print " ".join(fila) #la funcion join()  nos permite eliminar las " , " de las listas.
 
 
 
#print_TABLERO(TABLERO_bot)  <----TABLERO de bot
 
#-----------------------------------------------------------------------------------------------------------
 
 
#Funcion #2 generador de posicion del enemigo:
 
def fila_aleatoria(TABLERO_bot):
  return random.randint(2, len(TABLERO_bot) - 1)
 
def columna_aleatoria(TABLERO_bot):
        return random.randint(3, len(TABLERO_bot[0]) - 1)
 
#barco_fila = fila_aleatoria(TABLERO_bot)
#barco_col = columna_aleatoria(TABLERO_bot)
 
#Funcion #3 generador de coordenadas de jugador: esta funcion transforma las coordenadas que inserta el jugador "a1, a2, b3" etc a numeros para hubicarnos dentro de las listas donde estan los TABLEROs.
def coordenadas_barco(y):
    coordenada = []
    if len(y) == 2:
        y = y.lower()
        if y[0] == "a" or y[0] == "b" or y[0] == "c" or y[0] == "d" or y[0] == "e" or y[0] == "f" or y[0] == "g" or y[0] == "h" or y[0] == "i" or y[0] == "j":
            if y[1] == "1" or y[1] == "2" or y[1] == "3" or y[1] == "4" or y[1] == "5" or y[1] == "6" or y[1] == "7" or y[1] == "8" or y[1] == "9" or y[1] == "10":
                if y[0] == "a":
                    coordenada.append(2)
                    coordenada.append(int(y[1]) + 2)
                    coordenada.append("coordenada buena") #el "coordenada buena" se envia para como mensaje para decir "que las coordenadas estan bien"
 
                elif y[0] == "b":
                    coordenada.append(3)
                    coordenada.append(int(y[1]) + 2)
                    coordenada.append("coordenada buena")
                elif y[0] == "c":
                    coordenada.append(4)
                    coordenada.append(int(y[1]) + 2)
                    coordenada.append("coordenada buena")
                elif y[0] == "d":
                    coordenada.append(5)
                    coordenada.append(int(y[1]) + 2)
                    coordenada.append("coordenada buena")
                elif y[0] == "e":
                    coordenada.append(6)
                    coordenada.append(int(y[1]) + 2)
                    coordenada.append("coordenada buena")
                elif y[0] == "f":
                    coordenada.append(7)
                    coordenada.append(int(y[1]) + 2)
                    coordenada.append("coordenada buena")
                elif y[0] == "g":
                    coordenada.append(8)
                    coordenada.append(int(y[1]) + 2)
                    coordenada.append("coordenada buena")
                elif y[0] == "h":
                    coordenada.append(9)
                    coordenada.append(int(y[1]) + 2)
                    coordenada.append("coordenada buena")            
                else:
                    coordenada.append(10)
                    coordenada.append(int(y[1]) + 2)
                    coordenada.append("coordenada buena")
                return coordenada
            else:
                coordenada = [None, None, "error coordenada"] #el "error coordenada" significa que hay un error en la coordenada
                return coordenada
 
        else:
            coordenada = [None, None, "error coordenada"]
            return coordenada
    else:
        coordenada = [None, None, "error coordenada"]
        return coordenada
 
 
 
#Funcion #4 generador posicion del jugador:-------------------------------------------------------------------------------------------------------------------
 
def posicion_jugador():  #aqui insertamos la coordenada "a1,a2 etc" que se envia a la funcion de arriba para transformarla a la coordenada dentr de las listas
    while True:
        print "\n"
        print "\t\t\t\t\t\t-Ingrese la coordenada donde quiere ocultar su barco"
        coordenada_jugador = raw_input("--->: ")
        #ahi esta la funcion de arriba
        coordenada_jugador = coordenadas_barco(coordenada_jugador)
        if coordenada_jugador[2] == "coordenada buena":
            return coordenada_jugador
            break
        else:
            print" "
            print "Coordenada invalida \n"
#coordenada_jugador=posicion_jugador()
#jugador_fila_lugar=coordenada_jugador[0]
#jugador_col_lugar=coordenada_jugador[1]

#Funcion #5 generador posicion jugador2-----------------------------------------------------------------------------------------------------
#si se juega multiplayer esto hace lo mismo que la funcion de arriba pero para el player 2
def posicion_jugador2():
    while True:
        print "\n"
        print "\t\t\t\t\t\t-Ingrese la coordenada donde quiere ocultar su barco."
        coordenada_jugador2 = raw_input("--->: ")
        coordenada_jugador2 = coordenadas_barco(coordenada_jugador2)
        if coordenada_jugador2[2] == "coordenada buena":
            return coordenada_jugador2
            break
        else:
            print" "
            print "-Coordenada invalida. \n"
 
#coordenada_jugador2=posicion_jugador2()
#jugador_fila_lugar2=coordenada_jugador2[0]
#jugador_col_lugar2=coordenada_jugador2[1]

#Motor de ataque-------------------------------------------------------------------

#Funcion #6 ataque de jugador

def ataque_jugador():
    while True:
        print "\n"
        print "\t\t\t\t\t\tIngrese la coordenada del lugar a donde desea disparar sus cañones"
        coordenada_jugador = raw_input("--->: ")
        coordenada_jugador = coordenadas_barco(coordenada_jugador)
        if coordenada_jugador[2] == "coordenada buena":
            return coordenada_jugador
            break
        else:
            print " "
            print "\t\t\t\t\t\tBot_Ayuda: Error, ingrese una coordenada valida porfavor!\n"
 
#coordenada_jugador=ataque_jugador()
#jugador_fila=coordenada_jugador[0]
#jugador_col=coordenada_jugador[1]
 
 
 
#Funcion #7 -------en la función verifi se analiza que pasa con el el ataque del juugador: si da al blanco, si falla etc
def verifi(jugador_fila,jugador_col,barco_fila,barco_col, TABLERO):
    verifi = 0
    if barco_fila == jugador_fila and barco_col == jugador_col:
        TABLERO[jugador_fila][jugador_col] = " ☠ "
        os.system("reset")
        print " "
        print_TABLERO(TABLERO)
        print "\n\t\t\t\t\t\tBot_Enemigo: Felicidades hundiste mi barco ツ\n"
        print """
                        
        \t\t\t\t\t\t                ✄╭╮╭╮╱╱╭━╮╭━━╮╱╱╱╱╱╱╱╱╱╭╮
        \t\t\t\t\t\t                ✄┃╰╯┣━╮┃━┫┃╭━╋━╮╭━┳┳━╮╭╯┣━╮
        \t\t\t\t\t\t                ✄┃╭╮┃╋╰╋━┃┃╰╮┃╋╰┫┃┃┃╋╰┫╋┃╋┃
        \t\t\t\t\t\t                ✄╰╯╰┻━━┻━╯╰━━┻━━┻┻━┻━━┻━┻━╯

        """
        rrrr = raw_input("\t\t\t\t\t\tPrecione ENTER para volver al menú principal")
        verifi = 1
        return verifi #nuestra amiga: verifi se encarga de llevar en mensaje de que alguien ganó la partida para dar fin al juego
 
    elif TABLERO[jugador_fila][jugador_col] ==" 😭 ":
        print "\n\t\t\t\t\t\tBot_Enemigo: Ya dijiste esa, pierdes el turno 😜\n"
    else:
        TABLERO[jugador_fila][jugador_col] = " 😭 "
        print "\n\t\t\t\t\t\tBot_Enemigo: Fallaste 😦 \n"
 
#ganador=verifi()
 
 
 
 
#Funcion #8 funcion verifi jugador1cuando se juega para dos jugadores playerVsplayer-----------
 
def verifi1(jugador_fila,jugador_col,jugador_fila_lugar2,jugador_col_lugar2,TABLERO):
    verifi = 0
    if jugador_fila_lugar2 == jugador_fila and jugador_col_lugar2 == jugador_col:
        TABLERO[jugador_fila][jugador_col] =" ☠ "
        os.system("reset")
        print " "
        print " "
        print_TABLERO(TABLERO)
        print "\n\t\t\t\t\t\t°°°°  Felicidades, le has ganado a tu oponente!  °°°°\n"
        print "\t\t\t\t\t\t    *************************************************"
        print "\t\t\t\t\t\t    ********    Jugador 1 Gana la partida    ********"
        print "\t\t\t\t\t\t    *************************************************\n"
        print " "
        verifi = 1
        return verifi #nuestra amiga: verifi se encarga de llevar en mensaje de que alguien ganó la partida para dar fin al juego
 
    elif TABLERO[jugador_fila][jugador_col] ==" 😭 ":
        print "\n\t\t\t\t\t\t Ya dijiste esa, pierdes el turno 😜\n"
    else:
        print "\n\t\t\t\t\t\tFallaste 😦 \n"
        TABLERO[jugador_fila][jugador_col] = " 😭 "
        raw_input("\t\t\t\t\t\tPrecione ENTER para continuar")
 
#ganador=verifi1()
 
 
 
 
#Funcion #9 funcion verifi & ataque jugador 2--------
 
def ataque_jugador2():
    while True:
        print "\n"
        print "\t\t\t\t\t\t-Ingrese la coordenada del lugar a donde quiera disparar sus cañones"
        coordenada_jugador2 = raw_input("--->: ")
        coordenada_jugador2 = coordenadas_barco(coordenada_jugador2)
        if coordenada_jugador2[2] == "coordenada buena":
            return coordenada_jugador2
            break
        else:
            print " "
            print "\n\t\t\t\t\t\t--> Error, ingrese una coordenada valida porfavor!\n"
 
#coordenada_jugador2=ataque_jugador2()
#jugador_fila2=coordenada_jugador2[0]
#jugador_col2=coordenada_jugador2[1]
 
 
#Funcion #10 funcion verifi jugador2--------------------
 
 
 
def verifi2(jugador_fila2,jugador_col2,jugador_fila_lugar,jugador_col_lugar,TABLERO_bot):
    verifi = 0
    if jugador_fila2 == jugador_fila_lugar and jugador_col_lugar == jugador_col2:
        TABLERO_bot[jugador_fila2][jugador_col2] = " ☠ "
        os.system("reset")
        print " "
        print " "
        print_TABLERO(TABLERO_bot)
        print "\n\t\t\t\t\t\t°°°°  Felicidades, le has ganado a tu oponente!  °°°°\n"
        print "\t\t\t\t\t\t    *************************************************"
        print "\t\t\t\t\t\t    ********    Jugador 1 Gana la partida    ********"
        print "\t\t\t\t\t\t    *************************************************\n"
        print " "
        verifi = 1
        return verifi #nuestra amiga: verifi se encarga de llevar en mensaje de que alguien ganó la partida para dar fin al juego
 
    elif TABLERO_bot[jugador_fila2][jugador_col2] ==" 😭 ":
        print "\n\t\t\t\t\t\t ---> Ya dijiste esa, pierdes el turno 😜\n"
    else:
        print "\n\t\t\t\t\t\tFallaste 😦 \n"
        TABLERO_bot[jugador_fila2][jugador_col2] = " 😭 "
        raw_input("\t\t\t\t\t\tPrecione ENTER para continuar")
 
 
#ganador=verifi1()
 
 
 
#Funcion #11 ataque de bot-------------------------------
 
#estas funciones generan el ataque aleatorio del bot, aun sobran porque dentro de la funcion verifi_de_bot estan incluidas.
 
def fila_ataque_bot1(TABLERO_bot):
  return random.randint(2, len(TABLERO_bot) - 1)
 
def columna_ataque_de_bot1(TABLERO_bot):
        return random.randint(3, len(TABLERO_bot[0]) - 1)
 
#fila_ataque_bot=fila_ataque_bot1(TABLERO_bot)
#columna_ataque_de_bot=columna_ataque_de_bot1(TABLERO_bot)
 
#Funcion #13
def verifi_de_bot(jugador_fila_lugar,jugador_col_lugar,TABLERO_bot): #esto hace lo mismo que la funcion verifi, solo que en favor del bot.
    print " "
    print_TABLERO(TABLERO_bot)
    time.sleep(1)
 
    while True:
        fila_ataque_bot = random.randint(2, len(TABLERO_bot) - 1)#
        columna_ataque_de_bot = random.randint(3, len(TABLERO_bot[0]) - 1)
        if TABLERO_bot[fila_ataque_bot][columna_ataque_de_bot] != " 😭 ":
            break
    os.system("reset")
    print """
        \t\t\t\t\t\t####################################
        \t\t\t\t\t\t######  Turno de tu enemigo  #######
        \t\t\t\t\t\t####################################
        """

    if fila_ataque_bot == jugador_fila_lugar and columna_ataque_de_bot == jugador_col_lugar:
        TABLERO_bot[fila_ataque_bot][columna_ataque_de_bot] = " ☠ "
        os.system("reset")
        print " "
        print_TABLERO(TABLERO_bot)
        print "\nBot: Acabo de destruir a tu barco 😚.\n\n "
        print"""
        \t\t\t\t\t\t            ╭╮╱╭╮╱╱╱╱╱╱  ╱╱╱╱╱╱╱╱╱╱╭╮╱╱╭╮
        \t\t\t\t\t\t            ┃┃╱┃┃╱╱╱╱╱╱  ╱╱╱╱╱╱╱╱╱╱┃┃╱╱┃┃
        \t\t\t\t\t\t            ┃╰━╯┣━━┳━━╮  ╭━━┳━━┳━┳━╯┣┳━╯┣━━╮
        \t\t\t\t\t\t            ┃╭━╮┃╭╮┃━━┫  ┃╭╮┃┃━┫╭┫╭╮┣┫╭╮┃╭╮┃
        \t\t\t\t\t\t            ┃┃╱┃┃╭╮┣━━┃  ┃╰╯┃┃━┫┃┃╰╯┃┃╰╯┃╰╯┃
        \t\t\t\t\t\t            ╰╯╱╰┻╯╰┻━━╯  ┃╭━┻━━┻╯╰━━┻┻━━┻━━╯
        \t\t\t\t\t\t            ╱╱╱╱╱╱╱╱╱╱╱  ┃┃
        \t\t\t\t\t\t            ╱╱╱╱╱╱╱╱╱╱╱  ╰╯
        \t\t\t\t\t\t            """

        rrrr = raw_input("\n\n\t\t\t\t\t\tPrecione ENTER para volver al menú principal")
        verifi = 1
        return verifi
    else:
        TABLERO_bot[fila_ataque_bot][columna_ataque_de_bot]=" 😭 "
        palabra = ["\nBot_Enemigo: No!, he fallado! 😦 \n\n", "\nBot_Enemigo: Uff, no te di 😭 \n\n", "\nBot_Enemigo: Rayos! he fallado! \n\n", "\nBot_Enemigo: He fallado, rayos 😢\n\n", "\nBot_Enemigo: Rayos, He fallado 😢\n\n", "\nBot_Enemigo: no te di 😭\n\n"]
        botsays = random.randint(0,5)  #<--- hay algunos mensajes que se imprimen al azar cuando el bot falla el disparo
        palabra1 = palabra[botsays]
        print " "
        print_TABLERO(TABLERO_bot)
        print palabra1
        time.sleep(1)
 
 
#ganador2=verifi_de_bot(jugador_fila_lugar,jugador_col_lugar)
 
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#funciones bot vs bot
 
#posiciones bot ----
 
#en las funciones siguientes ordeno a un bot que juegue contra otro (porque no experimentar esto también) xD
#Funcion #14
def posicion_bot1():
    while True:
        print "\n"
        print "\t\t\t\t\t\t-Ingrese la coordenada donde quiere ocultar el barco del primer bot"
        coordenada_bot1 = raw_input("--->: ")
        coordenada_bot1 = coordenadas_barco(coordenada_bot1)
        if coordenada_bot1[2] == "coordenada buena":
            return coordenada_bot1
            break
        else:
            print " "
            print "\t\t\t\t\t\tCoordenada invalida \n"

 
 
#coordenada_bot1=posicion_bot1()
#bot1_fila_lugar=coordenada_bot1[0]
#bot1_col_lugar=coordenada_bot1[1]
 
 
#si nos da flojera elejir las coordenadas de los bots, pues dejemos que ellos lo hagan
 
#bot1_fila_lugar = fila_aleatoria(TABLERO)
#bot1_col_lugar = columna_aleatoria(TABLERO)
#Funcion #15
def posicion_bot2():
    while True:
        print "\n"
        print "\t\t\t\t\t\tIngrese la coordenada donde quiere ocultar el barco del segundo bot"
        coordenada_bot2 = raw_input("\t\t\t\t\t\t--->: ")
        coordenada_bot2 = coordenadas_barco(coordenada_bot2)
        if coordenada_bot2[2] == "coordenada buena":
            return coordenada_bot2
            break
        else:
            print " "
            print "\t\t\t\t\t\tCoordenada invalida \n"
 
 
#coordenada_bot2=posicion_bot2()
#bot2_fila_lugar=coordenada_bot2[0]
#bot2_col_lugar=coordenada_bot2[1]
 
 
 
#si la selecion es automatica
 
#bot2_fila_lugar = fila_aleatoria(TABLERO)
#bot2_col_lugar = columna_aleatoria(TABLERO)
 
 
#ataque bot1----------------
 
#supongo que ya saben masomenos para que sirven las funciones verifi xD
 
#Funcion #16
def verifi_de_bot1(bot2_fila_lugar,bot2_col_lugar, TABLERO_bot):
    while True:
        fila_ataque_bot1 = random.randint(2, len(TABLERO_bot) - 1)
        columna_ataque_de_bot1 = random.randint(3, len(TABLERO_bot[0]) - 1)
        if TABLERO_bot[fila_ataque_bot1][columna_ataque_de_bot1] != " 😭 ":
            break
    if fila_ataque_bot1 == bot2_fila_lugar and columna_ataque_de_bot1 == bot2_col_lugar:
        TABLERO_bot[fila_ataque_bot1][columna_ataque_de_bot1] = " ☠ "
        print_TABLERO(TABLERO_bot)
        print """
        \t\t\t\t\t\t          /////////////////////////////////////////
        \t\t\t\t\t\t          ///////      Bot_1 ha ganado      ///////
        \t\t\t\t\t\t         /////////////////////////////////////////
        """
        verifi = 1
        return verifi
    else:
        TABLERO_bot[fila_ataque_bot1][columna_ataque_de_bot1] = " 😭 "
        print_TABLERO(TABLERO_bot)
 
 
 
#ganador1=verifi_de_bot1(bot2_fila_lugar,bot2_col_lugar)
 
#ataque bot2----------------
 
 
#Funcion #17
 
def verifi_de_bot2(bot1_fila_lugar,bot1_col_lugar,TABLERO):
    while True:
        fila_ataque_bot2 = random.randint(2, len(TABLERO) - 1)
        columna_ataque_de_bot2 = random.randint(3,len(TABLERO[0])-1)
        if TABLERO[fila_ataque_bot2][columna_ataque_de_bot2] != " 😭 ":
            break
    if fila_ataque_bot2 == bot1_fila_lugar and columna_ataque_de_bot2 == bot1_col_lugar:
        TABLERO[fila_ataque_bot2][columna_ataque_de_bot2] = "☠"
        print_TABLERO(TABLERO)
        print """
        \t\t\t          /////////////////////////////////////////
        \t\t\t          ///////      Bot_2 ha ganado      ///////
        \t\t\t          /////////////////////////////////////////
        """
        verifi = 1
        return verifi
    else:
        TABLERO[fila_ataque_bot2][columna_ataque_de_bot2] = " 😭 "
        print_TABLERO(TABLERO)
 
 
 
#ganador2=verifi_de_bot2(bot1_fila_lugar,bot1_col_lugar)
 
 
 
 
 
 
 
 
#-------------------------------------------------------------------------
#Funcion jugador vs bot----------------------------------------------------
#aqui empezamos a armar los modos de juego juntando todas las funciones anteriores en 1, este es para jugar player vs bot
#Funcion #18
 
def jugadorVSbot(TABLERO,TABLERO_bot):

    print " "
    print_TABLERO(TABLERO)
    coordenada_jugador = posicion_jugador()
    jugador_fila_lugar = coordenada_jugador[0]
    jugador_col_lugar = coordenada_jugador[1]
    #coordenadas bot
    barco_fila = fila_aleatoria(TABLERO_bot)
    barco_col = columna_aleatoria(TABLERO_bot)
    while True:
        #juego
        os.system("reset")
        print """
        \t\t\t//////////////////////////////
        \t\t\t//////  Turno Jugador1  //////
        \t\t\t//////////////////////////////
        """
        print_TABLERO(TABLERO)
        coordenada_jugador = ataque_jugador()
        jugador_fila = coordenada_jugador[0]
        jugador_col = coordenada_jugador[1]
        ganador = verifi(jugador_fila, jugador_col, barco_fila, barco_col, TABLERO)
        if ganador == 1:
            verifi1 = 1
            return verifi1
            raw_input("Precione ENTER para volver al menú principal")
            print " "
            break
 
        else:
            raw_input("Precione ENTER para continuar")
        os.system("reset")
        print """
        \t\t\t####################################
        \t\t\t######  Turno de tu enemigo  #######
        \t\t\t####################################
        """
 
        ganador2 = verifi_de_bot(jugador_fila_lugar, jugador_col_lugar, TABLERO_bot)
        if ganador2 == 1:
            verifi1 = 1
            return verifi1
            raw_input("Precione ENTER para volver al menú principal")
            break
        else:
            raw_input("Precione ENTER para continuar\n")
 
 
 
 
#funcion jugador vs jugador-----------------------------------------------------------
#Funcion #19
def JugadorVsJugador(TABLERO,TABLERO_bot):
    #coordenadas jugador1
    print "\n\t\t\tEl juego comienza en: \n"
    print """
            \t\t\t╭━━━╮
            \t\t\t┃╭━╮┃
            \t\t\t╰╯╭╯┃
            \t\t\t╭╮╰╮┃
            \t\t\t┃╰━╯┃
            \t\t\t╰━━━╯
            \n"""
    time.sleep(1)
    os.system('reset')
    print"""
            \t\t\t╭━━━╮
            \t\t\t┃╭━╮┃
            \t\t\t╰╯╭╯┃
            \t\t\t╭━╯╭╯
            \t\t\t┃┃╰━╮
            \t\t\t╰━━━╯
            \n"""
    time.sleep(1)
    os.system('reset')
    print """

            \t\t\t╱╭╮
            \t\t\t╭╯┃
            \t\t\t╰╮┃
            \t\t\t╱┃┃
            \t\t\t╭╯╰╮
            \t\t\t╰━━╯
            \n"""
    time.sleep(1)
    os.system('reset')


    print """"
    \t\t\t*******************************
    \t\t\t*********  Jugador 1  *********
    \t\t\t*******************************
    """
    print_TABLERO(TABLERO)
    print " "
    coordenada_jugador = posicion_jugador()
    jugador_fila_lugar = coordenada_jugador[0]
    jugador_col_lugar = coordenada_jugador[1]
    #coordenadas jugador2
    os.system("reset")
    print """"
    \t\t\t*******************************
    \t\t\t*********  Jugador 2  *********
    \t\t\t*******************************
    """
    print_TABLERO(TABLERO_bot)
    print " "
    coordenada_jugador2 = posicion_jugador2()
    jugador_fila_lugar2 = coordenada_jugador2[0]
    jugador_col_lugar2 = coordenada_jugador2[1]
    #juego
    while True:
        os.system('reset')
        print """
        \t\t\t//////////////////////////////
        \r\t\t//////  Turno Jugador 1  /////
        \r\t\t//////////////////////////////
        """
        print_TABLERO(TABLERO)
        coordenada_jugador = ataque_jugador()
        jugador_fila = coordenada_jugador[0]
        jugador_col = coordenada_jugador[1]
        ganador = verifi1(jugador_fila, jugador_col, jugador_fila_lugar2, jugador_col_lugar2, TABLERO)
        if ganador == 1:
            raw_input("Precione ENTER para volver al menú principal")
            break
 
        os.system('reset')
        print """
        \t\t\t//////////////////////////////
        \t\t\t//////  Turno Jugador 2  /////
        \t\t\t//////////////////////////////
        """
        print_TABLERO(TABLERO_bot)
        coordenada_jugador2 = ataque_jugador2()
        jugador_fila2 = coordenada_jugador2[0]
        jugador_col2 = coordenada_jugador2[1]
        ganador2 = verifi2(jugador_fila2, jugador_col2, jugador_fila_lugar, jugador_col_lugar, TABLERO_bot)
        if ganador2 == 1:
            raw_input("Precione ENTER para volver al menú principal")
            break
 
 
#Funcion #20 funcion botVsbot
 
def botVSbot(TABLERO, TABLERO_bot):
    print "\n\t\t\t\t\t\t------------Elija un modo, Escriba 1 o 2----------\n"
    while True:
        print "\t\t\t\t\t\t 1-Manual (usted elije la ubicacion de los bots)"
        print "\t\t\t\t\t\t 2-Automatico (Los Bots elijen una ubicacion a su antojo)"
        botss=raw_input("\t\t\t\t\t\t> ")
        if botss == "1":
            os.system("reset")
 
            #bot1
            print " "
            print_TABLERO(TABLERO)
            coordenada_bot1 = posicion_bot1()
            bot1_fila_lugar = coordenada_bot1[0]
            bot1_col_lugar = coordenada_bot1[1]
            #bot2
            coordenada_bot2 = posicion_bot2()
            bot2_fila_lugar = coordenada_bot2[0]
            bot2_col_lugar = coordenada_bot2[1]
            print "\n\t\t\t\t\t\t\t\tEl juego comienza en: \n"
            time.sleep(1)
            os.system('reset')
            print """
            \n\n\n\n\n\n\n\n\n\n
            \t\t\t\t\t\t\t\t╭━━━╮
            \t\t\t\t\t\t\t\t┃╭━╮┃
            \t\t\t\t\t\t\t\t╰╯╭╯┃
            \t\t\t\t\t\t\t\t╭╮╰╮┃
            \t\t\t\t\t\t\t\t┃╰━╯┃
            \t\t\t\t\t\t\t\t╰━━━╯
            \n"""
            
            time.sleep(1)
            os.system('reset')
            print"""
            \n\n\n\n\n\n\n\n\n\n
            \t\t\t\t\t\t\t\t╭━━━╮
            \t\t\t\t\t\t\t\t┃╭━╮┃
            \t\t\t\t\t\t\t\t╰╯╭╯┃
            \t\t\t\t\t\t\t\t╭━╯╭╯
            \t\t\t\t\t\t\t\t┃┃╰━╮
            \t\t\t\t\t\t\t\t╰━━━╯
            \n"""
            time.sleep(1)
            os.system('reset')
            print """
            \n\n\n\n\n\n\n\n\n\n
            \t\t\t\t\t\t\t\t╱╭╮
            \t\t\t\t\t\t\t\t╭╯┃
            \t\t\t\t\t\t\t\t╰╮┃
            \t\t\t\t\t\t\t\t╱┃┃
            \t\t\t\t\t\t\t\t╭╯╰╮
            \t\t\t\t\t\t\t\t╰━━╯
            \n"""
            time.sleep(1)
            os.system('reset')
            break
 
 
 
 
        elif botss == "2":
            os.system("reset")
            print " "
 
            #bot1
            bot1_fila_lugar = fila_aleatoria(TABLERO)
            bot1_col_lugar = columna_aleatoria(TABLERO)
            #bot2
            bot2_fila_lugar = fila_aleatoria(TABLERO)
            bot2_col_lugar = columna_aleatoria(TABLERO)
            print "\n\t\t\t\t\t\t\t\tEl juego comienza en: \n"
 
            time.sleep(1)
            print """
            \n\n\n\n\n\n\n\n\n\n
            \t\t\t\t\t\t\t\t╭━━━╮
            \t\t\t\t\t\t\t\t┃╭━╮┃
            \t\t\t\t\t\t\t\t╰╯╭╯┃
            \t\t\t\t\t\t\t\t╭╮╰╮┃
            \t\t\t\t\t\t\t\t┃╰━╯┃
            \t\t\t\t\t\t\t\t╰━━━╯
            \n"""
            time.sleep(1)
            os.system('reset')
            print"""
            \n\n\n\n\n\n\n\n\n\n
            \t\t\t\t\t\t\t\t╭━━━╮
            \t\t\t\t\t\t\t\t┃╭━╮┃
            \t\t\t\t\t\t\t\t╰╯╭╯┃
            \t\t\t\t\t\t\t\t╭━╯╭╯
            \t\t\t\t\t\t\t\t┃┃╰━╮
            \t\t\t\t\t\t\t\t╰━━━╯
            \n"""
            time.sleep(1)
            os.system('reset')
            print """
            \n\n\n\n\n\n\n\n\n\n
            \t\t\t\t\t\t\t\t╱╭╮
            \t\t\t\t\t\t\t\t╭╯┃
            \t\t\t\t\t\t\t\t╰╮┃
            \t\t\t\t\t\t\t\t╱┃┃
            \t\t\t\t\t\t\t\t╭╯╰╮
            \t\t\t\t\t\t\t\t╰━━╯
            \n"""
            time.sleep(1)
            os.system('reset')
            break
        else:
            print "\n-->Elija una obcion valida<----\n"
 
    while True:
 
 
        print """
        \t\t\t\t\t *********************************
        \t\t\t\t\t *********  Turno Bot_1  *********
        \t\t\t\t\t *********************************
        """
        ganador1 = verifi_de_bot1(bot2_fila_lugar, bot2_col_lugar, TABLERO_bot)
        if ganador1 == 1:
            raw_input("Precione ENTER para volver al menú principal\n")
            print " \n."
 
            break
        print """
        \t\t\t\t\t *********************************
        \t\t\t\t\t *********  Turno Bot_2  *********
        \t\t\t\t\t *********************************
        """
        ganador2 = verifi_de_bot2(bot1_fila_lugar, bot1_col_lugar, TABLERO)
        if ganador2 == 1:
            raw_input("Precione ENTER para volver al menú principal\n")
            print " \n."
 
            break
 
 
#motor del juego
#y la funcion main que ejecuta todo el juego
#Funcion #21
 
 
 
 
 
 
def main():
    os.system("color 2")
    print """
    \n\n\n\n\n\n\n
    
    \t\t\t\t\t\t\t╭╮╱╭┳━━━┳╮╱╱╭━━━╮
    \t\t\t\t\t\t\t┃┃╱┃┃╭━╮┃┃╱╱┃╭━╮┃
    \t\t\t\t\t\t\t┃╰━╯┃┃╱┃┃┃╱╱┃┃╱┃┃
    \t\t\t\t\t\t\t┃╭━╮┃┃╱┃┃┃╱╭┫╰━╯┃
    \t\t\t\t\t\t\t┃┃╱┃┃╰━╯┃╰━╯┃╭━╮┃
    \t\t\t\t\t\t\t╰╯╱╰┻━━━┻━━━┻╯╱╰╯
    \n\n\t\t       A contunación te sumergiras a una batalla epíca, donde tus enemigos querran destruirte,\n\t\t\t\thaz todo lo posible para que no te destruyan destruyelos tu a ellos.
    \n\t\t\t\t\t\t\tSUERTE.\n"""
    raw_input("\t\t\t\t\t       Presione enter para continuar...")
    os.system('reset')
    print """
    \n\n\n\n\n\n\n
    \t\t\t\t\t                ╭━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
    \t\t\t\t\t                ┃╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
    \t\t\t\t\t                ┃╰╯╰┳┳━━┳━╮╭╮╭┳━━┳━╮╭┳━╯┣━━╮
    \t\t\t\t\t                ┃╭━╮┣┫┃━┫╭╮┫╰╯┃┃━┫╭╮╋┫╭╮┃╭╮┃
    \t\t\t\t\t                ┃╰━╯┃┃┃━┫┃┃┣╮╭┫┃━┫┃┃┃┃╰╯┃╰╯┃
    \t\t\t\t\t                ╰━━━┻┻━━┻╯╰╯╰╯╰━━┻╯╰┻┻━━┻━━╯
    \t\t\t\t\t                            ╭━━╮
    \t\t\t\t\t                            ┃╭╮┃
    \t\t\t\t\t                            ┃╭╮┃
    \t\t\t\t\t                            ╰╯╰╯
    \t\t\t\t\t            ╭━━╮╱╱╱╭╮╱╱╱╭╮╭╮╱╱╱╱╭━╮╱╭╮╱╱╱╱╱╱╱╱╭╮
    \t\t\t\t\t            ┃╭╮┃╱╱╭╯╰╮╱╱┃┃┃┃╱╱╱╱┃┃╰╮┃┃╱╱╱╱╱╱╱╱┃┃
    \t\t\t\t\t            ┃╰╯╰┳━┻╮╭╋━━┫┃┃┃╭━━╮┃╭╮╰╯┣━━┳╮╭┳━━┫┃
    \t\t\t\t\t            ┃╭━╮┃╭╮┃┃┃╭╮┃┃┃┃┃╭╮┃┃┃╰╮┃┃╭╮┃╰╯┃╭╮┃┃
    \t\t\t\t\t            ┃╰━╯┃╭╮┃╰┫╭╮┃╰┫╰┫╭╮┃┃┃╱┃┃┃╭╮┣╮╭┫╭╮┃╰╮
    \t\t\t\t\t            ╰━━━┻╯╰┻━┻╯╰┻━┻━┻╯╰╯╰╯╱╰━┻╯╰╯╰╯╰╯╰┻━╯
    """

    time.sleep(2)
    os.system('reset')
    while True:
        TABLERO = [[" ", " ", " ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 "], [" ", "-------------------------------------------"], [" ", "A", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "B", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "C", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "D", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "E", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "F", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "G", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "H", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "I", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ']]
        TABLERO_bot = [[" ", " ", " ", " 1 ", " 2 ", " 3 ", " 4 "," 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 "], [" ", "------------------------------------------"], [" ", "A", "|" ,' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "B", "|",' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "C", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "D", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "E", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "F", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "G", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "H", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ '], [" ", "I", "|", ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ', ' ☺ ']]
        print """
        \n\n\n
        \t\t\t\t\t    ╭━━╮╱╱╱╱╱╭╮
        \t\t\t\t\t    ╰┫┣╯╱╱╱╱╭╯╰╮
        \t\t\t\t\t    ╱┃┃╭━╮╭━┻╮╭╋━┳╮╭┳━━┳━━┳┳━━┳━╮╭━━┳━━╮
        \t\t\t\t\t    ╱┃┃┃╭╮┫━━┫┃┃╭┫┃┃┃╭━┫╭━╋┫╭╮┃╭╮┫┃━┫━━┫
        \t\t\t\t\t    ╭┫┣┫┃┃┣━━┃╰┫┃┃╰╯┃╰━┫╰━┫┃╰╯┃┃┃┃┃━╋━━┃
        \t\t\t\t\t    ╰━━┻╯╰┻━━┻━┻╯╰━━┻━━┻━━┻┻━━┻╯╰┻━━┻━━╯
        \n"""
        nombre = raw_input("\t\t\t\t\t\t\t Ingresa tu nombre:\n\t\t\t\t\t\t\t\t")
        os.system('reset')
        print """
        \t\t\t\t\t                    ╭━╮╭━╮
        \t\t\t\t\t                    ┃┃╰╯┃┃
        \t\t\t\t\t                    ┃╭╮╭╮┣━━┳━╮╭╮╭╮
        \t\t\t\t\t                    ┃┃┃┃┃┃┃━┫╭╮┫┃┃┃
        \t\t\t\t\t                    ┃┃┃┃┃┃┃━┫┃┃┃╰╯┃
        \t\t\t\t\t                    ╰╯╰╯╰┻━━┻╯╰┻━━╯
        \t\t\t\t\t                ╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
        \t\t\t\t\t                ┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
        \t\t\t\t\t                ┃╰━╯┣━┳┳━╮╭━━┳┳━━┳━━┫┃
        \t\t\t\t\t                ┃╭━━┫╭╋┫╭╮┫╭━╋┫╭╮┃╭╮┃┃
        \t\t\t\t\t                ┃┃╱╱┃┃┃┃┃┃┃╰━┫┃╰╯┃╭╮┃╰╮
        \t\t\t\t\t                ╰╯╱╱╰╯╰┻╯╰┻━━┻┫╭━┻╯╰┻━╯
        \t\t\t\t\t                ╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
        \t\t\t\t\t                ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
        \t\t\t\t\t                \n"""

        print "\t\t\t\t\t\t\t\t  Bienvenido " + str(nombre)
        print "\n\t\t\t\t\tSeleciona el modo de juego (Escriba 1,2,3... segun lo que se le antoje)"
        print " "
        print " "
        print "\t\t\t\t\t\t\t\t 1-Single player."
        print "\t\t\t\t\t\t\t\t 2-Multiplayer."
        print "\t\t\t\t\t\t\t\t 3-Bot Vs Bot. \n"
        selecciion1 = raw_input("\t\t\t\t\t\t\t\t> ")
        if selecciion1 == "1":
            os.system("reset")
            jugadorVSbot(TABLERO, TABLERO_bot)

        elif selecciion1 == "2":
            os.system("reset")
            JugadorVsJugador(TABLERO, TABLERO_bot)
        elif selecciion1 == "3":
            os.system("reset")
            botVSbot(TABLERO, TABLERO_bot)

        else:
            print "\n \t\t\t\t\t\t\t---->>Ingrese una obcion valida<<---\n"
            print "\n \t\t\t\t\t\t\tSolo puedes elegir un número del 1 al 3.\n"
            time.sleep(1.5)
        os.system("reset")
main()
