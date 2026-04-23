# TABLERO DEL JUEGO DAMAS 8X8
# Integrantes:
# Victor Calbucura
# Denisse Maldonado
# Matias Salgado
# Angel Vargas
from busqueda import busqueda

class tablero:

    # Visualmente en el codigo se utilizará estas letras para cada pieza, y cada una se representará con un símbolo diferente al imprimirse en el tablero
    # Pieza peón blanco "B": ○
    # Pieza peón negro "N": ●
    # Pieza dama blanco "b": (○)
    # Pieza dama negro: "n": (●)

    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1 
        self.jugador2 = jugador2
        self.hay_ganador = False
        self.matriz = self.iniciar_matriz()

    def iniciar_matriz(self): #Inicia la matriz de damas
        m = [[' '] * 8 for _ in range(8)] #Matriz 8x8
        for f in range(3): # Fila de 0 a 2
            for c in range(8): # Para todas las columnas
                if (f + c) % 2 == 1: # Esta es una forma de calcular las casillas impares (en este caso las casillas negras) de un tablero de ajedrez
                    m[f][c] = 'B'   # Las fichas blancas van abajo
        for f in range(5, 8): # Fila de 5 a 7
            for c in range(8):
                if (f + c) % 2 == 1:
                    m[f][c] = 'N'   # Y las negras van arriba

        return m # Aqui está la matriz

    def imprimir_tablero(self): # Vamos a imprimir la matriz
        print("\n    0   1   2   3   4   5   6   7") # Estas son las columnas
        print("  +" + "---+" * 8) # La linea superior del tablero que está bien formado para las 8 columnas
        for f in range(7, -1, -1):
            fila = str(f) + " |" # Linea de fila
            for c in range(8): 
                celda = self.matriz[f][c]
                if celda == 'B': # Como se dijo antes, esto es peón blanco
                    sym = ' ○ '
                elif celda == 'b': # dama blanco
                    sym = '(○)'   
                elif celda == 'N': # peón negro
                    sym = ' ● '
                elif celda == 'n':
                    sym = '(●)'   # y dama negro
                else:
                    sym = '   '
                fila += sym + '|'
            print(fila)
            print("  +" + "---+" * 8) # Y linea inferior
        print()

    def contar_piezas(self): # Función para contar las piezas de ambos jugadores
        b = n = 0
        for f in range(8):
            for c in range(8):
                p = self.matriz[f][c]
                if p in ('B', 'b'):
                    b += 1
                elif p in ('N', 'n'):
                    n += 1
        return b, n

    def encuentra_ganador(self, ficha): # Y esta función es para determinar si hay un ganador por fichas (si uno no tiene fichas, el otro gana, aunque no es la unica forma de ganar)
        b, n = self.contar_piezas()
        if ficha in ('B', 'b'):
            return n == 0
        if ficha in ('N', 'n'):
            return b == 0
        return False

    def obtener_movimientos(self, simbolo): # Aqui se utiliza la clase busqueda para obtener los movimientos posibles de un jugador a traves de su simbolo de ficha
        b = busqueda(self.matriz, simbolo, 'N' if simbolo == 'B' else 'B')
        return b.obtener_movimientos(self.matriz, simbolo)

    def hay_movimientos(self, simbolo): # Si hay movimientos se retornan cuantos movimientos posibles hay, de lo contrario, retorna 0
        return len(self.obtener_movimientos(simbolo)) > 0

    def inicia_partida(self): # Con lo anterior mostrado, se inicia la partida
        # Breve introducción
        print("Bienvenido a damas\n")
        print(" Jugador 1 (Blancas): " + self.jugador1.nombre)
        print(" Jugador 2 (Negras): " +  self.jugador2.nombre)
        print("Comienza el jugador: " + self.jugador1.nombre)
        # Se inicia la matriz del juego
        self.matriz = self.iniciar_matriz()
        self.hay_ganador = False # No hay ganador aún
        turno = 1   # Empieza en el turno 1, donde las blancas empiezan y siguen en los turnos impares, mientras que los turnos pares son de las negras
        max_turnos = 200  # Límite de turnos para evitar partidas que no acaben
        sin_captura = 0   # Contador de capturas (Es útil para una de las reglas de empate)
        while turno <= max_turnos: # Juego ciclico
            self.imprimir_tablero()
            b, n = self.contar_piezas() # Se cuentan las piezas para determinar si el juego sigue en pie
            print("Blancas: " + str(b) + " | Negras: " + str(n))
            if turno % 2 != 0: # ¿Turno impar?
                # Turno de blancas
                jugador_actual = self.jugador1
                simbolo_actual = 'B'
            else: # Si no
                # Turno de negras
                jugador_actual = self.jugador2
                simbolo_actual = 'N'
            movimientos = self.obtener_movimientos(simbolo_actual) # Se obtienen los movimientos posibles
            if not movimientos:
                # Si retorna FALSE entonces el jugador pierde, no tiene movimientos disponibles
                ganador = self.jugador1 if simbolo_actual == 'N' else self.jugador2 # El jugador rival gana
                print("\n" + jugador_actual.nombre + " no tiene movimientos posibles.")
                print("\nEl Ganador es...¡" + ganador.nombre + "!")
                self.hay_ganador = True
                break
            nueva_matriz = jugador_actual.toma_turno(self.matriz, movimientos) # Se obtiene la nueva matriz con el movimiento que el jugador actual eligió
            self.matriz = nueva_matriz # Y se inserta a la matriz actual
            
            # REGLA DE EMPATE 1: si ningun jugador ha capturado la ficha del otro en 40 movimientos, el juego acaba
            # Implementación:
            piezas_actuales = self.contar_piezas() # Se actualiza el conteo en la variable auxiliar piezas actuales
            aux_rival_ahora = piezas_actuales[1] if simbolo_actual == 'B' else piezas_actuales[0] # Se crea otra variable auxiliar llamada "rival ahora" que guarda las fichas dependiendo de quien acaba de jugar
            aux_rival_antes = n if simbolo_actual == 'B' else b # Por ultimo, una tercera variable auxiliar (rival antes) guarda la cantidad de fichas rivales original antes de la jugada dependiendo de quien jugó
            if aux_rival_ahora < aux_rival_antes: # Las compara, si el rival ahora tiene menos fichas que antes, hubo captura, y se reinicia el contador de movimientos sin captura
                sin_captura = 0
            else: # Si nadie ha capturado nada aún, se aumenta el contador
                sin_captura += 1
            if sin_captura >= 40:
                self.imprimir_tablero()
                print("\nEMPATE: se han jugado 40 movimientos sin capturar una ficha...")
                break
            
            # REGLA DE VICTORIA
            if self.encuentra_ganador(simbolo_actual): # Si el jugador actual ha eliminado todas las piezas del rival, ha ganado (es decir, si retorna a TRUE, ganó)
                self.imprimir_tablero()
                print("\nEl Ganador es...¡" + jugador_actual.nombre + "!")
                self.hay_ganador = True
                break
            
            # REGLA DE EMPATE 2: si se alcanza el límite de turnos, el juego acaba
            turno += 1
        if not self.hay_ganador and turno > max_turnos:
            self.imprimir_tablero()
            print("\nEMPATE: se alcanzó el límite de turnos...")
        print("\n=============================================")
        print("            FIN DE PARTIDA")
        print("=============================================")
