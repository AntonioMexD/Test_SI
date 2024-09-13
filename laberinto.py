# Función sucesor
def sucesor(n):
    return [2 * n, 2 * n + 1]

# Búsqueda primero en profundidad (DFS) recursiva
def dfs_recursiva(estado, objetivo, visitados, camino, limite):
    if limite == 0:
        return False  # No continuar si se llega al límite
    camino.append(estado)  # Guardar el nodo visitado en el camino
    if estado == objetivo:
        return True  # Se encontró el objetivo
    visitados.add(estado)
    for sucesor_nodo in sucesor(estado):
        if sucesor_nodo not in visitados:
            if dfs_recursiva(sucesor_nodo, objetivo, visitados, camino, limite - 1):
                return True
    camino.pop()  # Eliminar el nodo del camino si no lleva al objetivo
    return False

# Función que envuelve la DFS con un límite
def dfs_con_limite(inicio, objetivo, limite=15):
    visitados = set()
    camino = []
    if dfs_recursiva(inicio, objetivo, visitados, camino, limite):
        return camino
    else:
        return []  # Si no encuentra el objetivo, devuelve una lista vacía

# Prueba de la búsqueda en profundidad con límite
estado_inicial = 1
estado_objetivo = 11
limite_profundidad = 15

# Ejecutar DFS con límite
print("\nBúsqueda DFS con límite:")
resultado_dfs = dfs_con_limite(estado_inicial, estado_objetivo, limite_profundidad)
print(f"Camino encontrado en DFS: {resultado_dfs}")
