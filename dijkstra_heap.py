import heapq
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    
    def add_edge(self, from_vertex, to_vertex, weight):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))
        self.edges.append((from_vertex, to_vertex, weight))
    
    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        previous = {vertex: None for vertex in self.vertices}
        
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.vertices[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances, previous
    
    def get_shortest_path(self, start, end, previous):
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path.reverse()
        
        if path[0] != start:
            return None
        
        return path
    
    def visualize_graph(self, start_vertex=None, distances=None, paths=None):
        G = nx.Graph()
        
        for vertex in self.vertices:
            G.add_node(vertex)
        
        for from_v, to_v, weight in self.edges:
            G.add_edge(from_v, to_v, weight=weight)
        
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, seed=42, k=2, iterations=50)
        
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                              node_size=1500)
        
        if start_vertex:
            nx.draw_networkx_nodes(G, pos, nodelist=[start_vertex],
                                  node_color='lightgreen', node_size=1500)
        
        nx.draw_networkx_edges(G, pos)
        
        nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')
        
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=12)
        
        if distances and start_vertex:
            distance_labels = {}
            for node in G.nodes():
                x, y = pos[node]
                plt.text(x, y-0.15, f"d={distances[node]}", 
                        horizontalalignment='center',
                        fontsize=10, color='red', weight='bold')
        
        plt.title("Граф з найкоротшими відстанями від початкової вершини", 
                 fontsize=16)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

def create_sample_graph():
    g = Graph()
    
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3)
    ]
    
    for from_v, to_v, weight in edges:
        g.add_edge(from_v, to_v, weight)
    
    return g

def main():
    print("=== Алгоритм Дейкстри з бінарною купою ===\n")
    
    graph = create_sample_graph()
    
    print("Граф створено з вершинами:", list(graph.vertices.keys()))
    print("\nРебра графа:")
    for from_v, to_v, weight in graph.edges:
        print(f"  {from_v} -- {to_v}: вага {weight}")
    
    start_vertex = 'A'
    print(f"\nЗапускаємо алгоритм Дейкстри з початкової вершини: {start_vertex}")
    
    distances, previous = graph.dijkstra(start_vertex)
    
    print(f"\nНайкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in sorted(distances.items()):
        if distance == float('infinity'):
            print(f"  {vertex}: недосяжна")
        else:
            print(f"  {vertex}: {distance}")
    
    print("\nНайкоротші шляхи:")
    for vertex in sorted(graph.vertices.keys()):
        if vertex != start_vertex:
            path = graph.get_shortest_path(start_vertex, vertex, previous)
            if path:
                path_str = " -> ".join(path)
                print(f"  {start_vertex} до {vertex}: {path_str} (відстань: {distances[vertex]})")
    
    print("\nВізуалізація графа...")
    graph.visualize_graph(start_vertex, distances)

if __name__ == "__main__":
    main()