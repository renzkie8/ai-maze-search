import networkx as nx
import matplotlib.pyplot as plt
import heapq  # For the priority queue

# Instantiating a node class
class Node:
    def __init__(self, state, parent=None, cost=0, hn=0):
        self.state = state
        self.parent = parent
        self.action = []
        self.cost = cost
        self.hn = hn  # Heuristic
        self.f_cost = cost + hn  # Total cost (g(n) + h(n))
    
    def add_action(self, action_node, cost):
        self.action.append((action_node, cost))

    def __str__(self):
        return self.state

    def __lt__(self, other):
        return self.f_cost < other.f_cost

class AStar:
    def __init__(self):
        self.frontier = []
        self.entry_finder = {}  # mapping of nodes to entries in the priority queue

    def add(self, node):
        if node.state in self.entry_finder:
            self.remove(node.state)
        entry = [node.f_cost, node]
        self.entry_finder[node.state] = entry
        heapq.heappush(self.frontier, entry)

    def remove(self, state):
        entry = self.entry_finder.pop(state)
        entry[-1] = None  # Mark as removed

    def contains_state(self, state):
        return state in self.entry_finder

    def empty(self):
        while self.frontier and self.frontier[0][-1] is None:
            heapq.heappop(self.frontier)
        return len(self.frontier) == 0

    def remove(self):
        while self.frontier:
            _, node = heapq.heappop(self.frontier)
            if node is not None:
                del self.entry_finder[node.state]
                return node
        raise Exception("empty frontier")

# Creating nodes
Arad = Node(state="Arad", hn=366)
Zerind = Node(state="Zerind", parent=Arad, cost=75, hn=374)
Oradea = Node(state="Oradea", parent=Zerind, cost=71, hn=380)
Sibiu = Node(state="Sibiu", parent=Arad, cost=140, hn=253)
Rimnicu_Vilcea = Node(state="Rimnicu Vilcea", parent=Sibiu, cost=80, hn=193)
Craiova = Node(state="Craiova", parent=Rimnicu_Vilcea, cost=146, hn=160)
Drobeta = Node(state="Drobeta", parent=Craiova, cost=120, hn=142)
Mehadia = Node(state="Mehadia", parent=Drobeta, cost=75, hn=0)
Timisoara = Node(state="Timisoara", parent=Arad, cost=118, hn=329)
Lugoj = Node(state="Lugoj", parent=Mehadia, cost=70, hn=0)
Pitesti = Node(state="Pitesti", parent=Craiova, cost=138, hn=98)
Bucharest = Node(state="Bucharest", parent=Pitesti, cost=101, hn=0)
Giurgiu = Node(state="Giurgiu", parent=Bucharest, cost=90, hn=77)
Fagaras = Node(state="Fagaras", parent=Sibiu, cost=99, hn=178)
Neamt = Node(state="Neamt", hn=0)
Iasi = Node(state="Iasi", parent=Neamt, cost=87, hn=0)
Vaslui = Node(state="Vaslui", parent=Iasi, cost=92, hn=0)
Urziceni = Node(state="Urziceni", parent=Vaslui, cost=142, hn=80)
Eforie = Node(state="Eforie", hn=0)
Hirsova = Node(state="Hirsova", cost=86, parent=Eforie, hn=0)

# Instantiating a graph
G = nx.DiGraph()

# Adding actions (edges) to nodes
Arad.add_action(Timisoara, 118)
Arad.add_action(Zerind, 75)
Arad.add_action(Sibiu, 140)
Zerind.add_action(Oradea, 71)
Oradea.add_action(Sibiu, 151) 
Sibiu.add_action(Fagaras, 99)
Sibiu.add_action(Rimnicu_Vilcea, 80)
Craiova.add_action(Rimnicu_Vilcea, 146)
Drobeta.add_action(Craiova, 120)
Mehadia.add_action(Drobeta, 75)
Lugoj.add_action(Mehadia, 70)
Timisoara.add_action(Lugoj, 70)
Craiova.add_action(Pitesti, 138)
Pitesti.add_action(Rimnicu_Vilcea, 97)  
Rimnicu_Vilcea.add_action(Pitesti, 138)
Pitesti.add_action(Bucharest, 101)
Giurgiu.add_action(Bucharest, 90)
Fagaras.add_action(Bucharest, 211)  
Iasi.add_action(Vaslui, 92)
Vaslui.add_action(Urziceni, 142)
Urziceni.add_action(Bucharest, 80)
Eforie.add_action(Hirsova, 86)
Hirsova.add_action(Urziceni, 98)  

# Adding edges to the graph with weights (gn and hn)
edges = []
for node in [Arad, Zerind, Oradea, Sibiu, Rimnicu_Vilcea, Craiova, Drobeta, Mehadia, Timisoara, Lugoj, Pitesti, Bucharest, Giurgiu, Fagaras, Neamt, Iasi, Vaslui, Urziceni, Eforie, Hirsova]:
    for action_node, cost in node.action:
        edges.append((node.state, action_node.state, cost))

G.add_weighted_edges_from(edges)

# Drawing the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d for u, v, d in edges})
plt.show()

# Setting the goal
goal = Bucharest

# Empty solution
solution = []

# Empty frontier (A*)
frontier = AStar()

# Empty explored set
explored = set()

# Add the initial state to the frontier
frontier.add(Arad)

while True:
    # If the frontier is empty, then no solution
    if frontier.empty():
        raise Exception("no solution")

    # Remove a node from the frontier
    node = frontier.remove()
    print(f"Node {node.state} was removed from the Frontier.")
    
    solution.append(node.state)

    # If node contains goal state, return the solution
    if goal.state == node.state:
        print(f"{node.state} was reached. This is the goal.")
        print(f"Here is the solution: {solution}")
        break

    # Adding to the explored set
    explored.add(node.state)
    print(f"{node.state} Added to Explored.")

    # Expanding the node and adding the resulting nodes to the frontier
    print("\nPossible actions: ", end="")
    for action_node, cost in node.action:
        if action_node.state not in explored and not frontier.contains_state(action_node.state):
            action_node.cost = node.cost + cost  # Update the cost to reach the action node
            action_node.f_cost = action_node.cost + action_node.hn  # Update the total cost
            frontier.add(action_node)
            print(f"{action_node.state} Added to Frontier.")
        else:
            print("nah")
    print("\n\n")
