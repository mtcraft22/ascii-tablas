import os

class tabla:
    def __init__(self, **kargs):
        self.ancho = kargs["ancho"]
        self.alto = kargs["alto"]
        self.estilo = kargs["estilo"]
        self.estilos = {
            "doble_linea": ["╔", "╗", "╚", "╝", "══", "║", "╦", "╩", "╬", "╣", "╠"],
            "simple": ["┌", "┐", "└", "┘", "──", "│", "┬", "┴", "┼", "┤", "├"],
            "por_defecto": ["+", "+", "+", "+", "--", "|", "+", "+", "+", "+", "+"],
            "especial": ["╔", "╗", "╚", "╝", "▀▀", "█", "╦", "╣", "╠"],
            "especial_simple": ["┌", "┐", "└", "┘", "▀▀", "█", "┬", "┴", "┼", "┤", "├"],
            "especial_por_defecto": ["+", "+", "+", "+", "▀▀", "█", "+", "+", "+"],
            "mix": ["╔", "╗", "└", "┘", "══", "█", "+", "┴", "┼", "┤", "├"]
        }
        self.__composición = {}
    def creación_base(self):
        pass




