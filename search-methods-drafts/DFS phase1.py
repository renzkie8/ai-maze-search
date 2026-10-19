import networkx as nx #pip install networkx
import matplotlib.pyplot as plt  #pip install matplotlib

#instantiating a node class
class Node():
    def __init__(self, state=None, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = []
        self.cost = cost
    
    def add_action(self, action):
        self.action.append(action)
        return (self.state, action.state)

    def actions(self):
        for action in self.action:
            print(action.state, end =" ")

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier) or any(explored_node.state == state for explored_node in explored)

class DFS():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

#creating node
Arad = Node(state="Arad", parent=None,cost=0)
Zerind = Node(state="Zerind", parent=Arad,cost=0)
Oradea = Node(state="Oradea", parent=Zerind,cost=0)
Sibiu = Node(state="Sibiu", parent=Arad,cost=0)
Rimnicu_Vilcea = Node(state="Rimnicu Vilcea", parent=Sibiu,cost=0)
Craiova = Node(state="Craiova", parent=Rimnicu_Vilcea, cost=0)
Drobeta = Node(state="Drobeta", parent=Craiova, cost=0)
Mehadia = Node(state="Mehadia", parent=Drobeta, cost=0)
Timisoara = Node(state="Timisoara", parent=Arad, cost=0)
Lugoj = Node(state="Lugoj", parent=Mehadia,cost=0)
Pitesti = Node(state="Pitesti", parent=Craiova, cost=0)
Bucharest = Node(state="Bucharest", parent=Pitesti, cost=0)
Giurgiu = Node(state="Giurgiu", parent=Bucharest, cost=0)
Fagaras = Node(state="Fagaras", parent=Sibiu, cost=0)
Neamt = Node(state="Neamt", parent=None, cost=0)
Iasi = Node(state="Iasi", parent=Neamt,cost=0)
Vaslui = Node(state="Vaslui", parent=Iasi,cost=0)
Urziceni= Node(state="Arad", parent=Vaslui,cost=0)
Eforie= Node(state="Eforie", parent=None, cost=0)
Hirsova = Node(state="Hirsova", parent=Eforie, cost=0)
Urziceni = Node(state="Urziceni", parent=Hirsova,cost=0)

#instantiating a graph
Graph=nx.DiGraph()

#adding actions
Graph.add_edges_from([
Arad.add_action(Sibiu),#0
Arad.add_action(Timisoara),
Arad.add_action(Zerind),#1
Zerind.add_action(Oradea),#2
Oradea.add_action(Sibiu),#3
Sibiu.add_action(Fagaras),
Sibiu.add_action(Rimnicu_Vilcea), ###
Craiova.add_action(Rimnicu_Vilcea),
Drobeta.add_action(Craiova),
Mehadia.add_action(Drobeta),
Lugoj.add_action(Mehadia),
Timisoara.add_action(Lugoj),
Craiova.add_action(Pitesti),
Rimnicu_Vilcea.add_action(Pitesti),
Pitesti.add_action(Bucharest),
Giurgiu.add_action(Bucharest),
Fagaras.add_action(Bucharest),
Neamt.add_action(Iasi),
Iasi.add_action(Vaslui),
Vaslui.add_action(Urziceni),
Urziceni.add_action(Bucharest),
Eforie.add_action(Hirsova),
Hirsova.add_action(Urziceni)

])

pos = {
    "Arad": (1, 2),
    "Zerind": (1.5, 2.5),
    "Timisoara": (1.5, 1),
    "Lugoj": (3.7, 0.7),
    "Oradea": (2, 3),
    "Sibiu": (4.8, 1.8),
    "Rimnicu Vilcea": (6, 1.3),
    "Craiova": (6.7, -0.8),
    "Drobeta": (4, -0.6),
    "Mehadia": (4, 0.2),
    "Pitesti": (8.7, 1),
    "Bucharest": (12.5, 0),
    "Giurgiu": (12, -0.8),
    "Fagaras": (8.5, 1.8),
    "Neamt": (14, 3),
    "Iasi": (16, 2),
    "Vaslui": (15, 1),
    "Urziceni": (14, 0.5),
    "Eforie": (18, -0.8),
    "Hirsova": (16, 0.4)
}

nx.draw(Graph, pos, with_labels=True, edge_color='b', node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(Graph, 'weight')
nx.draw_networkx_edge_labels(Graph, pos, edge_labels=labels)
plt.show()

#setting the goal
goal = Bucharest

#empty solution
solution = []

#empty frontier (can be changed to DFS or BFS)
frontier = DFS()

#empty explored set
explored = []

#add the initial state to the frontier
frontier.add(Arad)

print("***********************************************")
while True:
    #if the frontier is empty, then no solution
    if frontier.empty():
        raise Exception("no solution")
    
    print("Frontier: " + str([fnode.state for fnode in frontier.frontier]))
    print("Explored: " + str([fnode.state for fnode in explored]))

    #remove a node from the frontier
    node = frontier.remove()
    print(node.state + " was removed from the Frontier.")
    
    #add node to the solution
    solution.append(node.state)

    #if node contains goal state, return the solution
    if goal.state == node.state:
        print(node.state + " was reached. This is the goal.")
        print("Here is the solution: " + str(solution))
        break

    #adding to the explored set
    explored.append(node)
    print(node.state + " Added to Explored.")
    

    #expanding the node and adding the resulting node/s to the frontier
    for action in node.action:
        if not frontier.contains_state(action) and all(explored_node.state != action.state for explored_node in explored):
            print(action.state + " Added to Frontier.")
            frontier.add(action)
            
    print("***********************************************")









