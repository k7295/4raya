import jugadorMovAbstract
class JugadorHumano(jugadorMovAbstract.JugadorMov):
    """ Clase cuando juega un humano
    """
    
    tipo = None 
    nombre = None
    color = None
    
    def __init__(self, nombre, color):
        super().move(self)
        self.tipo = "Human"
        self.nombre = nombre
        self.color = color
    
    def move(self, state):
        super().move(self)
        print("turno de {0}. {0} es {1}".format(self.nombre, self.color))
        col = None
        while col == None:
            try:
                choice = int(input("Ingrese numero de la columna colocara la ficha: ")) - 1
            except ValueError:
                choice = None
            
            if choice == None:
                print("Opcion invalida,debe ser un numero entre 1 y 7")
            else:
                if 0 <= choice <= 6:
                    col = choice
                else:
                    print("Opcion invalida, debe ser un numero entre 1 y 7")
        return col