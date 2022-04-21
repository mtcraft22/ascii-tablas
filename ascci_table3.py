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
        self.__composicion = {}

    def __creación_basica(self):
        self.top = []
        self.top.append(self.estilos[self.estilo][0])
        for i in range(self.ancho):
            self.top.append(self.estilos[self.estilo][4])
        self.top.append(self.estilos[self.estilo][1])
        self.__composicion["top"] = self.top
        for i in range(self.alto):
            self.xt = []
            self.xt.append("\n")
            self.xt.append(self.estilos[self.estilo][5])
            for ib in range(self.ancho):
                self.xt.append("  ")
            self.xt.append(self.estilos[self.estilo][5])
            self.__composicion[i] = self.xt
        self.bottom = []
        self.bottom.append("\n")
        self.bottom.append(self.estilos[self.estilo][2])
        for i in range(self.ancho):
            self.bottom.append(self.estilos[self.estilo][4])
        self.bottom.append(self.estilos[self.estilo][3])
        self.__composicion["bottom"] = self.bottom
    def mostrar(self):
        self.__creación_basica()
        self.tabla = []
        for i in self.__composicion:
            for a in self.__composicion[i]:
                self.tabla.append(a)
        print("".join(self.tabla))


algo = tabla(ancho=0, alto=10, estilo="doble_linea")

algo.mostrar()



