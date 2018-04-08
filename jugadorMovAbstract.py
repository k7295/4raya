from abc import ABC, abstractmethod
class JugadorMov(object):
    """ Clase cuando jugador
    """
    @abstractmethod
    def move(self, state):
        pass