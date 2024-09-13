from collections import deque

def sucesor(n):
    return [2 * n, 2 * n + 1]

def bfs(inicio, objetivo):
    frontera = deque([inicio])
    visitados = set()
    nodos_visitados = []

    while frontera:
        estado = frontera.popleft()
        nodos_visitados.append(estado)
        if estado == objetivo:
            return nodos_visitados
        if estado not in visitados:
            visitados.add(estado)
            frontera.extend(sucesor(estado))

    return nodos_visitados

# Búsqueda primero en profundidad (DFS)
def dfs(inicio, objetivo):
    frontera = [inicio]
    visitados = set()
    nodos_visitados = []  # Lista para almacenar los nodos visitados

    while frontera:
        estado = frontera.pop()  # Sacar el último nodo (pila)
        nodos_visitados.append(estado)  # Guardar el nodo visitado
        if estado == objetivo:
            return nodos_visitados  # Devolver los nodos visitados
        if estado not in visitados:
            visitados.add(estado)
            frontera.extend(sucesor(estado))  # Agregar los sucesores (sin invertir)

    return nodos_visitados  # Devolver lo visitado si no se encuentra el objetivo

def dfs_recursiva(estado, objetivo, visitados, camino, limite):
    if limite == 0:
        return False
    camino.append(estado)
    if estado == objetivo:
        return True
    visitados.add(estado)
    for sucesor_nodo in sucesor(estado):
        if sucesor_nodo not in visitados:
            if dfs_recursiva(sucesor_nodo, objetivo, visitados, camino, limite - 1):
                return True
    camino.pop()
    return False

def dfs_con_limite(inicio, objetivo, limite=15):
    visitados = set()
    camino = []
    if dfs_recursiva(inicio, objetivo, visitados, camino, limite):
        return camino
    else:
        return []

estado_inicial = 1
estado_objetivo = 11
limite_profundidad = 15

print("Búsqueda BFS:")
resultado_bfs = bfs(estado_inicial, estado_objetivo)
print(f"Nodos visitados en BFS: {resultado_bfs}")

print("\nBúsqueda DFS con límite:") ### BUSQUEDA 
resultado_dfs = dfs_con_limite(estado_inicial, estado_objetivo, limite_profundidad)
print(f"Camino encontrado en DFS: {resultado_dfs}")

print("\nBúsqueda DFS:")            ### BUSQUEDA SOLO CON DFS TARDA UN MONTON, PERO NO LLEGA A UN RESULTADO ESTO ES DEBIDO AL SUCESOR
resultado_dfs = dfs(estado_inicial, estado_objetivo)
print(f"Nodos visitados en DFS: {resultado_dfs}")