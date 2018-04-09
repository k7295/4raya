
import random
import os
import jugadorHumano 
import jugadorIA


class Game(object):

    
    tablero = None
    round = None
    fin = None
    ganador = None
    turno = None
    jugadores = [None, None]
    juego = u"Raya de 4" 
    ficha = ["x", "o"]
    

    def __init__(self):
        self.round = 1
        self.fin = False
        self.ganador = None

        os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
        print(u"Bienvenido a {0}!".format(self.juego))
      
        nombre = str(input("Nombre del jugador #1? "))
        self.jugadores[0] = jugadorHumano.JugadorHumano(nombre, self.ficha[0])
        print("{0} sera {1}".format(self.jugadores[0].nombre, self.ficha[0]))
        
        print(" El jugador#2 sera la computadora ")
        nombre = str(input("Nombre del jugador #2: "))
              
        diff = int(input(" Dificultad de la computadora(1 - 4) "))
        self.jugadores[1] = jugadorIA.JugadorIA(nombre, self.ficha[1], diff+1)
        print("{0} sera {1}".format(self.jugadores[1].nombre, self.ficha[1]))
        

        self.turno = self.jugadores[0]
        
        self.tablero = []
        for i in range(6):
            self.tablero.append([])
            for j in range(7):
                self.tablero[i].append(' ')
        
    def iniciarJuego(self):
        """ Reset del tablero
        """
        self.round = 1
        self.fin = False
        self.ganador = None
        
        # siempre se inicia con x 
        self.turno = self.jugadores[0]
        
        self.tablero = []
        for i in range(6):
            self.tablero.append([])
            for j in range(7):
                self.tablero[i].append(' ')

    def cambioTurno(self):
        """Funcion para elcambio de turno 
        """

        if self.turno == self.jugadores[0]:
            self.turno = self.jugadores[1]
        else:
            self.turno = self.jugadores[0]

        # conteo de los rounds
        self.round += 1

    def nextMove(self):
        jugador = self.turno

        # 42 campos
        if self.round > 42:
            self.fin = True
            return
        
        # mueve la ficha segun la columna que da el jugador
        move = jugador.move(self.tablero)

        for i in range(6):
            if self.tablero[i][move] == ' ':
                self.tablero[i][move] = jugador.color
                self.cambioTurno()
                self.check4linea()
                self.imprimirTablero()
                return

        print("movimiento invalido (columna llena)")
        return
    
    def check4linea(self):
        """  Encuentra la linea de 4, buscando por las diferentes direcciones
        """
        for i in range(6):
            for j in range(7):
                if self.tablero[i][j] != ' ':
                    # linea vertical
                    if self.lineaVertical(i, j):
                        self.fin = True
                        return
                    
                    # linea horizontal
                    if self.horizontallinea(i, j):
                        self.fin = True
                        return
                    
                    # diagonales
                    diag_fours, slope = self.diagonalllinea(i, j)
                    if diag_fours: # si se encuentra 4 en raya 
                        print(slope)
                        self.fin = True
                        return
        
    def lineaVertical(self, row, col):
       
        fourInARow = False
        consecutiveCount = 0
    
        for i in range(row, 6):
            if self.tablero[i][col].lower() == self.tablero[row][col].lower():
                consecutiveCount += 1
            else:
                break
    
        if consecutiveCount >= 4:
            fourInARow = True
            if self.jugadores[0].color.lower() == self.tablero[row][col].lower():
                self.ganador = self.jugadores[0]
            else:
                self.ganador = self.jugadores[1]
    
        return fourInARow
    
    def horizontallinea(self, row, col):
        fourInARow = False
        consecutiveCount = 0
        
        for j in range(col, 7):
            if self.tablero[row][j].lower() == self.tablero[row][col].lower():
                consecutiveCount += 1
            else:
                break

        if consecutiveCount >= 4:
            fourInARow = True
            if self.jugadores[0].color.lower() == self.tablero[row][col].lower():
                self.ganador = self.jugadores[0]
            else:
                self.ganador = self.jugadores[1]

        return fourInARow
    
    def diagonalllinea(self, row, col):
        fourInARow = False
        count = 0
        slope = None

         ## diagonal positiva
        consecutiveCount = 0
        j = col
        for i in range(row, 6):
            if j > 6:
                break
            elif self.tablero[i][j].lower() == self.tablero[row][col].lower():
                consecutiveCount += 1
            else:
                break
            j += 1 
            
        if consecutiveCount >= 4:
            count += 1
            slope = 'positive'
            if self.jugadores[0].color.lower() == self.tablero[row][col].lower():
                self.ganador = self.jugadores[0]
            else:
                self.ganador = self.jugadores[1]

          ## diagonal negativo
        consecutiveCount = 0
        j = col
        for i in range(row, -1, -1):
            if j > 6:
                break
            elif self.tablero[i][j].lower() == self.tablero[row][col].lower():
                consecutiveCount += 1
            else:
                break
            j += 1 

        if consecutiveCount >= 4:
            count += 1
            slope = 'negative'
            if self.jugadores[0].color.lower() == self.tablero[row][col].lower():
                self.ganador = self.jugadores[0]
            else:
                self.ganador = self.jugadores[1]

        if count > 0:
            fourInARow = True
        if count == 2:
            slope = 'both'
        return fourInARow, slope
     
    def imprimirTablero(self):
        """Funcion encargada de imprimir el tablero
        """

        os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] ) # limpiar pantalla
        print(u"{0}!".format(self.juego))
        print("Round: " + str(self.round))

        for i in range(5, -1, -1):
            print("\t", end="")
            for j in range(7):
                print("| " + str(self.tablero[i][j]), end=" ")
            print("|")
        print("\t  _   _   _   _   _   _   _ ")
        print("\t  1   2   3   4   5   6   7 ")

        if self.fin:
            print("Game Over!")
            if self.ganador != None:
                print(str(self.ganador.nombre) + " es el ganador")
            else:
                print("Empate")


