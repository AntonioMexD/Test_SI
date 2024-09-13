1 -> [2, 3]
2 -> [4, 5]
3 -> [6, 7]
4 -> [8, 9]
5 -> [10, 11]
6 -> [12, 13]
7 -> [14, 15]

b) Orden de visita de los nodos según las búsquedas
# Búsqueda primero en anchura (Breadth-First Search - BFS)

La búsqueda en anchura explora el árbol nivel por nivel, comenzando por el nodo raíz (1) y luego los siguientes en el mismo nivel, y así sucesivamente.

Orden en el que se visitan los nodos hasta encontrar el objetivo 11:

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.
# Búsqueda primero en profundidad (Depth-First Search - DFS)

La búsqueda en profundidad explora primero lo más profundo posible a lo largo de cada rama antes de retroceder.

Orden en el que se visitan los nodos hasta encontrar el objetivo 11:

1, 2, 5, 11.