import networkx as nx
import matplotlib.pyplot as plt
from MarkovChain import *
from chord_extractor import *


def create_graph():
    g = nx.Graph()

    m = MarkovChain(get_all_progressions())

    nodes_dict = {}
    nodes = list(m.nodes)


    for i in range(0, len(nodes)):
        g.add_node(i)
        nodes_dict[nodes[i]] = i

    queue = [m.START]
    visited_nodes = set()

    while len(queue) > 0:
        curr_node = queue.pop(0)

        while curr_node in visited_nodes:
            curr_node = queue.pop(0)

        visited_nodes.update(curr_node)

        for n in m.neighbours[curr_node]:
            if n not in visited_nodes:
                queue.insert(0, n)

            print "adding edge..." + str(nodes_dict[n])

            g.add_edge(nodes_dict[curr_node], nodes_dict[n])

    return g
            

g = create_graph()
nx.draw_circular(g)
plt.show()
