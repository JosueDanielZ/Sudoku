"""
Crear un sudoku 9x9 con las siguientes reglas

1. Crear tablero de 9x9 (hecho)
2. validar filas (hecho)
3. validar columnas (hecho)
4. validar segmentos de 3x3
5. añadir mapa con numeros aleatorios
6. integrar modo grafico

"""
class Cuerpo():
    def __init__(self):
        self.tablero = []
        self.listaexclusiva = []


    def creartablero(self):
        self.tablero = [[4,1,0,0,0,0,0,0,0],
                        [4,0,0,2,0,0,0,0,0],
                        [2,7,0,0,0,3,3,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [5,0,0,8,0,0,0,0,0],
                        [0,8,0,0,0,0,0,1,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],]

    def imprimirtablero(self):
        for filas in self.tablero:
            print(filas)

    def pruebadeverificacion(self):
        for filas in self.tablero:
            validar = self.validarfilas(filas)
            if validar == True:
                print("Valido ",filas)
            else:
                print("invalido ", filas)
        

    def validarfilas(self,unicafila):
        for elemento in unicafila:
            if elemento != 0:
                if unicafila.count(elemento) > 1:
                    return False
        return True

    def validarcolumnas(self):
        for columnas in range(0,9):
            for filas in range(0,9):
                self.listaexclusiva.append(self.tablero[filas][columnas])
                validar2 = self.validarfilas(self.listaexclusiva)
                
            if validar2 == True:
                print("valido",self.listaexclusiva)
                self.listaexclusiva.clear()
            else:
                print("ivalido",self.listaexclusiva)
                self.listaexclusiva.clear()

s_cuerpo = Cuerpo()
s_cuerpo.creartablero()
s_cuerpo.imprimirtablero()
s_cuerpo.pruebadeverificacion()
s_cuerpo.validarcolumnas()

