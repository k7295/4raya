
import random

class Minimax(object):
   
    
    tablero = None
    ficha = ["x", "o"]

    
    def __init__(self, tablero):
        # actualizar tablero
        self.tablero = [x[:] for x in tablero]
        
            
    def mejorMov(self, profundidad, state, jugador_actual):
       
        
        # para saber cuando esta moviendo X o O
        if jugador_actual == self.ficha[0]:
            jugador_oponente = self.ficha[1]
        else:
            jugador_oponente = self.ficha[0]
        
        movimiento_posibles = {} # posibles movimientos
        for col in range(7):
            if self.isMovimientoPosible(col, state):
                # se realiza el movimiento
                temp = self.Mover(state, col, jugador_actual)
                movimiento_posibles[col] = -self.buscarAlpha(profundidad-1, temp, jugador_oponente)
        
        best_alpha = -99999999
        mejor_mov = None
        movimientos = movimiento_posibles.items()
        print(movimientos)
        random.shuffle(list(movimientos))
        for move, alpha in movimientos:
            print(alpha)
            print(move)
            if alpha >= best_alpha:
                best_alpha = alpha
                mejor_mov = move
        
        return mejor_mov, best_alpha
        
    def buscarAlpha(self, profundidad, state, jugador_actual):
        """ 
            Se busca en el arbol el valor del alpha,
        """
        movimiento_posibles = [] # posibles movimientos
        for i in range(7):
            if self.isMovimientoPosible(i, state):
                # realiza el movimiento en la columna i del jugador actual
                temp = self.Mover(state, i, jugador_actual)
                movimiento_posibles.append(temp)
        
        if profundidad == 0 or len(movimiento_posibles) == 0 or self.gameOver(state): # profundidad 0, ultimo nodo o si ya no hay mas movimiento
            # retorna la heuristica 
            return self.value(state, jugador_actual)
        
        # ficha del oponente
        if jugador_actual == self.ficha[0]:
            jugador_oponente = self.ficha[1]
        else:
            jugador_oponente = self.ficha[0]

        alpha = -99999999
        for nodoHijo in movimiento_posibles:
            if nodoHijo == None:
                print("nodoHijo == None (buscarAlpha)")
            alpha = max(alpha, -self.buscarAlpha(profundidad-1, nodoHijo, jugador_oponente))
        return alpha

    def isMovimientoPosible(self, column, state):
        """ Funcion hecha con el fin de saber si el espacio en donde se quiere colocar una ficha
            este vacia, en caso contrario significa que esta ocupada y no se puede colocar la ficha
        """
        for i in range(6):
            if state[i][column] == ' ': # espacio vacio? mueva 
                return True
        return False
    
    def gameOver(self, state):
        if self.checkRaya(state, self.ficha[0], 4) >= 1:
            return True
        elif self.checkRaya(state, self.ficha[1], 4) >= 1:
            return True
        else:
            return False
        
    
    def Mover(self, state, column, color):
        """ realiza un movimieto de estado en el tablero del jugador actual, 
            esta funcion me tira todos los posibles movimientos 
            
            Retorna el nuevo tablero con los cambios del movimiento realizado
        """
        
        temp = [x[:] for x in state]
        for i in range(6):
            if temp[i][column] == ' ': ## si el espacio esta disponible, se puede colocar una ficha
                temp[i][column] = color
                return temp

    def value(self, state, color):
        """
            Funcion que se encarga de calcular la heuristica. 
            Se van a generar 
            * valores positivos:  para indicar las buenas situaciones para el jugador actual 
            * valores negativos: para indicar las mejores situaciones para el contrincante. 

            Heuristica: (num  4-in-a-rows)*99999 + (num  3-in-a-rows)*100 + 
            (num  2-in-a-rows)*10 - (num of opponent 4-in-a-rows)*99999 - (num  opponent
            3-in-a-rows)*100 - (num  opponent 2-in-a-rows)*10
        """
        if color == self.ficha[0]:
            o_color = self.ficha[1]
        else:
            o_color = self.ficha[0]
        
        fourrow = self.checkRaya(state, color, 4)
        threerow = self.checkRaya(state, color, 3)
        tworow = self.checkRaya(state, color, 2)
        fourrow_contrincante = self.checkRaya(state, o_color, 4)
    
        if fourrow_contrincante > 0:
            return -100000
        else:
            return fourrow*100000 + threerow*100 + tworow
            
    def checkRaya(self, state, color, streak):
        count = 0
        # se recorre el tablero 
        for i in range(6):
            for j in range(7):
                if state[i][j].lower() == color.lower():
                    count += self.vertical_raya(i, j, state, streak)
                 
                    count += self.horizontal_raya(i, j, state, streak)
 
                    count += self.diagonal_raya(i, j, state, streak)

        # retorna el peso del arbol 
        return count
            
    def vertical_raya(self, row, col, state, streak):
        consecutiveCount = 0
        for i in range(row, 6):
            if state[i][col].lower() == state[row][col].lower():
                consecutiveCount += 1
            else:
                break
    
        if consecutiveCount >= streak:
            return 1
        else:
            return 0
    
    def horizontal_raya(self, row, col, state, streak):
        consecutiveCount = 0
        for j in range(col, 7):
            if state[row][j].lower() == state[row][col].lower():
                consecutiveCount += 1
            else:
                break

        if consecutiveCount >= streak:
            return 1
        else:
            return 0

    
    def diagonal_raya(self, row, col, state, streak):
        
        total = 0

        consecutiveCount = 0
        j = col

        ## diagonal positiva
        for i in range(row,6):
            if j > 6:
                break
            elif state[i][j].lower() == state[row][col].lower():
                consecutiveCount += 1
            else:
                break
            j += 1 
            
        if consecutiveCount >= streak:
            total += 1

        # diagonal neativa 
        consecutiveCount = 0
        j = col
        for i in range(row, -1, -1):
            if j > 6:
                break
            elif state[i][j].lower() == state[row][col].lower():
                consecutiveCount += 1
            else:
                break
            j += 1 

        if consecutiveCount >= streak:
            total += 1

        return total
