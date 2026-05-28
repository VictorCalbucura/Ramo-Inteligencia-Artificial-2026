import random
import time

"""Resetear seed para generar números aleatorios diferentes cada ejecución"""
random.seed(time.time())

"""Datos del problema: mochila de camping"""
#items = [
#    ("Carpa",        5, 10),
#    ("Saco dormir",  4,  10),
#    ("Botella agua", 2,  3),
#    ("Comida",       3,  7),
#    ("Linterna",     1,  4),
#    ("Botiquín",     1,  6),
#    ("Cocinilla",    3,  6),
#    ("Abrigo",       4,  7),
#]

#capacity = 15  # Capacidad máxima en kg


items = [
    ("Carpa",        10, 120),
    ("Saco dormir",  5,  80),
    ("Botiquín",     3,  80),
    ("Cocinilla",    3,  80),
    ("Abrigo",       1,  60),
    ("Botella agua", 1,  60),
    ("Comida",       1,  60),
    ("Linterna",     1,  60),
    ("Ropa extra",   1,  60),
    ("Carne",        1,  60),
]

capacity = 25  # Capacidad máxima en kg

n_items = len(items)

"""Mundo espacial para simular la 'comida' del pseudocódigo"""
GRID_WIDTH = 5
GRID_HEIGHT = 5
FOOD_CELLS = 8
MAX_FOOD_PER_CELL = 3
FOOD_ENERGY = 4


"""Funciones auxiliares"""
def random_solution():
    """Vector binario aleatorio."""
    return [random.randint(0, 1) for _ in range(n_items)]

def random_position():
    """Posición aleatoria dentro de la rejilla."""
    return [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]

def initialize_food_world():
    """Crea la rejilla con comida distribuida aleatoriamente."""
    world = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for _ in range(FOOD_CELLS):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        world[y][x] += random.randint(1, MAX_FOOD_PER_CELL)
    return world

def move_to_neighbor(position):
    """Mueve el abejorro a una celda vecina sin salir de la rejilla."""
    x, y = position
    neighbors = []
    if x > 0:
        neighbors.append([x - 1, y])
    if x < GRID_WIDTH - 1:
        neighbors.append([x + 1, y])
    if y > 0:
        neighbors.append([x, y - 1])
    if y < GRID_HEIGHT - 1:
        neighbors.append([x, y + 1])
    return random.choice(neighbors) if neighbors else position[:]

def consume_food(food_world, position):
    """Consume una unidad de comida si la celda tiene alimento."""
    x, y = position
    if food_world[y][x] > 0:
        food_world[y][x] -= 1
        return FOOD_ENERGY
    return 0

def evaluate(solution):
    """Devuelve (valor_total, peso_total, fitness_penalizado)."""
    total_weight = 0
    total_value = 0
    for bit, (_, w, v) in zip(solution, items):
        if bit == 1:
            total_weight += w
            total_value += v

    """Penalización fuerte: cualquier solución que exceda la capacidad queda castigada"""
    if total_weight > capacity:
        excess = total_weight - capacity
        fitness = max(0, total_value - excess * 100)  # Penalización severa
    else:
        fitness = total_value

    return total_value, total_weight, fitness

def mutate(solution, mutation_rate=0.1):
    """Mutación bit a bit con intensidad adaptativa."""
    new_sol = solution[:]
    for i in range(len(new_sol)):
        if random.random() < mutation_rate:
            new_sol[i] = 1 - new_sol[i]
    return new_sol

