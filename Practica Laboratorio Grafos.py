import collections

####Parte echa por Julio 
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
    
    #### Parte echa por Yaritza
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

    def es_conexo(self):
        if not self.grafo:
            return False

        # Tomar el primer vértice para iniciar el BFS/DFS
        primer_vertice = next(iter(self.grafo))

        # Realizar un BFS desde el primer vértice
        recorrido_bfs = self.bfs(primer_vertice)
        
        # Verificar si todos los vértices están en el recorrido
        """Comparando si el numero de vertices que se puedieron encontrar en el recorrido y 
        el numero de vertices, si esto es igual retorna True de lo contrario retorna False"""
        return len(recorrido_bfs) == len(self.grafo)

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


#Parte echa por Enoc Y Yaritza
# ----------- Prueba con grafo no dirigido -------------
print("============ Grafo No Dirigido =============")
g1 = Grafo(es_derigido=False)

# Agrega vértices
# F es un grafo desconectado para comprobar como se comporta BFS y DFS
for v in ['A', 'B', 'C', 'D', 'E', 'F']:
    g1.agregar_vertice(v)

# Agrega conexiones entre los vértices
g1.agregar_arista('A', 'B')
g1.agregar_arista('A', 'C')
g1.agregar_arista('B', 'D')
g1.agregar_arista('C', 'D')
g1.agregar_arista('D', 'E')

# Mostrar vecinos de algunos vértices
print("Vecinos de A:", g1.obtener_vecinos('A'))
print("Vecinos de D:", g1.obtener_vecinos('D'))
print("Vecinos de F:", g1.obtener_vecinos('F'))  # F no existe

# Verifica si existen ciertas aristas
print("¿Existe arista A-C?", g1.existe_arista('A', 'C'))
print("¿Existe arista A-D?", g1.existe_arista('A', 'D'))

print("\n--- Recorridos en Grafo no Dirigido ---")
print(f"Orden de recorrido BFS desde Inicio: {g1.bfs('A')}\n")
print(f"Orden de recorrido DFS desde Inicio: {g1.dfs('A')}")

#Aqui se comprube si el grafo es conexo o no, en este caso El grafo no es dirigido
print("\n--- Conectividad ---")
print(f"¿Es el grafo conexo? {g1.es_conexo()}")

print("\n--- Conectividad y Caminos en Grafo Dirigido ---")
#Encontrar Camino De A a E y De A a un Vertice inexistente
camino_dirigido = g1.encontrar_camino('A', 'E')
print(f"Camino dirigido de Inicio a Fin: {camino_dirigido}")

camino_dirigido_no_existente = g1.encontrar_camino('E', 'A')
print(f"Camino dirigido de Fin a Inicio: {camino_dirigido_no_existente}")

#Encontrar Camino de A a un Vertice Inexistente
print("\n--- Caminos en Grafo No Dirigido Vertice Inexistente ---")
camino_dirigido = g1.encontrar_camino('A', 'F')
print(f"Camino dirigido de Inicio a Fin: {camino_dirigido}")

camino_dirigido_no_existente = g1.encontrar_camino('F', 'A')
print(f"Camino dirigido de Fin a Inicio: {camino_dirigido_no_existente}")

# ----------- Prueba con grafo dirigido -------------
print("\n========== Grafo Dirigido =============")
g2 = Grafo(es_derigido=True)

# Agrega aristas (los vértices se crean solos si no existen)
g2.agregar_arista('X', 'Y')
g2.agregar_arista('Y', 'Z')
g2.agregar_arista('X', 'Z')

#En este caso se comprueba si el grafo dirigido es conexo
print("\n--- Conectividad y Caminos ---")
print(f"¿Es el grafo conexo? {g2.es_conexo()}")

# Muestra los vecinos de cada vértice
print("Vecinos de X:", g2.obtener_vecinos('X'))
print("Vecinos de Y:", g2.obtener_vecinos('Y'))
print("Vecinos de Z:", g2.obtener_vecinos('Z'))
