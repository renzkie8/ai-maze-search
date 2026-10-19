import networkx as nx
import matplotlib.pyplot as plt

#instantiating a node class
class Node():
    def __init__(self, state, parent, hn=0):
        self.state = state
        self.parent = parent
        self.action = []
        self.hn = hn
    
    def add_action(self, action):
        self.action.append(action)
        return ((self.state, action.state), action.hn)

    def actions(self):
        for action in self.action:
            print(action.name, end =" ")

class GBFS():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        c=float('inf')
        if self.empty():
            raise Exception("empty frontier")
        else:
            for node in self.frontier:
                if(node.hn < c):
                    index = self.frontier.index(node)
                    c=node.hn
        return self.frontier.pop(index)



#creating node
Neamt = Node(state = "Neamt", parent = None, hn = 0)
Iasi = Node(state = "Iasi", parent = Neamt, hn = 87)
Vaslui = Node(state = "Vaslui", parent = Iasi, hn = 92)
Urziceni = Node(state = "Urziceni", parent = Vaslui, hn = 142)
Hirsova = Node(state = "Hirsova", parent = Urziceni, hn = 98)
Eforie = Node(state = "Eforie", parent = Hirsova, hn = 86)
Bucharest = Node(state = "Bucharest", parent = Urziceni, hn = 85)
Giurgiu = Node(state = "Giurgiu", parent = Bucharest, hn = 90)
Fagaras = Node(state = "Fagaras", parent = Bucharest, hn = 211)
Pitesti = Node(state = "Pitesti", parent = Bucharest, hn = 101)
Craiova = Node(state = "Craiova", parent = Pitesti, hn = 138)
RimnicuVilcea = Node(state = "Rimnicu Vilcea", parent = Pitesti, hn = 97)
Sibiu = Node(state = "Sibiu", parent = Fagaras, hn = 99)
Oradea = Node(state = "Oradea", parent = Sibiu, hn = 151)
Zerind = Node(state = "Zerind", parent = Oradea, hn = 71)
Arad = Node(state = "Arad", parent = Sibiu, hn = 140)
Timisoara = Node(state = "Timisoara", parent = Arad, hn = 118)
Lugoj = Node(state = "Lugoj", parent = Timisoara, hn = 111)
Mehadia = Node(state = "Mehadia", parent = Lugoj, hn = 70)
Drobeta = Node(state = "Drobeta", parent = Craiova, hn = 120)

#instantiating a graph
G=nx.DiGraph()

pcost=dict([
    Neamt.add_action(Iasi),
    Iasi.add_action(Vaslui),
    Vaslui.add_action(Urziceni),
    Urziceni.add_action(Hirsova),
    Urziceni.add_action(Bucharest),
    Hirsova.add_action(Eforie),
    Bucharest.add_action(Giurgiu),
    Bucharest.add_action(Pitesti),
    Bucharest.add_action(Fagaras),
    Pitesti.add_action(Craiova),
    Pitesti.add_action(RimnicuVilcea),
    RimnicuVilcea.add_action(Craiova),
    RimnicuVilcea.add_action(Sibiu),
    Fagaras.add_action(Sibiu),
    Sibiu.add_action(Oradea),
    Sibiu.add_action(Arad),
    Oradea.add_action(Zerind),
    Arad.add_action(Zerind),
    Arad.add_action(Timisoara),
    Timisoara.add_action(Lugoj),
    Lugoj.add_action(Mehadia),
    Mehadia.add_action(Drobeta),
    Craiova.add_action(Drobeta),
])

#adding actions
G.add_edges_from(pcost  .keys())

#drawing actions
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=pcost)   
plt.show()


#setting the goal
goal = Mehadia

#empty solution
solution = []

#empty frontier (can be changed to DFS or BFS)
frontier = GBFS()

#empty explored set
explored = []

#add the initial state to the frontier
frontier.add(Iasi)

while True:
    #if the frontier is empty, then no solution
    if frontier.empty():
        raise Exception("no solution")

    #remove a node from the frontier
    print("frontier: ", end="")
    for front in frontier.frontier:
        print(front.state, end=", ")
    node = frontier.remove()
    print("\nremove: "+node.state)
    
    
    solution.append(node.state)

    #if node contains goal state, return the solution
    if goal.state == node.state:
        print("[SOLVED]:" + str(solution))
        break

    #adding to the explored set
    explored.append(node)
    print("explored: ", end="")
    for exp in explored:
        print(exp.state, end=", ")

    #expanding the node and adding the resulting node/s to the frontier
    print("\npossible action: ", end="")
    for action in node.action:
        if not frontier.contains_state(action) and action not in explored:
            print(action.state, end=", ")
            frontier.add(action)
        else:
            print("nah")
    print("\n\n")