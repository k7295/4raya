
import random

class Minimax(object):
    """ Minimax object that takes a current connect four board state
    """
    
    board = None
    colors = ["x", "o"]

    
    def __init__(self, board):
        # actualizar tablero
        self.board = [x[:] for x in board]
        
            
    def bestMove(self, depth, state, curr_player):
        """ Returns the best move (as a column number) and the associated alpha
            Calls search()
        """
        
        # para saber cuando esta moviendo X o O
        if curr_player == self.colors[0]:
            opp_player = self.colors[1]
        else:
            opp_player = self.colors[0]
        
        legal_moves = {} # posibles movimientos
        for col in range(7):
            if self.isLegalMove(col, state):
                # se realiza el movimiento
                temp = self.makeMove(state, col, curr_player)
                legal_moves[col] = -self.search(depth-1, temp, opp_player)
        
        best_alpha = -99999999
        best_move = None
        moves = legal_moves.items()
        print(moves)
        random.shuffle(list(moves))
        for move, alpha in moves:
            print(alpha)
            print(move)
            if alpha >= best_alpha:
                best_alpha = alpha
                best_move = move

                print(best_alpha)
                print(best_move)
        
        return best_move, best_alpha
        
    def search(self, depth, state, curr_player):
        """ 
            Se busca en el arbol el valor del alpha,
        """
        legal_moves = [] # posibles movimientos
        for i in range(7):
            if self.isLegalMove(i, state):
                # realiza el movimiento en la columna i del jugador actual
                temp = self.makeMove(state, i, curr_player)
                legal_moves.append(temp)
        
        if depth == 0 or len(legal_moves) == 0 or self.gameIsOver(state): # profundidad 0, ultimo nodo o si ya no hay mas movimiento
            # retorna la heuristica 
            return self.value(state, curr_player)
        
        # ficha del oponente
        if curr_player == self.colors[0]:
            opp_player = self.colors[1]
        else:
            opp_player = self.colors[0]

        alpha = -99999999
        for child in legal_moves:
            if child == None:
                print("child == None (search)")
            alpha = max(alpha, -self.search(depth-1, child, opp_player))
        return alpha

    def isLegalMove(self, column, state):
        """ Funcion hecha con el fin de saber si el espacio en donde se quiere colocar una ficha
            este vacia, en caso contrario significa que esta ocupada y no se puede colocar la ficha
        """
        
        for i in range(6):
            if state[i][column] == ' ':
                # once we find the first empty, we know it's a legal move
                return True
        
        # if we get here, the column is full
        return False
    
    def gameIsOver(self, state):
        if self.checkForStreak(state, self.colors[0], 4) >= 1:
            return True
        elif self.checkForStreak(state, self.colors[1], 4) >= 1:
            return True
        else:
            return False
        
    
    def makeMove(self, state, column, color):
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
        if color == self.colors[0]:
            o_color = self.colors[1]
        else:
            o_color = self.colors[0]
        
        my_fours = self.checkForStreak(state, color, 4)
        my_threes = self.checkForStreak(state, color, 3)
        my_twos = self.checkForStreak(state, color, 2)
        opp_fours = self.checkForStreak(state, o_color, 4)
    
        if opp_fours > 0:
            return -100000
        else:
            return my_fours*100000 + my_threes*100 + my_twos
            
    def checkForStreak(self, state, color, streak):
        count = 0
        # se recorre el tablero 
        for i in range(6):
            for j in range(7):
                if state[i][j].lower() == color.lower():
                    count += self.verticalStreak(i, j, state, streak)
                 
                    count += self.horizontalStreak(i, j, state, streak)
 
                    count += self.diagonalCheck(i, j, state, streak)

        # retorna el peso del arbol 
        return count
            
    def verticalStreak(self, row, col, state, streak):
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
    
    def horizontalStreak(self, row, col, state, streak):
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

    
    def diagonalCheck(self, row, col, state, streak):
        
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
