

from cuatroenraya import *

def main():
    """ Play a game!
    """
    
    g = Game()
    g.imprimirTablero()
    player1 = g.jugadores[0]
    player2 = g.jugadores[1]
    
    partidasGanadas = [0, 0, 0] # [p1 gana, p2 gana, empate]
    
    exit = False
    while not exit:
        while not g.fin:
            g.nextMove()
        
        g.imprimirTablero()
        
        if g.ganador == None:
            partidasGanadas[2] += 1
        
        elif g.ganador == player1:
            partidasGanadas[0] += 1
            
        elif g.ganador == player2:
            partidasGanadas[1] += 1
        
        printResultado(player1, player2, partidasGanadas)
        
        break
        
def printResultado(player1, player2, partidasGanadas):
    print("{0}: {1} partidas ganadas, {2}: {3} partidas ganadas, {4} empates".format(player1.nombre,
        partidasGanadas[0], player2.nombre, partidasGanadas[1], partidasGanadas[2]))
        
if __name__ == "__main__": # Default "main method" idiom.
    main()