def crossover(parent1, parent2):
    """Recombinación de dos soluciones (crossover de un punto)."""
    point = random.randint(1, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child

def local_search(solution, iterations=3):
    """Búsqueda local: prueba cambiar cada bit y mantiene mejoras."""
    best_sol = solution[:]
    _, _, best_fit = evaluate(best_sol)
    
    for _ in range(iterations):
        for i in range(len(best_sol)):
            # Invertir bit
            test_sol = best_sol[:]
            test_sol[i] = 1 - test_sol[i]
            _, _, test_fit = evaluate(test_sol)
            
            # Si mejora, aceptar
            if test_fit > best_fit:
                best_sol = test_sol
                best_fit = test_fit
    
    return best_sol

"""Bumblebees Algorithm mejorado"""
def bumblebees_knapsack(
    n_bees=50,
    max_generations=500,
    base_life=20,
    mutation_rate=0.1,
    elite_fraction=0.2,
    verbose=False
):
    """Inicializar población de abejorros"""
    food_world = initialize_food_world()
    bees = []
    for _ in range(n_bees):
        sol = random_solution()
        _, _, fit = evaluate(sol)
        life = base_life + fit  # Más vida para mejor fitness
        bees.append({"solution": sol, "fitness": fit, "life": life, "position": random_position()})

    """Mejor solución global"""
    best_bee = max(bees, key=lambda b: b["fitness"])
    best_solution = best_bee["solution"][:]
    best_fitness = best_bee["fitness"]

    for gen in range(max_generations):
        """Ordenar por fitness"""
        bees.sort(key=lambda b: b["fitness"], reverse=True)
        
        """Detectar si hay mejora"""
        fitness_mejoró = False
        if bees[0]["fitness"] > best_fitness:
            best_fitness = bees[0]["fitness"]
            best_solution = bees[0]["solution"][:]
            fitness_mejoró = True

        """Mostrar estadísticas cada 20 generaciones"""
        if verbose and gen % 20 == 0:
            fitnesses = [b["fitness"] for b in bees]
            avg_fitness = sum(fitnesses) / len(fitnesses)
            max_fitness = max(fitnesses)
            min_fitness = min(fitnesses)
            print(f"\n{'='*70}")
            print(f"GENERACION {gen}")
            print(f"{'='*70}")
            print(f"[ESTADISTICAS DE LA POBLACION]")
            print(f"   * Fitness MAXIMO actual: {max_fitness}")
            print(f"   * Fitness MINIMO actual: {min_fitness}")
            print(f"   * Fitness PROMEDIO: {avg_fitness:.2f}")
            print(f"   * MEJOR GLOBAL encontrado: {best_fitness}")
            if fitness_mejoró:
                print(f"   >> ¡MEJORA DETECTADA! Nuevo mejor fitness: {best_fitness}")
            print(f"{'='*70}\n")

        """Lista de élite"""
        elite_count = max(1, int(elite_fraction * n_bees))
        elite_bees = bees[:elite_count]

        new_bees = []
        nacimientos = 0
        muertes = 0
        mutaciones = 0
        crossovers = 0
        comidas = 0

        for b in bees:
            """Moverse a una celda vecina y buscar comida"""
            b["position"] = move_to_neighbor(b["position"])
            food_gain = consume_food(food_world, b["position"])
            if food_gain > 0:
                comidas += 1
                b["life"] += food_gain
                b["position"] = [0, 0]  # Regresa al nido tras encontrar comida

            """Reducir vida"""
            b["life"] -= 1

            """Si muere, se reemplaza por una copia mutada de un élite"""
            if b["life"] <= 0:
                muertes += 1
                nacimientos += 1
                parent = random.choice(elite_bees)
                """Combinar élite con mutación y búsqueda local"""
                new_sol = mutate(parent["solution"], mutation_rate * 1.5)
                new_sol = local_search(new_sol, iterations=2)
                _, _, new_fit = evaluate(new_sol)
                new_life = base_life + int(new_fit / 2)  # Vida proporcional al fitness
                new_bees.append({"solution": new_sol, "fitness": new_fit, "life": new_life, "position": random_position()})
            else:
                """Sobrevivientes: combinan mutación y crossover"""
                """70% mutación, 30% crossover con élite"""
                if random.random() < 0.7:
                    new_sol = mutate(b["solution"], mutation_rate)
                    mutaciones += 1
                else:
                    partner = random.choice(elite_bees)
                    new_sol = crossover(b["solution"], partner["solution"])
                    new_sol = mutate(new_sol, mutation_rate * 0.5)
                    crossovers += 1
                
                _, _, new_fit = evaluate(new_sol)
                
                """Actualizar vida de forma más realista"""
                if new_fit > b["fitness"]:
                    b["life"] += min(5, int((new_fit - b["fitness"]) / 2))
                else:
                    b["life"] -= 1  # Penalizar si no mejora
                
                b["solution"] = new_sol
                b["fitness"] = new_fit
                new_bees.append(b)

        # Mostrar operaciones genéticas cada 20 generaciones
        if verbose and gen % 20 == 0 and gen > 0:
            print(f"[OPERACIONES GENETICAS]")
            print(f"   * Muertes/Nacimientos: {muertes}")
            print(f"   * Mutaciones: {mutaciones}")
            print(f"   * Crossovers: {crossovers}")
            print(f"   * Elites en poblacion: {elite_count}")
            print(f"   * Celdas con comida consumida: {comidas}")

        bees = new_bees

    """Evaluar mejor solución final"""
    total_value, total_weight, _ = evaluate(best_solution)
    return best_solution, total_value, total_weight

"""Ejecutar el algoritmo"""
if __name__ == "__main__":
    best_sol, best_val, best_w = bumblebees_knapsack(verbose=True)

    print("\nMejor solución encontrada:")
    for bit, (name, w, v) in zip(best_sol, items):
        if bit == 1:
            print(f"- {name} (peso {w}, valor {v})")
    print(f"Peso total: {best_w}")
    print(f"Valor total: {best_val}")