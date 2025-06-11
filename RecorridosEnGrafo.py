import collections

class Grafo:
    def __init__(self, es_derigido=False):
        self.grafo = {}
        self.es_dirigido = es_derigido

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = set()
            print(f"Vertice '{vertice}' agregado.")
        else:
            print(f"Vertice '{vertice}' ya existe.")

    def agregar_arista(self, u, v, peso=1):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.grafo[u].add(v)
        print(f"Arista {u} -> {v} agregada.")
        if not self.es_dirigido:
            self.grafo[v].add(u)
            print(f"Arista {v} -> {u} (bidireccional) agregada.")

    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list(self.grafo[vertice])
        return []

    def existe_arista(self, u, v):
        return u in self.grafo and v in self.grafo[u]

    def bfs(self, inicio):
        visitados = set()
        cola = collections.deque()
        cola.append(inicio)
        visitados.add(inicio)
        recorrido = []
        while cola:
            vertice_actual = cola.popleft()
            recorrido.append(vertice_actual)
            print(f"Visitando: {vertice_actual}")
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return recorrido

    def dfs(self, inicio):
        visitados = set()
        recorrido = []
        def _dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            print(f"Visitando: {vertice}")
            for vecino in self.obtener_vecinos(vertice):
                if vecino not in visitados:
                    _dfs_recursivo(vecino)
        _dfs_recursivo(inicio)
        return recorrido

    def imprimir_grafo(self):
        print("\n--- Representación del Grafo ---")
        for vertice, vecinos in self.grafo.items():
            print(f"{vertice}: {{ {', '.join(vecinos)} }}")
        print("--------------------------------")

# --- INICIO DE PRUEBAS DE RECORRIDO ---

mi_grafo = Grafo(es_derigido=False)
mi_grafo.agregar_arista('A', 'B')
mi_grafo.agregar_arista('A', 'C')
mi_grafo.agregar_arista('B', 'D')
mi_grafo.agregar_arista('C', 'E')
mi_grafo.agregar_vertice('F')
mi_grafo.imprimir_grafo()

print("\nRecorrido BFS desde 'A':")
recorrido_bfs = mi_grafo.bfs('A')
print("Orden BFS:", recorrido_bfs)

print("\nRecorrido DFS desde 'A':")
recorrido_dfs = mi_grafo.dfs('A')
print("Orden DFS:", recorrido_dfs)

print("\nRecorrido BFS desde 'F' (desconectado):")
recorrido_bfs_f = mi_grafo.bfs('F')
print("Orden BFS desde 'F':", recorrido_bfs_f)

print("\nRecorrido DFS desde 'F' (desconectado):")
recorrido_dfs_f = mi_grafo.dfs('F')
print("Orden DFS desde 'F':", recorrido_dfs_f)
