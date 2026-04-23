# JUGADOR DEL JUEGO DAMAS
# Integrantes:
# Victor Calbucura
# Denisse Maldonado
# Matias Salgado
# Angel Vargas
from busqueda import busqueda

class jugador:
    # Se crearon nuevos atributos y métodos para el jugador.

    def __init__(self, nombre, tipo, simbolo):
        self.nombre = nombre
        self.cant_turnos = 0
        self.es_bot = tipo
        self.simbolo = simbolo # B para Blancas y N para Negras (B siempre va primero)                   
        self.simbolo_dama = simbolo.lower() # Cuando una dama llega al final, se activa esto para determinar que es reina
        
    def set_simbolo(self, simbolo):
        self.simbolo = simbolo
        self.simbolo_dama = simbolo.lower()

    def toma_turno_automatico(self, matriz):
        if self.simbolo == 'B':
            s_max = 'B'
            s_min = 'N'
        else:
            s_max = 'N'
            s_min = 'B'

        bot = busqueda(matriz, s_max, s_min)
        nueva_matriz = bot.inicia_busqueda() # entrega el mejor movimiento para ESE TURNO.
        if nueva_matriz is None:
            return matriz
        return nueva_matriz

    def toma_turno_por_teclado(self, matriz, movimientos_posibles): #Se modificó este método para no permitir que el humano formule movimientos ilegales.
        print(f"\n\nTurno de: {self.nombre} ({self.simbolo})") 
        print("Movimientos posibles:")

        # Mostrar movimientos numerados y dejar que el humano elija a su gusto
        for i, mov in enumerate(movimientos_posibles): # Cada movimiento se enumera y se muestra su origen o ficha elegida (x1, y1) y su destino (x2, y2) revisar código busqueda para entender como se obtienen esos movimientos
            if len(mov) == 2: # Si el movimiento solo tiene un origen y destino, es un movimiento simple o captura simple
                origen, destino = mov 
                print(f"  [{i}] ({origen[0]},{origen[1]}) -> ({destino[0]},{destino[1]})")
            else:  # Si el movimiento tiene más de 2 posiciones, por ejemplo, origen, destino1 y destino2, es una captura múltiple si o si
                ruta = " -> ".join([f"({p[0]},{p[1]})" for p in mov])
                print(f"  [{i}] {ruta}  (captura múltiple)")

        while True: # Bucle ciclico
            try:
                eleccion = int(input("Elige el número del movimiento: ")) # Se pide que ingrese la elección por número
                if 0 <= eleccion < len(movimientos_posibles): #Si ingresa un número mayor a 0 y menor a la cantidad de elección
                    break
                else:
                    print("Número fuera de rango, intenta de nuevo.") # Si no, se repite el ciclo hasta que ingrese una elección válida.
            except ValueError:
                print("Entrada inválida, ingresa un número.")

        movimiento = movimientos_posibles[eleccion] # Se ingresa/obtiene el movimiento elegido

        # Aplicar el movimiento en la matriz
        nueva_matriz = self.aplicar_movimiento(matriz, movimiento) # Como es una matriz con múltiples movimientos, se requiere añadir un método nuevo para aplicar el movimiento elegido
        return nueva_matriz

    def aplicar_movimiento(self, matriz, movimiento):
        # Aplica un movimiento elegido sobre la matriz y retorna una nueva matriz
        nueva = [fila[:] for fila in matriz] # Se crea una copia de la matriz original para no modificarla directamente
        pieza = nueva[movimiento[0][0]][movimiento[0][1]] # Guarda la pieza que se va a mover en la variable "pieza"
        nueva[movimiento[0][0]][movimiento[0][1]] = ' ' # y luego esa pieza se borra de su posición original

        for i in range(1, len(movimiento)): # Se recorre la lista de movimientos que tiene que aplicar
            origen = movimiento[i - 1] # Se obtiene el origen
            destino = movimiento[i] # y el destino
            fila_med = (origen[0] + destino[0]) // 2 # Calcula la distancia que hay entre el origen
            col_med = (origen[1] + destino[1]) // 2 # y el destino
            if abs(destino[0] - origen[0]) == 2: # Y si existe una distancia de 1 casilla entre el origen y el destino entonces existe una ficha que se capturó al hacer el movimiento
                nueva[fila_med][col_med] = ' ' # Por ende, esa ficha se borra de la matriz

        destino_final = movimiento[-1] # Se obtiene el destino final
        nueva[destino_final[0]][destino_final[1]] = pieza # Y se coloca la pieza en su nuevo destino

        # En cuyo caso que la pieza que se movió llega hasta el final 
        if pieza == 'B' and destino_final[0] == 7: # Siendo una pieza normal blanca
            nueva[destino_final[0]][destino_final[1]] = 'b'
        if pieza == 'N' and destino_final[0] == 0: # o negra
            nueva[destino_final[0]][destino_final[1]] = 'n'
        # Entonces es coronada y se convierten en reina
        return nueva # Finalmente, se obtiene la nueva matriz con el movimiento aplicado y los cambios realizados

    def toma_turno(self, matriz, movimientos_posibles): 
        self.cant_turnos += 1
        
        if self.es_bot:
            return self.toma_turno_automatico(matriz)
        return self.toma_turno_por_teclado(matriz, movimientos_posibles) # se mantuvo la misma logica del método original, pero se introdujo el atributo "movimientos posibles"
