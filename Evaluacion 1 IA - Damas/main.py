# MAIN PARA INICIAR JUEGO
# Para probar el juego, se debe eliminar el comentario de la seccion que debe jugar (abajo del comentario del tipo de juego)
# Integrantes:
# Victor Calbucura
# Denisse Maldonado
# Matias Salgado
# Angel Vargas
from jugador import jugador
from tablero import tablero

if __name__ == "__main__":
    # Humano vs Bot
    #nombre = input("Ingresa tu nombre: ")
    #j1 = jugador(nombre, False, 'B')
    #j2   = jugador("BOT", True, 'N')
    
    # Humano vs Humano
    #nombre1 = input("Nombre del Jugador 1 (Blancas ○): ")
    #nombre2 = input("Nombre del Jugador 2 (Negras  ●): ")
    #j1 = jugador(nombre1, False, 'B')
    #j2 = jugador(nombre2, False, 'N')
    
    # Bot vs Bot
    j1 = jugador("BOT-Blancas", True, 'B')
    j2 = jugador("BOT-Negras",  True, 'N')

    juego = tablero(j1, j2)
    juego.inicia_partida()
