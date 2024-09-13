from AgenteIA.AgenteBuscador import AgenteBuscador


class AgenteViajero(AgenteBuscador):

    def __init__(self):
        AgenteBuscador.__init__(self)
        self.distancias = {}
        self.lineal = {}

    def generar_hijos(self, e):
        return self.get_percepciones()[e]

    def get_costo(self, camino):
        return sum(self.distancias[(camino[i], camino[i + 1])] for i in range(len(camino) - 1))

    def get_heuristica(self, camino):
        return self.lineal[camino[-1]]
