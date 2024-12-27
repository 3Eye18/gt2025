class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, vertex):
        if not isinstance(vertex, Vertex):
            raise TypeError("Argument must be of type Vertex")
        else:
            self.neighbors.append(vertex)
        
class Graph:
    def __init__(self, vertices = []):
        self.subgraphs = []
        self.vertices = vertices
        self.start_vertex = None
    
    def add_vertex(self, vertex: Vertex):
        self.vertices.append(vertex)
    
    def add_subgraph(self, subgraph):
        if not isinstance(subgraph, Graph):
            raise TypeError("Argument must be of type Graph")
        else:
            self.subgraphs.append(subgraph)

    def check_path_existence(self, vertex1: Vertex, vertex2: Vertex):
        if not vertex1.visited:
            vertex1.visited = True
            if vertex2 in vertex1.neighbors:
                for vertex in self.vertices:
                    vertex.visited = False
                print("True")
                return
            else:
                for vertex in vertex1.neighbors:
                    self.check_path_existence(vertex, vertex2)
    
a = Vertex(1)
b = Vertex(2)
c = Vertex(3)
d = Vertex(4)
e = Vertex(5)
f = Vertex(6)
g = Vertex(7)

a.add_neighbor(b)
b.add_neighbor(a)
b.add_neighbor(e)
c.add_neighbor(f)
d.add_neighbor(f)
d.add_neighbor(g)
e.add_neighbor(b)
f.add_neighbor(c)
f.add_neighbor(g)
g.add_neighbor(d)
g.add_neighbor(f)

gr = Graph([a,b,c,d,e,f,g])
gr.check_path_existence(a, e)
    
