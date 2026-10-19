import networkx as nx
import matplotlib.pyplot as plt

# Instantiating a node class
class Node:
    def __init__(self, state, parent=None, cost=0, hn=0):
        self.state = state
        self.parent = parent
        self.action = []
        self.cost = cost
        self.hn = hn
    
    def add_action(self, action_node, cost):
        self.action.append((action_node, cost))

    def __str__(self):
        return self.state

class GBFS:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
        self.frontier.sort(key=lambda x: x.hn)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            return self.frontier.pop(0)

# creating nodes
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

#instantiating a graph
G = nx.DiGraph()

# adding actions (edges) to nodes
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



# Adding edges to the graph with weights(gn and hn)
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

# setting the goal
goal = Bucharest

#empty solution
solution = []

#empty frontier (can be changed to DFS or BFS)
frontier = GBFS()

# empty explored set
explored = []

# add the initial state to the frontier
frontier.add(Arad)

while True:
    # if the frontier is empty, then no solution
    if frontier.empty():
        raise Exception("no solution")

    # remove a node from the frontier
    print("Frontier: " + str([fnode.state for fnode in frontier.frontier]))
    print("Explored: " + str([fnode.state for fnode in explored]))

    node = frontier.remove()
    print(node.state + " was removed from the Frontier.")
    
    solution.append(node.state)

    # if node contains goal state, return the solution
    if goal.state == node.state:
        print(node.state + " was reached. This is the goal.")
        print("Here is the solution: " + str(solution))
        break

    # adding to the explored set
    explored.append(node)
    print(node.state + " Added to Explored.")

    # expanding the node and adding the resulting nodes to the frontier
    print("\nPossible actions: ", end="")
    for action_node, cost in node.action:
        if not frontier.contains_state(action_node.state) and action_node not in explored:
            print(action_node.state + " Added to Frontier.")
            frontier.add(action_node)
        else:
            print("nah")
    print("\n\n")
