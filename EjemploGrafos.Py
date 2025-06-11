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
            print(f"Vertice '{vertice}' ya exite")
    
    def agregar_arista(self, u,v, peso = 1):
        # Aseguramiento de los vertices existan en el grafo
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        self.grafo[u].add(v) #Anadir arista
        print(f"Arista {u} -> agregada.")
        
        #si no es dirigido, anadir la arista en la direccion opuesta
        #osea una arista bidireccional
        if not self.es_dirigido:
            self.grafo[v].add(u)
            print(f"Arista {v} -> {u} (bidireccional) agregada.")
            
    def obtener_vecinos(self, vertice):
        if vertice in self.grafo:
            return list(self.grafo[vertice]) #se trasforma a una lista para retornarla
        return[]# si el vertice no existe, retorna nada
    
    def existe_arista(self, u, v):
        #Verifica si ambos vertices existen
        return u in self.grafo and v in self.grafo[u]
    
    def bfs(self, inicio):
        visitados = set()
        cola = collections.deque()
        
        cola.append(inicio)
        visitados.add(inicio)
        
        recorrido = []
        
        while cola:
            vertice_altual = cola.popleft()
            recorrido.append(vertice_altual)
            print(f"Visitando: {vertice_altual}")
        
            for vecino in self.obtener_vecinos(vertice_altual):
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
    # Iniciar el DFS desde el vértice dado
        _dfs_recursivo(inicio)
        return recorrido
    
    def imprimir_grafo(self):
        print("\n--- Representación del Grafo ---")
        for vertice, vecinos in self.grafo.items():
            print(f"{vertice}: {{', '.join(vecinos)}}")
        print("-------------------------------")

    def es_conexo(self):
        if not self.grafo:
            return True

        # Tomar el primer vértice para iniciar el BFS/DFS
        primer_vertice = next(iter(self.grafo))

        # Realizar un BFS desde el primer vértice
        recorrido_bfs = self.bfs(primer_vertice)

    def encontrar_camino(self, inicio, fin):
        if inicio not in self.grafo or fin not in self.grafo:
            print(f"Error: '{inicio}' o '{fin}' no existen en el grafo.")
            return []

        cola = collections.deque()
        visitados = set()
        padres = {}  # Para reconstruir el camino: padres[hijo] = padre

        cola.append(inicio)
        visitados.add(inicio)
        padres[inicio] = None  # El inicio no tiene padre

        while cola:
            vertice_actual = cola.popleft()

            if vertice_actual == fin:
                # Hemos llegado al destino, reconstruir el camino
                camino = []
                temp = fin
                while temp is not None:
                    camino.append(temp)
                    temp = padres[temp]
                return camino[::-1]  # Invertir el camino para que vaya de inicio a fin

            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual  # Guardar el padre
                    cola.append(vecino)

        return []  # No se encontró un camino

# --- EJECUCIÓN DEL EJEMPLO COMPLETO ---
print("--- Creación de Grafo No Dirigido ---")
mi_grafo = Grafo(es_derigido = False)

mi_grafo.agregar_arista('Managua', 'Masaya')
mi_grafo.agregar_arista('Managua', 'León')
mi_grafo.agregar_arista('Granada', 'Rivas')
mi_grafo.agregar_arista('Managua', 'Granada')  # Arista adicional para mayor conectividad

mi_grafo.imprimir_grafo()

print("\n--- Operaciones Básicas ---")
print(f"Vecinos de Managua: {mi_grafo.obtener_vecinos('Managua')}")
print(f"¿Existe arista entre Managua y Masaya? {mi_grafo.existe_arista('Managua', 'Masaya')}")
print(f"¿Existe arista entre Managua y Rivas? {mi_grafo.existe_arista('Managua', 'Rivas')}")

print("\n--- Recorridos ---")
print(f"Orden de recorrido BFS desde Managua: {mi_grafo.bfs('Managua')}")
print(f"Orden de recorrido DFS desde Managua: {mi_grafo.dfs('Managua')}")

print("\n--- Conectividad y Caminos ---")
print(f"¿Es el grafo conexo? {mi_grafo.es_conexo()}")

camino = mi_grafo.encontrar_camino('Managua', 'Rivas')
print(f"Camino de Managua a Rivas: {camino}")

camino_inexistente = mi_grafo.encontrar_camino('Managua', 'Juigalpa')
print(f"Camino de Managua a Juigalpa: {camino_inexistente}")

# --- Probar con un grafo dirigido ---
print("\n--- Creación de Grafo Dirigido ---")
grafo_dirigido = Grafo(es_derigido = True)
grafo_dirigido.agregar_arista('Inicio', 'A')
grafo_dirigido.agregar_arista('A', 'B')
grafo_dirigido.agregar_arista('B', 'C')
grafo_dirigido.agregar_arista('C', 'Fin')
grafo_dirigido.agregar_arista('Inicio', 'D')
grafo_dirigido.agregar_arista('D', 'Fin')

grafo_dirigido.imprimir_grafo()

print(f"Vecinos de Inicio (dirigido): {grafo_dirigido.obtener_vecinos('Inicio')}")
print(f"Vecinos de Fin (dirigido): {grafo_dirigido.obtener_vecinos('Fin')}")  # Debería ser vacío
print(f"Existe arista de A a B: {grafo_dirigido.existe_arista('A', 'B')}")
print(f"Existe arista de B a A: {grafo_dirigido.existe_arista('B', 'A')}")  # Debería ser False

print("\n--- Recorridos en Grafo Dirigido ---")
print(f"Orden de recorrido BFS desde Inicio: {grafo_dirigido.bfs('Inicio')}")
print(f"Orden de recorrido DFS desde Inicio: {grafo_dirigido.dfs('Inicio')}")

print("\n--- Conectividad y Caminos en Grafo Dirigido ---")
# es_conexo no es tan directamente aplicable a grafos dirigidos sin modificar la definición
# pero podemos encontrar caminos
camino_dirigido = grafo_dirigido.encontrar_camino('Inicio', 'Fin')
print(f"Camino dirigido de Inicio a Fin: {camino_dirigido}")

camino_dirigido_no_existente = grafo_dirigido.encontrar_camino('Fin', 'Inicio')
print(f"Camino dirigido de Fin a Inicio: {camino_dirigido_no_existente}")