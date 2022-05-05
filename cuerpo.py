"""
Crear un sudoku 9x9 con las siguientes reglas

1. Crear tablero de 9x9 (hecho)
2. validar filas (hecho)
3. validar columnas (hecho)
4. validar segmentos de 3x3 (hecho)
5. añadir mapa con numeros aleatorios (hecho)
5.1 Mostrar texto de ganar o de perder
6. integrar modo grafico

"""
import random
class Cuerpo():
    def __init__(self):
        self.tablero = []
        self.listaexclusiva = []


    def creartablero(self):
        self.tablero = [[0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
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

    def validartodossegmentos(self):
        self.validarsegmentos3x3(0,3)
        self.validarsegmentos3x3(3,6)
        self.validarsegmentos3x3(6,9)



    def validarsegmentos3x3(self,x,y):
        self.listaexclusiva.clear()
        for columnas in range(0,9):
            if columnas == 3 or columnas==6:
                self.listaexclusiva.clear()
            for filas in range(x,y):
                self.listaexclusiva.append(self.tablero[filas][columnas])
                if len(self.listaexclusiva)== 9:
                    validar3 = self.validarfilas(self.listaexclusiva)
                    if validar3 == True:
                        print("valido ", self.listaexclusiva)
                    else: 
                        print("invalido ",self.listaexclusiva)

    def numerosrandom(self):
        return random.randrange(1,10)

    def posiciondenumeros(self):
        numero = self.numerosrandom()
        self.tablero[1][1] = numero
        numero = self.numerosrandom()
        self.tablero[4][2] = numero
        numero = self.numerosrandom()
        self.tablero[8][0] = numero
        numero = self.numerosrandom()
        self.tablero[2][4] = numero
        numero = self.numerosrandom()
        self.tablero[3][5] = numero
        numero = self.numerosrandom()
        self.tablero[7][4] = numero
        numero = self.numerosrandom()
        self.tablero[0][6] = numero
        numero = self.numerosrandom()
        self.tablero[5][8] = numero
        numero = self.numerosrandom()
        self.tablero[6][7] = numero
        

        

s_cuerpo = Cuerpo()
s_cuerpo.creartablero()
s_cuerpo.posiciondenumeros()
s_cuerpo.imprimirtablero()
print("\nverificar filas\n")
s_cuerpo.pruebadeverificacion()
print("\nverificar columnas\n")
s_cuerpo.validarcolumnas()
print("\nverificar segmentos\n")
s_cuerpo.validartodossegmentos()