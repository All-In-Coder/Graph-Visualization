import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_edge(1, 2,color='r')
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
color = []
node_size = []
weight = []
for node in g:
    if node==1 or node==5:
        color.append('blue')
        node_size.append(500)
        weight.append(4)
    else:
        color.append('green')
        node_size.append(3500)
        weight.append(10)

nx.draw(g, with_labels=True,node_color=color,node_size = node_size,width=weight)
#
#
#
#
#
# # G = nx.Graph()
# # G.add_edge(0,1,color='r',weight=2)
# # G.add_edge(1,2,color='g',weight=4)
# # G.add_edge(2,3,color='b',weight=6)
# # G.add_edge(3,4,color='y',weight=3)
# # G.add_edge(4,0,color='m',weight=1)
# #
# # colors = nx.get_edge_attributes(G,'color').values()
# # weights = nx.get_edge_attributes(G,'weight').values()
# #
# # pos = nx.circular_layout(G)
# # nx.draw(G, pos,
# #         edge_color=colors,
# #         width=list(weights),
# #         with_labels=True,
# #         node_color='lightgreen')
# # plt.savefig("h.png")
#
#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro')
#
# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,
#
# def update(frame):
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     return ln,
#
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
plt.show()