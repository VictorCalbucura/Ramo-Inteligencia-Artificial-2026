# ESTADO DEL JUEGO
# Integrantes:
# Victor Calbucura
# Denisse Maldonado
# Matias Salgado
# Angel Vargas
class estado:
    def __init__(self, EA, EP, A, n, turno):
        self.valor = EA # Matriz
        self.padre = EP # Estado padre
        self.accion = A # Acción que llevó a este estado
        self.nivel = n # Nivel de profundidad
        self.turno = turno # Quien jugó para llegar acá si B o N
        self.heuristica = None # Huristica

    def get_estado(self):
        return self.valor

    def get_padre(self):
        return self.padre

    def get_accion(self):
        return self.accion

    def get_nivel(self):
        return self.nivel

    def get_turno(self):
        return self.turno

    def get_heuristica(self):
        return self.heuristica

    def set_heuristica(self, h):
        self.heuristica = h

    def __eq__(self, e):
        return self.valor == e
