

from connect4 import *

def main():
    """ Play a game!
    """
    
    g = Game()
    g.imprimirTablero()
    player1 = g.jugadores[0]
    player2 = g.jugadores[1]
    
    win_counts = [0, 0, 0] # [p1 gana, p2 gana, empate]
    
    exit = False
    while not exit:
        while not g.fin:
            g.nextMove()
        
        g.imprimirTablero()
        
        if g.ganador == None:
            win_counts[2] += 1
        
        elif g.ganador == player1:
            win_counts[0] += 1
            
        elif g.ganador == player2:
            win_counts[1] += 1
        
        printResultado(player1, player2, win_counts)
        
        break
        
def printResultado(player1, player2, win_counts):
    print("{0}: {1} wins, {2}: {3} wins, {4} ties".format(player1.nombre,
        win_counts[0], player2.nombre, win_counts[1], win_counts[2]))
        
if __name__ == "__main__": # Default "main method" idiom.
    main()
