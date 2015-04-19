import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from MarkovChain import *
from chord_extractor import *
import Tkinter as Tk
import time


def create_graph():
    g = nx.Graph()

    bla = [[('a', 2), ('b', 3)], [('a', 10), ('c', 2)]]

    #m = MarkovChain(get_all_progressions())
    m = MarkovChain(bla)

    nodes_dict = {}
    nodes = list(m.nodes)
    print nodes

    for i in range(0, len(nodes)):
        g.add_node(i)
        nodes_dict[nodes[i]] = i

    queue = [m.START]
    visited_nodes = set()

    while len(queue) > 0:
        curr_node = queue.pop(0)

        while curr_node in visited_nodes:
            if len(queue) == 0:
                return g

            curr_node = queue.pop(0)

        visited_nodes.add(curr_node)

        for n in m.neighbours[curr_node]:
            if n not in visited_nodes:
                queue.insert(0, n)

            g.add_edge(nodes_dict[curr_node], nodes_dict[n])

    return (g, nodes_dict)
            
root = Tk.Tk()
root.wm_title("Markov Chain")
root.wm_protocol('WM_DELETE_WINDOW', root.quit())

g = create_graph()
nodes_dict = g[1]
g = g[0]

pos = nx.circular_layout(g)

w,h=plt.figaspect(1)
f = plt.figure(figsize=(w,h))
a = f.add_subplot(111)
plt.axis('off')

nx.draw_networkx(g, pos=pos, ax=a)
xlim = a.get_xlim()
ylim = a.get_ylim()

canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def next(node):
    a.cla()
    other_nodes = [n for n in g.nodes() if not n == nodes_dict[node]]
    print other_nodes
    print [nodes_dict[node]]
    nx.draw_networkx_nodes(g, pos=pos, nodelist=[nodes_dict[node]], node_color='b', ax=a, node_size=1000)
    nx.draw_networkx_nodes(g, pos=pos, nodelist=other_nodes, node_color='w', ax=a)
    nx.draw_networkx_edges(g, pos=pos, ax=a)
    a.set_xlim(xlim)
    a.set_ylim(ylim)
    plt.axis('off')
    canvas.draw()

Tk.mainloop()

