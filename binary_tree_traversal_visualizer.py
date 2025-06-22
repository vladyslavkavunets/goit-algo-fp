import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, 
            node_color=colors, font_size=16, font_weight='bold')
    plt.title(title, fontsize=14, fontweight='bold')
    plt.show()

def heap_to_tree(heap_array):
    if not heap_array:
        return None
    
    nodes = [Node(val) for val in heap_array]
    
    for i in range(len(heap_array)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        
        if left_index < len(heap_array):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap_array):
            nodes[i].right = nodes[right_index]
    
    return nodes[0]

def get_color_by_order(order, total_nodes, traversal_type="DFS"):
    if traversal_type == "DFS":
        base_color = 0x1296F0
    else:
        base_color = 0x12F064
    
    r = (base_color >> 16) & 0xFF
    g = (base_color >> 8) & 0xFF  
    b = base_color & 0xFF
    
    intensity = 0.3 + 0.7 * (order / (total_nodes - 1))
    
    new_r = int(r * intensity)
    new_g = int(g * intensity)
    new_b = int(b * intensity)
    
    return f"#{new_r:02x}{new_g:02x}{new_b:02x}"

def dfs_traversal(root):
    if not root:
        return []
    
    stack = [root]
    visited_order = []
    
    while stack:
        node = stack.pop()
        visited_order.append(node)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return visited_order

def bfs_traversal(root):
    if not root:
        return []
    
    queue = deque([root])
    visited_order = []
    
    while queue:
        node = queue.popleft()
        visited_order.append(node)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return visited_order

def reset_tree_colors(root, default_color="lightblue"):
    if root:
        root.color = default_color
        reset_tree_colors(root.left, default_color)
        reset_tree_colors(root.right, default_color)

def visualize_traversal(root, traversal_type="DFS"):
    reset_tree_colors(root)
    
    if traversal_type == "DFS":
        visited_order = dfs_traversal(root)
        title = "Обхід в глибину (DFS) - використання стеку"
    else:
        visited_order = bfs_traversal(root)
        title = "Обхід в ширину (BFS) - використання черги"
    
    total_nodes = len(visited_order)
    for i, node in enumerate(visited_order):
        node.color = get_color_by_order(i, total_nodes, traversal_type)
    
    draw_tree(root, title)
    
    print(f"\n{title}")
    print("Порядок обходу:", [node.val for node in visited_order])
    print("Кольори від темного до світлого відображають послідовність обходу")

def main():
    elements = [1, 3, 5, 7, 9, 2, 4]
    heap = []
    
    print("Елементи для створення дерева:", elements)
    
    for e in elements:
        heapq.heappush(heap, e)
    
    print("Структура купи:", heap)
    
    root = heap_to_tree(heap)
    
    print("\n" + "="*60)
    print("ВІЗУАЛІЗАЦІЯ ОБХОДІВ БІНАРНОГО ДЕРЕВА")
    print("="*60)
    
    reset_tree_colors(root, "lightgray")
    draw_tree(root, "Початкове бінарне дерево (мін-купа)")
    
    print("\n1. ОБХІД В ГЛИБИНУ (DFS)")
    print("-" * 30)
    visualize_traversal(root, "DFS")
    
    print("\n2. ОБХІД В ШИРИНУ (BFS)")
    print("-" * 30)
    visualize_traversal(root, "BFS")
    
    print("\n" + "="*60)
    print("ПОЯСНЕННЯ КОЛЬОРІВ:")
    print("• DFS (синій): Темні відтінки - вузли, відвідані першими")
    print("• BFS (зелений): Світлі відтінки - вузли, відвідані останніми") 
    print("• Використовується 16-система RGB (1296F0 - синій, 12F064 - зелений)")
    print("="*60)

if __name__ == "__main__":
    main()