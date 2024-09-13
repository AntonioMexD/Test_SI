
from AgenteViajero import AgenteViajero
from Question5 import bfs, dfs_con_limite, dfs

if __name__ == "__main__":
    
    #Question # 5
    estado_inicial = 1
    estado_objetivo = 11
    limite_profundidad = 15
    
    #antonio = AgenteViajero()
    antonio = bfs(estado_inicial, estado_objetivo)
    antonio = dfs_con_limite(estado_inicial, estado_objetivo, limite_profundidad)
    antonio = dfs(estado_inicial, estado_objetivo) ### Solo DFS no llega a un resultado