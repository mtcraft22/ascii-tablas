import os


class table:
    os.system("color")
    rojo = "\033[38;2;255;0;0m"
    verde = "\033[38;2;0;255;0m"
    azul = "\033[38;2;0;0;255m"
    azul_blanquesino = "\033[38;2;104;136;252m"
    blanquecino_azul = "\033[38;2;154;175;252m"
    verde_lima_oscuro = "\033[38;2;0;204;102m"
    verde_pantano_claro = "\033[38;2;0;204;0m"
    verde_pantano = "\033[38;2;0;102;0m"
    verde_pantano_oscuro = "\033[38;2;0;51;0m"
    naranga = "\033[38;2;255;102;0m"
    marron_oscuro = "\033[38;2;128;0;0m"
    marron_claro = "\033[38;2;153;51;0m"
    amarillo = "\033[38;2;255;255;0m"
    amarillo_mostaza = "\033[38;2;250;100;0m"
    naranga_mostaza = "\033[38;2;200;150;0m"
    fin = "\033[38;2;255;255;255m"

    def __init__(self, w, h, s, c=0):
        self.w = w
        self.h = h
        self.c = c
        self.style = s
        self.columns = 0
        self.row = False
        self.rown = 0
        self.styles = {
            "double_line": ["╔", "╗", "╚", "╝", "══", "║", "╦", "╩", "╬", "╣", "╠"],
            "simple": ["┌", "┐", "└", "┘", "──", "│", "┬", "┴", "┼", "┤", "├"],
            "default": ["+", "+", "+", "+", "--", "|", "+", "+", "+", "+", "+"],
            "special": ["╔", "╗", "╚", "╝", "▀▀", "█", "╦", "╣", "╠"],
            "special_simple": ["┌", "┐", "└", "┘", "▀▀", "█", "┬", "┴", "┼", "┤", "├"],
            "special_default": ["+", "+", "+", "+", "▀▀", "█", "+", "+", "+"],
            "merged": ["╔", "╗", "└", "┘", "══", "█", "+", "┴", "┼", "┤", "├"]
        }
        self.composition = {}

    def cretate(self):
        self.top = []
        self.top.append(self.styles[self.style][0])
        for i in range(self.w):
            self.top.append(self.styles[self.style][4])
        self.top.append(self.styles[self.style][1])
        self.composition["top"] = self.top
        for i in range(self.h):
            self.xt = []
            self.xt.append("\n")
            self.xt.append(self.styles[self.style][5])
            for ib in range(self.w):
                self.xt.append("  ")
            self.xt.append(self.styles[self.style][5])
            self.composition[i] = self.xt
        self.bottom = []
        self.bottom.append("\n")
        self.bottom.append(self.styles[self.style][2])
        for i in range(self.w):
            self.bottom.append(self.styles[self.style][4])
        self.bottom.append(self.styles[self.style][3])
        self.composition["bottom"] = self.bottom

    def add_columns(self):
        self.topa = []
        if self.style == "default" or self.style == "special_default":
            for i in self.composition["top"]:
                self.topa.append(i)
            for i in range(self.w):
                self.topa.append(self.styles[self.style][4])
            self.topa.append(self.styles[self.style][1])
            self.composition["top"] = self.topa
            for a in range(self.h):
                self.botl = []
                for i in self.composition[a]:
                    self.botl.append(i)
                for i in range(self.w):
                    self.botl.append("  ")
                self.botl.append(self.styles[self.style][5])
                self.composition[a] = self.botl
            self.bot2 = []
            for i in self.composition["bottom"]:
                self.bot2.append(i)
            for i in range(self.w):
                self.bot2.append(self.styles[self.style][4])
            self.bot2.append(self.styles[self.style][1])
            self.composition["bottom"] = self.bot2
        else:
            for i in self.composition["top"]:
                self.topa.append(i)
            post = self.topa.index(self.styles[self.style][1])
            self.topa.pop(post)
            self.topa.insert(post, self.styles[self.style][6])
            for i in range(self.w):
                ob = 1
                self.topa.insert(post + ob, self.styles[self.style][4])
                ob += 1
            self.topa.append(self.styles[self.style][1])
            self.composition["top"] = self.topa

            for a in range(self.h):
                self.botl = []
                for i in self.composition[a]:
                    self.botl.append(i)
                for i in range(self.w):
                    self.botl.append("  ")
                self.botl.append(self.styles[self.style][5])
                self.composition[a] = self.botl
            self.bot2 = []
            for i in self.composition["bottom"]:
                self.bot2.append(i)
            post = self.bot2.index(self.styles[self.style][3])
            self.bot2.pop(post)
            self.bot2.insert(post, self.styles[self.style][7])
            for i in range(self.w):
                ob = 1
                self.bot2.insert(post + ob, self.styles[self.style][4])
                ob += 1
            self.bot2.append(self.styles[self.style][3])
            self.composition["bottom"] = self.bot2
        self.columns += 1


    def add_row(self):
        if self.rown >= 1:
            self.bajo = []
            self.esquinas = []
            for i in self.composition[f"br{self.rown}"]:
                self.bajo.append(i)
            for i in range(len(self.bajo)):
                if self.bajo[i] == self.styles[self.style][7]:
                    self.esquinas.append(i)
            for i in self.esquinas:
                self.bajo.pop(i)
                self.bajo.insert(i, self.styles[self.style][8])
            self.p = self.bajo.index(self.styles[self.style][2])
            self.prin2 = self.bajo.index(self.styles[self.style][3])
            self.bajo.pop(self.p)
            self.bajo.insert(self.p, self.styles[self.style][10])
            self.bajo.pop(self.prin2)
            self.bajo.insert(self.prin2, self.styles[self.style][9])
            self.composition[f"br{self.rown}"] = self.bajo
            for i in range(self.h):
                self.rowinrow = []
                self.rowinrow.append("\n")
                for iab in range(self.columns + 1):
                    self.rowinrow.append(self.styles[self.style][5])
                    for ia in range(self.w):
                        self.rowinrow.append("  ")
                self.rowinrow.append(self.styles[self.style][5])
                self.composition[f"{self.columns}.{i}"] = self.rowinrow
            self.rowbottom = []
            self.rowbottom.append("\n")
            self.rowbottom.append(self.styles[self.style][2])
            for i in range(self.columns + 1):
                for i in range(self.w):
                    self.rowbottom.append(self.styles[self.style][4])
                self.rowbottom.append(self.styles[self.style][7])
            self.rowbottom.pop(len(self.rowbottom) - 1)
            self.rowbottom.append(self.styles[self.style][3])
            self.composition[f"br{self.rown}"] = self.rowbottom
            self.rown += 1
        else:
            self.bajo = []
            self.esquinas = []
            for i in self.composition[f"bottom"]:
                self.bajo.append(i)
            for i in range(len(self.bajo)):
                if self.bajo[i] == self.styles[self.style][7]:
                    self.esquinas.append(i)
            for i in self.esquinas:
                self.bajo.pop(i)
                self.bajo.insert(i, self.styles[self.style][8])
            self.p = self.bajo.index(self.styles[self.style][2])
            self.prin2 = self.bajo.index(self.styles[self.style][3])
            self.bajo.pop(self.p)
            self.bajo.insert(self.p, self.styles[self.style][10])
            self.bajo.pop(self.prin2)
            self.bajo.insert(self.prin2, self.styles[self.style][9])
            self.composition[f"bottom"] = self.bajo
            for i in range(self.h):
                self.rowinrow = []
                self.rowinrow.append("\n")
                for iab in range(self.columns + 1):
                    self.rowinrow.append(self.styles[self.style][5])
                    for ia in range(self.w):
                        self.rowinrow.append("  ")
                self.rowinrow.append(self.styles[self.style][5])
                self.composition[f"{self.columns}.{i}"] = self.rowinrow
            self.rowbottom = []
            self.rowbottom.append("\n")
            self.rowbottom.append(self.styles[self.style][2])
            for i in range(self.columns + 1):
                for i in range(self.w):
                    self.rowbottom.append(self.styles[self.style][4])
                self.rowbottom.append(self.styles[self.style][7])
            self.rowbottom.pop(len(self.rowbottom) - 1)
            self.rowbottom.append(self.styles[self.style][3])
            self.composition[f"br{self.rown}"] = self.rowbottom
            self.rown += 1
            print("composicion: ", self.composition)


    def show(self):
        self.tabla = []
        for i in self.composition:
            for a in self.composition[i]:
                # print(a)
                self.tabla.append(a)
        print(self.c)
        print("".join(self.tabla))
        print(self.fin)


a = input("pon stilo")


hola2 = table(5, 2, a)
hola2.c = hola2.azul_blanquesino
hola2.cretate()
hola2.add_columns()
hola2.add_columns()
hola2.add_columns()
hola2.add_columns()
hola2.add_row()
hola2.add_row()
hola2.add_row()


hola2.show()
print("composicion: ", hola2.composition)
""" hola2=table(10,5,"double_line")
hola2.cretate()
hola2.show()
hola3=table(10,5,"simple")
hola3.cretate()
hola3.show() """
