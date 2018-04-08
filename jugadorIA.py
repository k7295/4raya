import jugadorMovAbstract
from minimax import Minimax 
class JugadorIA(jugadorMovAbstract.JugadorMov):
    """ Jugador con IA donde la dificultad representa la profundidad hasta a la que se va a buscar, 
    en este caso llegara hasta 4
    """
    
    dificultad = None
    def __init__(self, nombre, color, dificultad=5):
        self.tipo = "AI"
        self.nombre = nombre
        self.color = color
        self.dificultad = dificultad
        
    def move(self, state):
        super().move(self)
        print("{0}'s turno.  {0} es {1}".format(self.nombre, self.color))
        
        m = Minimax(state)
        mejor_mov, valor = m.mejorMov(self.dificultad, state, self.color)
       
        return mejor_mov
