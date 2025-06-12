class Grafo:
    def __init__(self, es_dirigido=False):
        # Guarda si el grafo es dirigido o no
        self.es_dirigido = es_dirigido
        # Cada vértice tendrá una lista con sus vecinos
        self.vertices = {}

    def agregar_vertice(self, vertice):
        # Agrega el vértice si no está en el grafo
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, u, v, peso=1):
        # Asegura que los dos vértices existan
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        # Agrega conexión de u a v
        self.vertices[u].append((v, peso))
        # Si no es dirigido, agrega también de v a u
        if not self.es_dirigido:
            self.vertices[v].append((u, peso))

    def obtener_vecinos(self, vertice):
        # Devuelve la lista de vecinos si existe el vértice
        if vertice in self.vertices:
            return self.vertices[vertice]
        else:
            return []

    def existe_arista(self, u, v):
        # Verifica si v está entre los vecinos de u
        if u in self.vertices:
            for vecino, _ in self.vertices[u]:
                if vecino == v:
                    return True
        return False


# ----------- Prueba con grafo no dirigido -------------
print("Grafo No Dirigido")
g1 = Grafo(es_dirigido=False)

# Agrega vértices
for v in ['A', 'B', 'C', 'D', 'E']:
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

# ----------- Prueba con grafo dirigido -------------
print("\nGrafo Dirigido")
g2 = Grafo(es_dirigido=True)

# Agrega algunas aristas (los vértices se crean solos si no existen)
g2.agregar_arista('X', 'Y')
g2.agregar_arista('Y', 'Z')

# Muestra los vecinos de cada vértice
print("Vecinos de X:", g2.obtener_vecinos('X'))
print("Vecinos de Y:", g2.obtener_vecinos('Y'))
print("Vecinos de Z:", g2.obtener_vecinos('Z'))