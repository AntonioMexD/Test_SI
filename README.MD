### Estudiante : Antonio Medina Padilla

# 1.	Identifique la descripción medida de rendimiento, entorno, acciones, percepciones : 
•	Agente Robot que juega Futbol
o	Rendimiento: Goles al arco, victorias, pases
o	Entorno: Cancha de futbol, sintetico, cemento, jugadores, pelota, clima
o	Acciones: Correr, pasar, amagar, patear, quitar, posición.
o	Percepciones: Ubicación de la pelota, compañeros, oponentes, distancia portería.
•	Agente Delivery
o	Rendimiento: Entregas a tiempo, eficiencia de la ruta, satisfacción del cliente.
o	Entorno: Calles, trafico, clima, clientes.
o	Acciones: Conducir, recoger pedidos, entregar pedidos o productos.
o	Percepciones: Trafico, direcciones, tiempo estimado de entrega.
# 2.	Para los casos anteriores, caracterice su entorno explicando el porque de su elección. 
o	Para el Robot que juega al fútbol, el entorno es dinámico y parcialmente observable. Los objetos en el entorno jugadores y pelota se mueven constantemente y el robot no tiene visibilidad completa de todo el campo.
o	Para el Agente Delivery, el entorno es dinámico y completamente observable. El tráfico y las condiciones climáticas pueden cambiar, pero las calles y la localización del cliente son fijas.
# 3.	 Diferencias y similitudes entre un agente reactivo simple, agente basado en modelos y agente basado en objetivos. 
o	Agente reactivo simple: Toma decisiones basadas solo en las percepciones actuales del entorno, sin almacenar información pasada ni anticipar el futuro. Ejemplo: Un termostato.
o	Agente basado en modelos: Tiene una representación interna del mundo (un modelo) que le permite recordar y anticipar eventos futuros. Ejemplo: Un robot aspiradora que recuerda el diseño del hogar.
o	Agente basado en objetivos: No solo usa un modelo, sino que también tiene un objetivo específico que persigue, optimizando sus acciones para alcanzarlo. Ejemplo: Un agente de planificación de rutas.
o	Similitudes: Todos los agentes perciben su entorno y realizan acciones para cambiarlo.
o	Diferencias: El agente reactivo es el más simple, mientras que el agente basado en modelos y objetivos tiene más complejidad en su toma de decisiones.
# 4.	Sea una frontera ordenada por f(n) = (2w)g(n) + wh(n). ¿Para qué valores del w está garantizado que el algoritmo sea óptimo? ¿Qué tipo de búsqueda realiza cuando w = 0, ¿cuándo w = 1? y ¿cuándo w = 2 
a.	Para w=0:
f(n)=2g(n)f(n)=2g(n). La búsqueda ignora la heurística y solo considera el costo acumulado g(n)g(n).
Búsqueda de costo uniforme, ya que siempre expande el nodo con el costo acumulado más bajo, lo que garantiza una solución óptima, deja de lado la heuristica.
b.	Para w=1:
f(n)=2g(n)+h(n)f(n)=2g(n)+h(n). En este caso, se toma en cuenta tanto el costo acumulado como la heurística.
Búsqueda A*, pero con peso extra en el costo acumulado. Su heurística es admisible, esto es un algoritmo optimo.
c.	Para w=2:
f(n)=4g(n)+2h(n)f(n)=4g(n)+2h(n). En este caso, tanto el costo acumulado como la heurística tienen más peso.
Este enfoque podría ser similar a una búsqueda con heurística ponderada (Weighted A*)


# 5. Considere un espacio de estados donde el estado comienzo es el número 1 y la función sucesor para el estado n devuelve 2 estados, los números 2n y 2n + 1. a) Dibuje el trozo del espacio de estados para los estados del 1 al 15. b) Supongamos que el estado objetivo es el 11. Enumere el orden en el que serán visitados los nodos por la búsqueda primero en anchura, búsqueda primero en profundidad. c) Programar el agente.

1 -> [2, 3]
2 -> [4, 5]
3 -> [6, 7]
4 -> [8, 9]
5 -> [10, 11]
6 -> [12, 13]
7 -> [14, 15]

# Búsqueda primero en anchura (Breadth-First Search - BFS)

La búsqueda en anchura explora el árbol nivel por nivel, comenzando por el nodo raíz (1) y luego los siguientes en el mismo nivel, y así sucesivamente.

Orden en el que se visitan los nodos hasta encontrar el objetivo 11:

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.
# Búsqueda primero en profundidad (Depth-First Search - DFS)

La búsqueda en profundidad explora primero lo más profundo posible a lo largo de cada rama antes de retroceder.

Orden en el que se visitan los nodos hasta encontrar el objetivo 11:

1, 2, 5, 11.