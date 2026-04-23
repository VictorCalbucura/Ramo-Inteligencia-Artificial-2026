# BUSQUEDA DEL MEJOR RESULTADO
# Integrantes:
# Victor Calbucura
# Denisse Maldonado
# Matias Salgado
# Angel Vargas
from estado import estado
import math
import sys
sys.setrecursionlimit(200000)

class busqueda:
    def __init__(self, EI, s_max, s_min):
        self.estado_inicial = estado(EI, None, "Origen", 0, s_max) # Estado inicial del tablero
        self.estado_solucion = None
        self.s_max = s_max          
        self.s_min = s_min        
        self.s_max_dama = s_max.lower()
        self.s_min_dama = s_min.lower()
        self.estados_descubiertos = 0

    def es_propia(self, pieza, simbolo):
        # Revisa si la ficha es del mismo color
        return pieza == simbolo or pieza == simbolo.lower()

    def es_rival(self, pieza, simbolo):
        # Revisa si la ficha pertenece al rival
        rival = 'N' if simbolo == 'B' else 'B'
        return pieza == rival or pieza == rival.lower()

    def obtener_direcciones(self, pieza):
        # Retorna las direcciones de movimiento segun la pieza
        if pieza == 'B':
            return [(1, -1), (1, 1)] # Blancas bajan diagonalmente en matriz logica (ya que logicamente el 0 va arriba y el 8 abajo), pero suben en tablero impreso (0 abajo y 8 arriba)
        elif pieza == 'N':
            return [(-1, -1), (-1, 1)] # Lo mismo pasa con las Negras
        else:
            return [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # La dama puede moverse en las 4 direcciones diagonales

    def casilla_esta_en_tablero(self, f, c):
        # Verifica si la casilla existe en el tablero
        return 0 <= f < 8 and 0 <= c < 8

    def capturas_desde_casilla(self, m, f, c, pieza, visitados):
        #Genera todas las capturas posibles desde una casilla
        dirs = self.obtener_direcciones(pieza)
        encontradas = []

        for df, dc in dirs:
            f_rival = f + df
            c_rival = c + dc
            f_dest  = f + 2*df
            c_dest  = c + 2*dc

            if not self.casilla_esta_en_tablero(f_dest, c_dest):
                continue

            simbolo = 'B' if pieza in ('B', 'b') else 'N'
            if not self.es_rival(m[f_rival][c_rival], simbolo):
                continue
            if m[f_dest][c_dest] != ' ':
                continue
            if (f_rival, c_rival) in visitados:
                continue

            # Simula la captura para probar la jugada
            nueva = [fila[:] for fila in m]
            nueva[f][c] = ' '
            nueva[f_rival][c_rival] = ' '
            nueva[f_dest][c_dest] = pieza

            # Coronacion durante la cadena
            pieza_siguiente = pieza
            if pieza == 'B' and f_dest == 7:
                pieza_siguiente = 'b'
                nueva[f_dest][c_dest] = 'b'
            if pieza == 'N' and f_dest == 0:
                pieza_siguiente = 'n'
                nueva[f_dest][c_dest] = 'n'

            nuevos_visitados = visitados | {(f_rival, c_rival)}
            sub_capturas = self.capturas_desde_casilla(nueva, f_dest, c_dest, pieza_siguiente, nuevos_visitados)

            if sub_capturas:
                for sub in sub_capturas:
                    encontradas.append([(f, c)] + sub)
            else:
                encontradas.append([(f, c), (f_dest, c_dest)])

        return encontradas

    def obtener_movimientos(self, m, simbolo):
        #Retorna los movimientos legales de una ficha
        dama = simbolo.lower()
        capturas = []
        simples = []

        for f in range(8):
            for c in range(8):
                pieza = m[f][c]
                if pieza not in (simbolo, dama):
                    continue

                # Busca capturas primero
                caps = self.capturas_desde_casilla(m, f, c, pieza, set())
                capturas.extend(caps)

                # Busca movimientos simples
                for df, dc in self.obtener_direcciones(pieza):
                    nf, nc = f + df, c + dc
                    if self.casilla_esta_en_tablero(nf, nc) and m[nf][nc] == ' ':
                        simples.append([(f, c), (nf, nc)])

        # Si hay capturas se usan primero
        if capturas:
            return capturas
        return simples

    def jugar_movimiento(self, m, movimiento):
        # Copia el tablero para no cambiar el original
        nueva = [fila[:] for fila in m]
        pieza = nueva[movimiento[0][0]][movimiento[0][1]]
        nueva[movimiento[0][0]][movimiento[0][1]] = ' '

        for i in range(1, len(movimiento)):
            origen  = movimiento[i - 1]
            destino = movimiento[i]
            if abs(destino[0] - origen[0]) == 2:
                fila_med = (origen[0] + destino[0]) // 2
                col_med  = (origen[1] + destino[1]) // 2
                nueva[fila_med][col_med] = ' '

        df = movimiento[-1]
        nueva[df[0]][df[1]] = pieza

        # Coronacion al llegar al borde final
        if pieza == 'B' and df[0] == 7:
            nueva[df[0]][df[1]] = 'b'
        if pieza == 'N' and df[0] == 0:
            nueva[df[0]][df[1]] = 'n'

        return nueva

    def juego_terminado(self, e):
        # Revisa si el rival ya no puede mover
        m = e.get_estado()
        turno = e.get_turno()
        rival = 'N' if turno == 'B' else 'B'
        return len(self.obtener_movimientos(m, rival)) == 0

    def calcular_heuristica(self, e): # Aquí viene la evaluación y nucleo del algoritmo
        m = e.get_estado() # Se obtiene el estado del tablero actual
        puntaje = 0 # Inicialmente tiene peso 0

        piezas_max = 0 # Contador de todas las piezas, rivales y propias
        dama_max  = 0
        piezas_min = 0
        dama_min  = 0

        for f in range(8): # Recorriendo matriz
            for c in range(8):
                p = m[f][c] # Entonces la pieza que se encuentra en esa posición puede o no sumar peso a ese movimiento particular
                if p == self.s_max: # ¿Y como se determina ese valor? Simple, si es propia
                    piezas_max += 1 # La suma
                    # Y suma por cada casilla que avance esta pieza (es decir, si avanza 2, es prioritario este movimiento)
                    avance = f if self.s_max == 'B' else (7 - f)
                    puntaje += 1 + avance * 0.2 # En este caso, por cada pieza suma 1 punto y por cada avance suma 0.2 puntos adicionales
                elif p == self.s_max_dama:
                    dama_max += 1 # Suma las damas propias (si tiene)
                    puntaje += 2 # Por cada dama suma 2 puntos de peso al estado
                    puntaje += 0.4 if 2 <= f <= 5 and 2 <= c <= 5 else 0 # Y como se prefiere que los damas estén más cerca del centro, se suman 0.4 puntos adicionales si el dama está en las filas o columnas centrales
                elif p == self.s_min: # Pero si es del rival
                    piezas_min += 1 # Se suma esa pieza rival
                    avance = f if self.s_min == 'B' else (7 - f) # Restando puntaje por cada casilla que avance el rival
                    puntaje -= 1 + avance * 0.2 # Especificamente, 1 punto por pieza de rival y 0.2 puntos por cada casilla que avance
                elif p == self.s_min_dama: # Y si el rival tiene una dama
                    dama_min += 1 # Se suma esa dama
                    puntaje -= 2 # Y se restan 2 puntos por cada dama rival
                    puntaje -= 0.4 if 2 <= f <= 5 and 2 <= c <= 5 else 0 # T se restan 0.4 puntos adicionales si esa dama está cerca del centro

        # Hace la diferencia entre piezas propias y rivales, en una ponderación diferente
        puntaje += (piezas_max - piezas_min) * 0.5 # Es prioritario tener más piezas que el rival
        puntaje += (dama_max - dama_min) * 1.5 # Pero es aún más prioritario tener más damas que el rival
        # Así se obtiene el peso inicial de ese estado, pasando pieza por pieza, pero falta un detalle final

        # Se penaliza o beneficia si alguno se quedó sin movimientos
        turno_siguiente = 'N' if e.get_turno() == 'B' else 'B' # Depende del turno siguiente
        movs = self.obtener_movimientos(m, turno_siguiente) # Calcula sus movimientos posibles
        if len(movs) == 0: # Si no tiene
            if turno_siguiente == self.s_min: # Si el siguiente turno sin movimientos es del rival
                puntaje += 1000   # Se gana automaticamente, entonces es una prioridad altisima y es el estado que se quiere a toda costa
            else: # Si es propio
                puntaje -= 1000   # Automaticamente se pierde, lo que hace que sea un estado que se quiere evitar a toda costa

        return puntaje # Se retorna el peso total de ese estado (Recordar que es un peso de un estado, aún falta revisar todos los demás)

    def minimax_ab(self, e, profundidad, alpha, beta, es_max): # Para ello se requiere minimax con poda alpha-beta, para decidir el mejor y podar los estados inutilizables
        # Revisa muchos estados para encontrar la mejor jugada
        self.estados_descubiertos += 1

        if profundidad == 0 or self.juego_terminado(e): # Si se llegó a la profundidad máxima o el juego terminó, se evalúa ese estado
            h = self.calcular_heuristica(e) # Se calcula el peso de ese estado
            e.set_heuristica(h) # Y se guarda ese peso en el estado
            return h # Se retorna el peso de ese estado, que es lo que se quiere maximizar o minimizar dependiendo del turno

        m = e.get_estado()
        simbolo = self.s_max if es_max else self.s_min
        movimientos = self.obtener_movimientos(m, simbolo)

        if not movimientos: # Si no hay movimientos
            h = self.calcular_heuristica(e) # Se evalua el estado actual
            e.set_heuristica(h) 
            return h # Y se retorna la heuristica

        mejor_mov = None # Aquí se guardará el mejor movimiento encontrado en esa rama de arbol

        if es_max: # Si el turno es del bot
            maximo = -math.inf # Se inicia el máximo como el peor valor posible
            for mov in movimientos: # Se revisar TODOS los movimientos posibles
                nueva_m = self.jugar_movimiento(m, mov) # Se juega el movimiento y se obtiene esa matriz
                hijo = estado(nueva_m, e, mov, e.get_nivel() + 1, simbolo) # Se evalua
                val = self.minimax_ab(hijo, profundidad - 1, alpha, beta, False)
                if val > maximo: # Si el valor otorgado es el máximo encontrado
                    maximo = val # Se actualiza el máximo y se guarda ese movimiento como el mejor
                    mejor_mov = nueva_m
                alpha = max(alpha, val) # Alpha beta
                if beta <= alpha:
                    break
            if mejor_mov is not None: 
                self.estado_solucion = mejor_mov # Si se encontró un movimiento mejor, se guarda como solución
            return maximo # Se retorna el valor máximo encontrado

        else: # Si el turno es del rival, es todo lo contrario, se busca minimizar
            minimo = math.inf
            for mov in movimientos:
                nueva_m = self.jugar_movimiento(m, mov)
                hijo = estado(nueva_m, e, mov, e.get_nivel() + 1, simbolo)
                val = self.minimax_ab(hijo, profundidad - 1, alpha, beta, True)
                if val < minimo:
                    minimo = val
                    mejor_mov = nueva_m
                beta = min(beta, val)
                if beta <= alpha:
                    break
            if mejor_mov is not None:
                self.estado_solucion = mejor_mov
            return minimo # Y retorna el minimo

    def inicia_busqueda(self):
        # Prueba varias profundidades para buscar mejor jugada
        self.estado_solucion = None
        mejor_valor = -math.inf # Deja el mejor valor como el peor posible
        lista_soluciones = []

        for profundidad in range(2, 7):  # profundidad 2 a 7
            parcial = self.minimax_ab(self.estado_inicial, profundidad, -math.inf, math.inf, True)
            lista_soluciones.append([self.estado_solucion, parcial])
            mejor_valor = max(mejor_valor, parcial)

        for sol in lista_soluciones: # Busca la mejor solución
            if sol[1] == mejor_valor:
                self.estado_solucion = sol[0]
                break

        # Para que no devuelva None, se aplica un fallback
        if self.estado_solucion is None:
            m = self.estado_inicial.get_estado() # Si no se encontró ningún movimiento mejor, se obtiene el estado inicial
            movimientos = self.obtener_movimientos(m, self.s_max) 
            if movimientos:
                self.estado_solucion = self.jugar_movimiento(m, movimientos[0])
            else:
                self.estado_solucion = m

        print(f"Estados descubiertos: {self.estados_descubiertos}") 
        return self.estado_solucion # Retorna el estado de la solución
