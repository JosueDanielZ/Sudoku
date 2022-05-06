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
interruptor = 0
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
                return False
        

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
                print("invalido",self.listaexclusiva)
                self.listaexclusiva.clear()
                return False

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
                        return False
                        
                        

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
        self.tablero[7][3] = numero
        numero = self.numerosrandom()
        self.tablero[0][6] = numero
        numero = self.numerosrandom()
        self.tablero[5][8] = numero
        numero = self.numerosrandom()
        self.tablero[6][7] = numero

    def mensajefinal(self):
        for filas in self.tablero:
            for elemento in filas:
                if elemento == 0:
                    return True
        return False

        

s_cuerpo = Cuerpo()
s_cuerpo.creartablero()
s_cuerpo.posiciondenumeros()
s_cuerpo.imprimirtablero()
print("\nverificar filas\n")

val1 = s_cuerpo.pruebadeverificacion()
if val1 == False:
    interruptor=1

print("\nverificar columnas\n")

val2 = s_cuerpo.validarcolumnas()
if val2 == False:
    interruptor=1

print("\nverificar segmentos\n")

val3 = s_cuerpo.validartodossegmentos()
if val3 == False:
    interruptor=1

val = s_cuerpo.mensajefinal()
if val == True:
    print("Le faltan numeros")
elif interruptor == 1:
    print("SOLUCION NO VALIDA")
else:
    print("GANASTE")

print(interruptor)

